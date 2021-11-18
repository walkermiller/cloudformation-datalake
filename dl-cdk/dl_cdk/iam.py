from aws_cdk import (
    core as cdk,
    aws_iam as iam
)




class IAMStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        glue_service_role = iam.Role(self,
            id="glueServiceRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=iam.ManagedPolicy.from_managed_policy_arn(self,
                id="GlueServicePolicy",
                managed_policy_arn="arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole")
        )

    