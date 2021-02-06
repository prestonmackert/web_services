"""
This is a utility file for dealing with AWS' object storage.... 's3'

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import logging
import boto3
from botocore.exceptions import ClientError


# -------------------------------------------------------------------------------------------------------------------- #
# json utility methods
# -------------------------------------------------------------------------------------------------------------------- #

def print_bucket_options():
    """ uploads a given json structure into s3 storage """
    s3 = boto3.client('s3')

    # cleaning up meta-data
    s3_buckets = s3.list_buckets()

    # parsing the response from amazon, thanks dad
    meta_data = s3_buckets['ResponseMetadata']
    buckets = s3_buckets['Buckets']
    owner = s3_buckets['Owner']

    # Kobe
    for bucket in buckets:
        print(bucket)


def upload_object(file_name, bucket_name, object_name):
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')

    try:
        response = s3.upload_file(file_name, bucket_name, object_name)

    except ClientError as e:
        logging.error(e)
        return False

    return True



# -------------------------------------------------------------------------------------------------------------------- #
# json utility
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    print_bucket_options()
    upload_object('/raw_text_files/newtestatment.txt', 'comprehend-examples')


# run script
main()
