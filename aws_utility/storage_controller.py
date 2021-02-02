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
# json utility methods
# -------------------------------------------------------------------------------------------------------------------- #

def list_bucket_options():
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



# -------------------------------------------------------------------------------------------------------------------- #
# json utility
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    list_bucket_options()


# run script
main()
