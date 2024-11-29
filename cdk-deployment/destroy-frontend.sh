#!/bin/bash

set -e

echo "Deleting Amplify stack..."
yes | cdk destroy
