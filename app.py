#!/usr/bin/env python3

from aws_cdk import core

from spotzero.spotzero_stack import SpotzeroStack


app = core.App()
SpotzeroStack(app, "spotzero")

app.synth()
