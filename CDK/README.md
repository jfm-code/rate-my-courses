# Before Deploying:
Create an .env file in the CDK directory and add the following environment variables:
TOKEN=<Your github personal access token>
USER=<Your Github user name>
AWSKEYPAIR=<your AWS key pair for SSH access>

Refer to: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic to know how to create the token

Creating backend repo:
1. Create a github repo name "rate-my-courses-backend"
2. Git clone that repo into your local machine.
3. Copy the entire "ratemycourses-backend" from the rate-my-courses repository into the cloned repo
4. Commit and push the folder


# Deploy:
chmod +x deploy-rate-my-courses.sh
./deploy-rate-my-courses.sh


# Destroy:
chmod +x destroy-rate-my-courses.sh
./destroy-rate-my-courses.sh

# NOTE:
If receive an error such as: -bash: "./deploy-rate-my-courses.sh: /bin/bash^M: bad interpreter: No such file or directory"
Then do:
sudo apt install dos2unix
dos2unix deploy-rate-my-courses.sh
The same problem can happen when running ./destroy-rate-my-courses.sh