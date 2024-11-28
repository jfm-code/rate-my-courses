from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    CfnOutput,
    aws_iam as iam,
    CfnTag,
)

from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # command to run automatically right after the ec2 instance is created. The command will be run in order. 
        self.ec2Command = [
            '#!/bin/bash',
            'sudo yum update -y',
            'sudo yum install -y aws-cli',
            'sudo yum install -y python3',
            'sudo yum install -y python3-pip',
            'sudo yum install -y amazon-ssm-agent',  # Ensure SSM Agent is installed. need to install SSM agent to enable connection to the ec2 instance when using session manager on aws website
            'sudo systemctl enable amazon-ssm-agent',  # Enable SSM Agent service
            'sudo systemctl start amazon-ssm-agent',   # Start SSM Agent
        ]

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

        
        url = self.create_ec2()

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

    def create_ec2(self):
        # Create Basic VPC
        vpc = self.vpc

        # add Security Group
        sec_group = self.ec2SecurityGroup

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
            vpc=vpc,
            security_group=sec_group,
            associate_public_ip_address=True,  # Ensures the instance gets a public IP
            key_pair=ec2.KeyPair.from_key_pair_attributes(self, "KeyPair", key_pair_name="HN_key"),
            vpc_subnets={"subnet_type": ec2.SubnetType.PUBLIC},  # add ec2 to the public subnet in the vpc
            role=role,
        )

        # add command to run automatically once the instance is created.
        instance.add_user_data(*[command for command in self.ec2Command]) # add commands to user data to run right after the ec2 instance in created 

        # Output Instance public url
        CfnOutput(self, "InstancePublicDNS", value=f"https://{instance.instance_public_dns_name}")
        return f"https://{instance.instance_public_dns_name}"



        