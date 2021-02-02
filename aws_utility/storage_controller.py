"""
This is a utility file for dealing with AWS' object storage.... 's3'

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import boto3
import os
import json


# -------------------------------------------------------------------------------------------------------------------- #
# json utility
# -------------------------------------------------------------------------------------------------------------------- #

def upload_json(bucket_name, file_path, file_name):
    """ uploads a given json structure into s3 storage """
    print("uploading json file to s3 storage...")
    s3 = boto3.client('s3')
    # s3.upload_file(file_path,bucket_name, '%s/%s' % (bucket_folder,dest_file_name))
    s3.upload_file(file_path, bucket_name, 'Git/amazon_web_services/raw_text_files/' + file_name)