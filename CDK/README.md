# CI/CD for RateMyCourses with AWS CDK

- The idea of using CDK is to create AWS resources using CloudFormation template.
- Inside the ```CDK/cdk/``` folder is the ```cdk_stack.py``` file which handles the creation of Amplify, EC2 and RDS. The app.py is used to call functions in ```cdk_stack.py``` to be executed, to create a Cloudformation template.
- The 2 scripts using to automate the process is ```deploy-app.sh``` and ```destroy-app.sh```



## Deploy the entire website to AWS using CDK:

### NOTE: 
- AWS CDK works by creating the templates from code and deploying the templates as stacks to AWS cloud formation to create AWS infrastructure. This means multiple AWS resources within the same stack and also in different stacks will be created at the same time. This will create a problem because sometimes you will need the credentials from an AWS resource in order to create/run another AWS resource properly, but the credentials of an AWS resource will not exist until that resource is successfully created. In our case, the back end in EC2 will need the credentials of the RDS database such as host, port, username, password, etc., and amplify needs the endpoint of the EC2 instance in order to send requests. One way to fix it is to add the credentials to the back end and front end manually once it finished deploying but there should be a better way to automate it.
- Solution: It can be solved by imposing dependency. This can be done by storing the credentials to the attributes inside a stack class and then referencing those attributes in other parts of your code. When AWS CDK sees this, it will know that the other part of your code depends on these credentials and will assign the correct credential information to that part of your CDK code. This can also be done by stack cross reference, which is passing an object that represents a stack to another stack (refer to app.py for example). Doing this will impose the dependency and CDK will know what stack it will have to create first.
 
### CDK deployment details:
AWS CDK will look at the code and create 3 different stacks in order:
#### The first stack:
The first stack will create a VPC that have 2 subnets, 1 private and 1 public subnet. Then, it create the security group for the EC2 instance which allows SSH, HTTP (HTTP access will be removed in the future for security reasons), and HTTPS requests. I will also create a security group for the RDS database which only allow any EC2 instance that attach to the previously created EC2 secuity group to access the RDS database that will attach to this RDS security group. Finally, it create the RDS database instance and add the database to the private subnet of the newly created VPC to ensure that no one can access it from the public internet.

#### The second stack:
The second stack will create an EC2 instance, attach the EC2 security group created earlier to this EC2 instance to make sure that it can access the RDS database. Then, run the commands in the user data to download dependencies, git clone the back end, download the Nginx web server to enable https access and reverse proxy which will forward the HTTPS request from the front end to the Flask server. Finally, run the Flask server and the Nginx web server.

#### The third stack:
The third stack will deploy the front end to AWS Amplify from the Github repo. 

### Before Deploying:
Create an .env file in the CDK directory and add the following environment variables:
TOKEN=<Your github personal access token>
USER=<Your Github user name>
AWSKEYPAIR=<your AWS key pair for SSH access>

Refer to: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic to know how to create the token

### Deploy:
```
chmod +x deploy-app.sh
./deploy-app.sh
```
### Destroy:
```
chmod +x destroy-app.sh
./destroy-app.sh
```
### Note:
If receive an error such as: 
```
-bash: "./deploy-app.sh: /bin/bash^M: bad interpreter: No such file or directory"
```
Then do:
```
sudo apt install dos2unix
dos2unix deploy-app.sh
```
The same problem can happen when running ```./destroy-app.sh```

### Debugging EC2 commands in user data:
If you believe that a command in user data do not work, then SSH into the ec2 instance and do ```sudo cat /var/log/ec2-init.log``` to look at the log information. There you will see the status of each command that was executed.




## Frontend (Amplify)

### Useful commands
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

First of all, you should use Linux Ubuntu instead of Bash, it's easier to use AWS CLI. Trust me.

### Automate (fully) frontend deployment with CDK (using Bash script)
- Step 1: Go to the ```cdk-deployment/``` folder, make the Bash script executable with ```chmod +x create-frontend.sh```
- Step 2: Create the Amplify frontend with ```./create-frontend.sh```
- Step 3: The only manual step (but it's not required, Amplify recommend us to do it). Migrate AWS Amplify to Github App via AWS Console (connect your Github account to Amplify to authorize the access to the repo). Right now it does not support migrating to the GitHub App integration via the CLI.
- Step 4: Delete the Amplify frontend (when done using) with ```cdk destroy```

## Automate (partially) frontend deployment with CDK (without using Bash script)
- Step 1: Install the AWS CDK CLI with ```npm install -g aws-cdk``` and double check with ```cdk --version```. If you're using Ubuntu and have errors when install, try ```sudo```, believe me it'll work.

- Step 2: Create the CDK project and choose the language Python with ```cdk init app --language python```

- Step 3: Go to that CDK project folder and install dependencies with ```python -m pip install -r requirements.txt``` and ```pip install aws-cdk.aws-amplify-alpha```

- Step 4: Understand the files:
    - ```cdk_app``` folder: this is where the stacks are defined(e.g., one stack for the frontend, another for the backend). Each stack is a Python file that defines specific resources for our infrastructure (like Amplify for the frontend and an EC2 for the backend).
    - ```app.py```: this file acts as the entry point for the CDK application

- Step 5: Update the information in files in ```cdk_app/```: for example the token name from AWS Secret Manager, the environment variable name, github username, github repo name, branch name to deploy,...
    - If don't have a token stored in AWS secret manager yet, can run the below CLI to create one
    ```
    aws secretsmanager create-secret \
    --name github-token-name \
    --secret-string "your-github-personal-access-token-aka-PAT"
    ```
    If it occurs errors, try to sync the time (Ubuntu case): ```sudo ntpdate -s ntp.ubuntu.com```
    Or using:
    ```
    sudo apt-get install ntpdate
    sudo ntpdate time.nist.gov
    ```

    And use this to make sure the token exists: ```aws secretsmanager describe-secret --secret-id github-token-name```

- Step 6: Run CDK with ```cdk synth``` will generate a CloudFormation template based on all the stacks defined in ```app.py``` file. These templates are output to the ```cdk.out``` director

- Step 7: Trigger the first build. When the Amplify stack is created and we completed migrating to Github App, no deployment will happen, simply because we haven't made any change to the branch yet, that's why we need to trigger the first build. Do the following steps:
```
aws amplify list-apps --query "apps[?name=='RateMyCourses'].appId | [0]
aws amplify start-job \
    --app-id "$AMPLIFY_APP_ID" \
    --branch-name "$AMPLIFY_BRANCH_NAME" \
    --job-type RELEASE
```
- Step 8: The only manual step (but it's not required, Amplify recommend us to do it). Migrate AWS Amplify to Github App via AWS Console (connect your Github account to Amplify to authorize the access to the repo). Right now it does not support migrating to the GitHub App integration via the CLI.

- Step 9: To delete the Amplify stack, do ```cdk destroy```
