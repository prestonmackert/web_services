"""
This is a small application that leverages text from the original bible to showcase Natural Language Processing

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import os
from bible_app import create_searchable_texts as text_parser
from aws_utility import translate_controller
from demi_bot import system_utility


# -------------------------------------------------------------------------------------------------------------------- #
# menu-based application
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
                english_text = translate_controller.translate_text(selected_verse)
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
    # loading in the new testament form text file and calling support to parse file
    new_testament_text = system_utility.load_text('/raw_text_files/newtestatment.txt')
    new_testament = text_parser.create_new_testament(new_testament_text)

    # todo: make quran searchable text and add to the application
    # quaran_text = system_utility.load_text('/raw_text_files/quran.txt')
    # quran_surahs = text_parser.create_quran(quaran_text)

    bible_app(new_testament)


# running the script
main()
