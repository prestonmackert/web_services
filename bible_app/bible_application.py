"""
This is a small application that leverages text from the original bible to showcase Natural Language Processing

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import boto3
import os
import json
from aws_utility import storage_controller as s3_util
from aws_utility import translate_controller as translator
from demi_bot import system_utility


# -------------------------------------------------------------------------------------------------------------------- #
# support functions for creating a searchable new testament
# -------------------------------------------------------------------------------------------------------------------- #

def create_new_testament(text):
    """ converts the plain text file of the greek new testament to a dictionary """
    new_testament = {}

    # this is unique to our file, but the concepts are transferable
    for line in text:
        data_structure = line.split('|')
        book = data_structure[0]
        chapter = data_structure[1]
        verse = data_structure[2]
        verse_text = data_structure[3].rstrip()

        """ creating our data structure so that the greek new testament is searchable, for example, here is how to 
        access revelation chapter 21 verse 3 text: new_testament['Rev']['21'][2][1] """
        if book in list(new_testament.keys()):
            if chapter in list(new_testament[book].keys()):
                new_testament[book][chapter].append((verse, verse_text))
            else:
                new_testament[book][chapter] = [(verse, verse_text)]
        else:
            new_testament[book] = {chapter: [(verse, verse_text)]}

    # return a dictionary of the new testament
    return new_testament


# -------------------------------------------------------------------------------------------------------------------- #
# bible support functions
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
# support functions for creating a searchable new testament
# -------------------------------------------------------------------------------------------------------------------- #

def bible_app(new_testament):
    """ simple user input application that will allow us to look at search and some amazon services """
    print("\nWelcome! This is a simple menu driven application that does some nifty things, select an option to "
          "play around with the different components :)")
    # setting up the app
    book_options = list(new_testament.keys())
    translation_app_active = True
    while translation_app_active:
        print("\n1) print out the books of the bible\n"
              "2) search for a bible verse\n"
              "3) exit the app")

        user_selection = input("\nselect an option\n>> ")

        if user_selection == '1':
            print(book_options)
            input("press any key to continue...")

        elif user_selection == '2':
            book_selection = input("\nselect a book (first 3 letters): ")
            chapter_selection = input("select the chapter: ")
            verse_selection = input("select the verse: ")

            try:
                selected_verse = new_testament[book_selection][chapter_selection][int(verse_selection)-1][1]
                print(book_selection, chapter_selection + ":" + verse_selection + " -", selected_verse)
                print("translating original greek text...")
                english_text = translator.translate_text(selected_verse)
                print(english_text)
                input("press any key to continue...")

            except (IndexError, KeyError):
                print("invalid search...")
                input("press any key to continue...")

        elif user_selection == '3':
            print("goodbye!")
            os._exit(0)

        else:
            print("enter a valid option :(")


# -------------------------------------------------------------------------------------------------------------------- #
# main
# -------------------------------------------------------------------------------------------------------------------- #

def main():
    text = system_utility.load_text('/raw_text_files/newtestatment.txt')
    new_testament = create_new_testament(text)
    # english_new_testament = translate_new_testament(new_testament)
    bible_app(new_testament)



# running the script
main()
