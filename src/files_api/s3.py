import boto3
try:
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.type_defs import (PutObjectOutputTypeDef, MetadataEntryTypeDef)
except ImportError:
    print("boto3-stubs[s3] is not installed")

BUCKET_NAME="cloud-course-bucket-arun"

session=boto3.Session(profile_name="cloud-course")
s3_client: "S3Client" = session.client("s3")

#write a file to the S3 bucket with the content "Hello World"
response:PutObjectOutputTypeDef =s3_client.put_object(Bucket=BUCKET_NAME,
                    Key="folder/hello.txt",
                    Body="Hello, World!",
                    ContentType="text/plain")

metadata=response["ResponseMetadata"]
