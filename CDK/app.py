#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import RDSStack, EC2Stack, AmplifyFrontendStack


app = cdk.App()
rds= RDSStack(app, "Group9RDS")
ec2 = EC2Stack(app, "Group9EC2", RDS=rds) # passing another stack into this stack allows stack cross reference. (accessing credentials of an instance )
AmplifyFrontendStack(app, "AmplifyFrontendStack", ec2=ec2)

app.synth()
