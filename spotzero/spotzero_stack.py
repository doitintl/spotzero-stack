from aws_cdk import core, aws_ecs as ecs, aws_ecs_patterns as ecs_patterns, aws_ec2 as ec2, \
    aws_iam as iam, aws_applicationautoscaling as autoscaling, aws_logs as logs


class SpotZeroStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create VPC
        vpc = ec2.Vpc(self, "Vpc")

        # create ECS cluster
        cluster = ecs.Cluster(self, 'FargateCluster', vpc=vpc)

        # define Task IAM role
        role = iam.Role(self, "ContainerRole",
                        assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"))
        role.add_to_policy(
            iam.PolicyStatement(
                actions=["autoscaling:DescribeTags",
                         "autoscaling:DescribeAutoScalingGroups",
                         "autoscaling:UpdateAutoScalingGroup",
                         "ec2:DescribeLaunchTemplateVersions",
                         "autoscaling:CreateOrUpdateTags"],
                resources=["*"])
        )

        # define ECS Fargate task
        task_definition = ecs.FargateTaskDefinition(self, "TaskDefinition",
                                                    cpu=256, memory_limit_mib=512, task_role=role)
        task_definition.add_container(
            "Container", image=ecs.ContainerImage.from_registry("doitintl/spotzero"),
            command=["update", "--mfl=1"],
            logging=ecs.AwsLogDriver(stream_prefix="SpotZero",
                                     log_retention=logs.RetentionDays.THREE_DAYS,
                                     datetime_format="%Y/%m/%d %H:%M:%S")
        )
        task_definition_options = ecs_patterns.ScheduledFargateTaskDefinitionOptions(
            task_definition=task_definition
        )

        # create ECS Fargate scheduled task
        ecs_patterns.ScheduledFargateTask(self, "Task",
                                          scheduled_fargate_task_definition_options=task_definition_options,
                                          cluster=cluster,
                                          schedule=autoscaling.Schedule.expression("rate(30 minutes)"))
