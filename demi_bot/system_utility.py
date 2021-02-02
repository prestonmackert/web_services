"""
Creating core functions that leverage the operating system to make life easier and more automated :)

@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# imports
# -------------------------------------------------------------------------------------------------------------------- #

import os


# -------------------------------------------------------------------------------------------------------------------- #
# json utility
# -------------------------------------------------------------------------------------------------------------------- #

def load_text(file_path):
    """ takes in a file path for a text file and returns a simple list of each line """
    path = os.getcwd() + file_path
    text = open(path, "r")
    lines = text.readlines()
    return lines