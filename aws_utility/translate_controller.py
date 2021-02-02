"""
This is a utility file for dealing with AWS' translation algorithm

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import boto3


# -------------------------------------------------------------------------------------------------------------------- #
# translation utility
# -------------------------------------------------------------------------------------------------------------------- #

def translate_text(the_text):
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    result = translate.translate_text(Text=the_text, SourceLanguageCode="el", TargetLanguageCode="en")
    return result.get('TranslatedText')