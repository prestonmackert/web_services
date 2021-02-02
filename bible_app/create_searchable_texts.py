"""
@author Preston Mackert
"""

# -------------------------------------------------------------------------------------------------------------------- #
# support functions to convert plain text into searchable data structures
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


def create_quran(text):
    """ converts the plain text file of an english translation of the quran """
    surahs = []

    # more uniqueness
    for line in text:
        # the text from the line is converted into a list
        data_structure = line.split()

        # will structure the quran into appropriate chunks, like we did with the new testament
        try:
            # the plain text file is split up so that each new surah is defined in the first word
            if data_structure[0] == 'SURA':
                surah_number = data_structure[1].replace('.', '')
                arabic_name = data_structure[2]
                english_name = ''.join(data_structure[3:]).replace('(', '')
                english_name = english_name.replace(')', '')

                surahs.append([surah_number, arabic_name, english_name])

        except IndexError:
            continue

    # i'm tapping with this basic data structure, quran is difficult man...
    return surahs