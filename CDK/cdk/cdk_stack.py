from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    CfnOutput,
    aws_iam as iam,
    aws_secretsmanager as secretsmanager,
    CfnTag,
    RemovalPolicy,
    SecretValue,
)
import uuid
from constructs import Construct
import os
from dotenv import load_dotenv

load_dotenv()

class RDS(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create the VPC
        self.vpc = ec2.Vpc(
            self,
            "group9Vpc",
            max_azs=2,  # Limit to 2 Availability Zones
            subnet_configuration=[
                # Public Subnet Configuration
                ec2.SubnetConfiguration(
                    name="public-subnet-1",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                # Private Subnet Configuration
                ec2.SubnetConfiguration(
                    name="private-subnet-1",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24,
                ),
            ],
        )

        # create security group for ec2
        self.ec2SecurityGroup = self.create_ec2_sg()

        
        self.RDSSecurityGroup = self.create_RDS_sg()

        self.host, self.dbName, self.port, self.user, self.pw  = self.create_RDS()

    def create_ec2_sg(self):
        sec_group = ec2.SecurityGroup(
            self, "EC2SecurityGroup", vpc=self.vpc, allow_all_outbound=True
        )

        # Create Security Group Ingress Rule
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="allow SSH access from any ip address"
        )

        # Allow HTTPS (port 443) access
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS access from any ip address"
        )
        return sec_group

    def create_RDS_sg(self):
        sec_group = ec2.SecurityGroup(
            self,
            "RDSSecurityGroup",
            vpc=self.vpc,
            description="Allow access to RDS from EC2",
            allow_all_outbound=True,
        )

        # Allow the EC2 security group to access the RDS security group on port 5432 (PostgreSQL)
        sec_group.add_ingress_rule(
            self.ec2SecurityGroup, # only instances associated with this self.ec2SecurityGroup security group (the created EC2 instance in this case) can send traffic to the RDS instance associated with this RDS security group.
            ec2.Port.tcp(5432),
            "Allow access from EC2 to RDS on PostgreSQL port",
        )
        return sec_group

    def create_RDS(self):
        db_name= "Group9"
        user = "Group9" # define username
        pw = str(uuid.uuid4()) # generate password

        secret = secretsmanager.Secret(self, "Secret",
            secret_object_value={
                "username": SecretValue.unsafe_plain_text(user),
                "database": SecretValue.unsafe_plain_text(db_name),
                "password": SecretValue.unsafe_plain_text(pw)
            }
        )

        instance = rds.DatabaseInstance(
            self,
            "MyPostgresDB",
            database_name=db_name,  # Set the database name
            engine=rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_16_3),
            vpc=self.vpc,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE_WITH_EGRESS},  # put this RDS database instance into the private subnet of egress type in this vpc
            security_groups=[self.RDSSecurityGroup],
            multi_az=False,  # For simplicity, disable multi-az. This database will only exist in one availability zone
            allocated_storage=20,  # Storage size in GB
            max_allocated_storage=100,  # Maximum storage (auto-scaling)
            removal_policy=RemovalPolicy.DESTROY,  # Destroy DB on stack delete
            deletion_protection=False,  # Disable deletion protection (for dev purposes)
            publicly_accessible=False,  # DB is private and only accessible from inside VPC
            credentials=rds.Credentials.from_secret(secret),  # Use the Secrets Manager secret for password and user name
        )

        #CfnOutput(self, "Host", value=f"{instance.db_instance_endpoint_address}")
        #CfnOutput(self, "Database name", value=f"{db_name}")
        #CfnOutput(self, "Port", value=f"{instance.db_instance_endpoint_port}")
        #CfnOutput(self, "Username", value=f"{user}")
        #CfnOutput(self, "Password", value=f"{pw}")
        return instance.db_instance_endpoint_address, db_name, instance.db_instance_endpoint_port, user, pw

class EC2(Stack):
    def __init__(self, scope: Construct, construct_id: str, RDS, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # command to run automatically right after the ec2 instance is created. The commands will be ran in order. 
        self.ec2Command = [
                '#!/bin/bash',
                'sudo yum update -y',
                'sudo yum install -y aws-cli',
                'sudo yum install -y python3',
                'sudo yum install -y python3-pip',
                'sudo yum install -y amazon-ssm-agent',  # Ensure SSM Agent is installed. need to install SSM agent to enable connection to the ec2 instance when using session manager on aws website
                'sudo systemctl enable amazon-ssm-agent',  # Enable SSM Agent service
                'sudo systemctl start amazon-ssm-agent',   # Start SSM Agent
                'sudo yum install git -y',
                'cd ./home/ec2-user',
                f'git clone https://{os.getenv("USER")}:{os.getenv("TOKEN")}@github.com/wilnn/rate-my-courses-backend.git',
                f'echo "export DBNAME={RDS.dbName}" >> /home/ec2-user/.bashrc', # start adding environment variable permanently
                f'echo "export DBPASSWORD={RDS.pw}" >> /home/ec2-user/.bashrc',
                f'echo "export DBUSER={RDS.user}" >> /home/ec2-user/.bashrc',
                f'echo "export DBPORT={RDS.port}" >> /home/ec2-user/.bashrc',
                f'echo "export DBHOST={RDS.host}" >> /home/ec2-user/.bashrc', 
                'source /home/ec2-user/.bashrc',
                'cd ./rate-my-courses-backend/ratemycourses-backend',
                'pip3 install -r requirements.txt',
                'python3 app.py',
            ]
        
        self.RDS = RDS
        self.url = self.create_ec2()
    
    def create_ec2(self):
        '''# Create Key Pair
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/CfnKeyPair.html
        cfn_key_pair = ec2.CfnKeyPair(
            self,
            "MyCfnKeyPair",
            key_name="cdk-ec2-key-pair",
            tags=[CfnTag(key="key", value="value")],
        )'''

        # add IAM role to allow this ec2 instance to communicate with AWS system manager so that we can access it from aws session manager
        role = iam.Role(
            self,
            "EC2SSMRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
            ]
        )

        # Create EC2 instance
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/README.html
        # https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html
        instance = ec2.Instance(
            self,
            "Group9",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=self.RDS.vpc,
            vpc_subnets={"subnet_type": ec2.SubnetType.PUBLIC},  # put this ec2 instance into the public subnet in this vpc
            #vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=self.RDS.ec2SecurityGroup,
            associate_public_ip_address=True,  # Ensures the instance gets a public IP
            key_pair=ec2.KeyPair.from_key_pair_attributes(self, "KeyPair", key_pair_name="HN_key"), # replace key_pair_name with the name of your own keypair to ssh into the ec2 instance
            role=role,
        )

        # add command to run automatically once the instance is created.
        instance.add_user_data(*[command for command in self.ec2Command]) # add commands to user data to run right after the ec2 instance in created 

        # Output Instance public url
        #CfnOutput(self, "InstancePublicDNS", value=f"https://{instance.instance_public_dns_name}")
        return f"https://{instance.instance_public_dns_name}"
