## Executing

The Cloudformation is divided into seperate templates, which should be run in order. 

### Steps
1. Set Datalake name
   `export Datalake=lakename`
2. Create IAM roles
   `aws cloudformation create-stack --template-body file://templates/iam.yaml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=Datalake,ParameterValue=${Datalake} --stack-name ${Datalake}-iam`
3. Create the S3 buckets
   `aws cloudformation create-stack --template-body file://templates/s3.yaml --parameters ParameterKey=Datalake,ParameterValue=$Datalake --stack-name ${Datalake}-s3`
4. Copy scripts into s3 buckets
   `aws s3 cp scripts/* [scripts bucket]`
5. Create the Lake processing resources
   `aws cloudformation create-stack --template-body file://templates/datalake.yaml --parameters ParameterKey=Datalake,ParameterValue=$Datalake  --stack-name ${Datalake}-dl`