#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import RDSStack, EC2Stack, AmplifyStack


app = cdk.App()
rds= RDSStack(app, "RateMyCourses-RDS")
ec2 = EC2Stack(app, "RateMyCourses-EC2", RDS=rds) # passing another stack into this stack allows stack cross reference. (accessing credentials of an instance )
AmplifyStack(app, "RateMyCourses-Amplify", ec2=ec2)

app.synth()
