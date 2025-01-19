from urllib import response
from more_itertools import bucket
from files_api.s3 import delete_objects
from files_api.s3.write_objects import upload_s3_object
import boto3
from moto import mock_aws
import os
from tests.consts import TEST_BUCKET_NAME

# TEST_BUCKET_NAME = "test-bucket-mlops-club-arun"

def test__upload_s3_object(mocked_aws):

    # upload a file to the bucket with correct content type
    object_key="test.txt"
    file_content:bytes=b"Hello World"
    content_type="text/plain"

    upload_s3_object(bucket_name=TEST_BUCKET_NAME,
                     object_key=object_key,
                     file_content=file_content,
                     content_type=content_type)

# check that file was uploaded with correct content type
    s3_client=boto3.client("s3")
    response=s3_client.get_object(Bucket=TEST_BUCKET_NAME,Key=object_key)
    assert response["ContentType"] == content_type
    assert response["Body"].read() == file_content 
