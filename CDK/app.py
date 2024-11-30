#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import RDS, EC2


app = cdk.App()
rds= RDS(app, "Group9RDS")
ec2 = EC2(app, "Group9EC2", RDS=rds) # passing another into this stack allows stack cross reference. 

app.synth()
