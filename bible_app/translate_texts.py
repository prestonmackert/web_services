"""
@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import json
from aws_utility import storage_controller as s3_util
from aws_utility import translate_controller as translator
from demi_bot import system_utility
from bible_app import create_searchable_texts as text_parser


# -------------------------------------------------------------------------------------------------------------------- #
# translation support functions
# -------------------------------------------------------------------------------------------------------------------- #

def translate_new_testament(new_testament):
    """ saves a list of tuples, where each tuple = 1 chapter """
    print("translating the greek bible into english using AWS...")
    full_text = []
    for book in new_testament:
        book_text = ''
        for chapter in new_testament[book]:
            chapter_text = ''
            for verse in new_testament[book][chapter]:
                chapter_text += verse[1] + " "
            book_text += chapter_text + " "
        full_text.append((book, book_text))


    """ we're going to write the full text into a text file to demonstrate how we measure expense from AWS :/ """
    with open('raw_text_files/newtestatment_text_to_translate.txt', 'w') as text_file:
        for book in full_text:
            text_file.write(book[0] + ":\n" + book[1] + "\n\n")

    """ now we're going to chop down the text into consumable chunks for the AWS 'translate' service, ain't free :/ """
    full_english_text = {}
    for book in full_text:
        # send the first 100 characters of each book into the aws translation engine
        consumable_chunk = book[1][:100]
        english_text = translator.translate_text(consumable_chunk)
        full_english_text[book[0]] = english_text

    partial_english_json = json.dumps(full_english_text, indent=4)
    with open('json_files/partial_english_translation.json', 'w') as json_file:
        json_file.write(partial_english_json)

    s3_util.upload_json("comprehend-examples", 'json_files/partial_english_translation.json', "english_new_testament.json")


# -------------------------------------------------------------------------------------------------------------------- #
# main function
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    # loading in the new testament form text file and calling support to parse file
    new_testament_text = system_utility.load_text('/raw_text_files/newtestatment.txt')
    new_testament = text_parser.create_new_testament(new_testament_text)
    # todo: figure out the AWS utility
    translate_new_testament(new_testament)