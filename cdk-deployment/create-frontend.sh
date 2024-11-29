#!/bin/bash

set -e

GITHUB_TOKEN_NAME="jfm-PAT-token"
GITHUB_PERSONAL_ACCESS_TOKEN="thisisjustaplaceholder"
AMPLIFY_APP_NAME="RateMyCourses"
GITHUB_BRANCH_NAME="dev-mi"

echo "Installing AWS CDK CLI..."
sudo npm install -g aws-cdk
cdk --version

echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt
pip install aws-cdk.aws-amplify-alpha

echo "Creating GitHub token in AWS Secrets Manager if there isn't one already..."
SECRET_EXISTS=$(aws secretsmanager describe-secret --secret-id "$GITHUB_TOKEN_NAME" --query "Name" --output text 2>/dev/null || echo "NOT_FOUND")
if [ "$SECRET_EXISTS" == "NOT_FOUND" ]; then
    echo "GitHub token not found. Creating a new secret..."
    aws secretsmanager create-secret \
        --name "$GITHUB_TOKEN_NAME" \
        --secret-string "$GITHUB_PERSONAL_ACCESS_TOKEN"
    echo "GitHub token created successfully."
else
    echo "GitHub token already exists: $SECRET_EXISTS"
fi

echo "Synthesize CDK to create CloudFormation template..."
cdk synth

echo "Deploying the Amplify stack..."
cdk deploy --require-approval never

echo "Triggering the first Amplify build..."
AMPLIFY_APP_ID=$(aws amplify list-apps --query "apps[?name=='$AMPLIFY_APP_NAME'].appId | [0]" --output text)
aws amplify start-job \
    --app-id "$AMPLIFY_APP_ID" \
    --branch-name "$GITHUB_BRANCH_NAME" \
    --job-type RELEASE

echo "Remember to migrate AWS Amplify to GitHub App integration via the AWS Console (we can't do this via CLI)."