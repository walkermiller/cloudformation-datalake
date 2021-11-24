from aws_cdk import (
    core as cdk,
    aws_glue as glue,
    aws_lakeformation as lakeformation,
    aws_s3 as s3,
    aws_iam as iam
)




class DlStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # database = glue.Database(self, 
        #     id="",
        #     database_name="")
    
        # source_table = glue.Table(self,
        #     id="SourceTable",
        #     database=database,
        #     bucket=
        # )

        lakeformation.