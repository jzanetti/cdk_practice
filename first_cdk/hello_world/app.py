#!/usr/bin/env python3
import aws_cdk as cdk
from hello_world.hello_world_stack import HelloWorldStack

app = cdk.App()

tags = {
    'Owner': 'Sijin',
    'Project': 'first_cdk',
    'CostCentre': 'Personal',
    'Status': 'research',
}

HelloWorldStack(
    app,
    "HelloWorldStack",
    tags=tags
)

app.synth()
