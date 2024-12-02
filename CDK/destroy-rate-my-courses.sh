#!/bin/bash

set -e

echo "Deleting Amplify stack..."
yes | cdk destroy --all --app "python3 app.py"
