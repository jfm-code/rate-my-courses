#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk_app.amplify_stack import AmplifyFrontendStack

app = cdk.App()

AmplifyFrontendStack(app, "AmplifyFrontendStack")

app.synth()
