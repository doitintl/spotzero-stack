# SpotZero CDK Stack

This CDK example project will deploy a [SpotZero](https://github.com/doitintl/spotzero) service as a Fargate Scheduled Task.

The task is running once on 30 minutes and automatically updates all EC2 Auto Scaling groups in the deployed AWS region. maximizing Spot usage.
**SpotZero** creates/updates `MixedInstancePolicy` configuration for an EC2 Auto Scaling group, adding _similar_ EC2 instances with appropriate weights.

## Install

1. Install CDK: `npm install -g aws-cdk`
1. Clone this repository: `git clone https://github.com/doitintl/spotzero.git && cd spotzero`
1. Deploy CDK Stack: `cdk deploy`

This should work!

## Reference

- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html)