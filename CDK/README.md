# Before Deploying:
Create an .env file in the CDK directory and add the following environment variables:
TOKEN=<Your github personal access token>
USER=<Your Github user name>

Refer to: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic to know how to create the token


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