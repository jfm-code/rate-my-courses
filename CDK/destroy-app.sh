#!/bin/bash

set -e

echo "Deleting the web app..."
yes | cdk destroy --all --app "python3 app.py"
