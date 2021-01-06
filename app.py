#!/usr/bin/env python3

from aws_cdk import core

from spotzero.spotzero_stack import SpotZeroStack


app = core.App()
SpotZeroStack(app, "SpotZero")

app.synth()
