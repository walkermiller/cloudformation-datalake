from aws_cdk import (
    core as cdk,
    aws_glue as glue,
    aws_lakeformation as lakeformation,
    aws_s3 as s3,
    aws_iam as iam,
    aws_kms as kms
)


class S3Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        databaseName = cdk.CfnParameter(self,
            id="databaseName",
            type="String")
        
        kmsKey = kms.Key.from_lookup(id="kmsKey", alias_name="")

        script_bucket = s3.Bucket(self,
            id="scriptBucket",
            bucket_name="",
            block_public_access=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            bucket_key_enabled=True)

        raw_bucket = s3.Bucket(self, 
            id="rawbucket", 
            bucket_name="raw_bucket",  #!Sub arn:aws:glue:${AWS::Region}:${AWS::AccountId}:workflow/${EventDrivenWorkflow}
            encryption=s3.BucketEncryption.KMS_MANAGED,
            encryption_key=kmsKey,
            bucket_key_enabled=True,
            block_public_access=True)

        transformed_bucket = s3.Bucket(self, 
            id="transformedBucket",
            bucket_name="",
            encryption=s3.BucketEncryption.KMS_MANAGED,
            encryption_key=kmsKey,
            bucket_key_enabled=True,
            block_public_access=True)
    