
# RateMyCourses Website

## Overview

- This project is a web-based application for reviewing and rating courses, similar to RateMyProfessors. It uses **Vue.js** for the frontend, **Flask** for the backend, and **PostgreSQL** for the database. 
- The application is hosted on **AWS** with a CI/CD pipeline for automated build and deployment, using AWS services like **EC2**, **S3**, **RDS**, **CloudFormation**, and **CodePipeline**.

## Project Setup
Go to each folder (frontend or backend and see the readme file for more info)

## Integrate with AWS
- Initially, host frontend in Amplify and backend in EC2, and use local database first
- Then, transit to S3 bucket + CloudFront for frontend if we need more control
- Then, use RDS database to replace PostgreSQL local database
- In the future, we'll host both frontend and backend on 1 virtual machine, with the help of web server nginx

## Automate frontend deployment with CDK
First of all, you should use Linux Ubuntu instead of Bash, it's easier to use AWS CLI. Trust me.

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

    And use this to get the token: ```aws secretsmanager describe-secret --secret-id github-token-name```

- Step 6: Run CDK with ```cdk synth``` will generate a CloudFormation template based on all the stacks defined in ```app.py``` file. These templates are output to the ```cdk.out``` director

- Step 7: The only manual step. Migrate AWS Amplify to Github App via AWS Console (connect your Github account to Amplify to authorize the access to the repo). Right now it does not support migrating to the GitHub App integration via the CLI.

- Step 8: To delete the Amplify stack, do ```cdk destroy```

## Notes
- When the Amplify stack is created and we completed migrating to Github App, no deployment will happen, simply because we haven't made any change to the branch yet.