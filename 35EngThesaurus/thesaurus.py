import json
import difflib
from mysql_vocabulary import MySQLVocabulary
from json_vocabulary import JSONVocabulary





def get_uni_description(word, vocabulary):
    word = word.lower()
    words = vocabulary.get_words()
    if not word in words:
        if word.capitalize() in words:
            word = word.capitalize()
        elif word.upper() in words:
            word = word.upper()
    if word in words:
        definition = vocabulary.get_definitions(word)
        if len(definition) == 1:
            return definition[0]
        else:
            # form listed output
            output = f'Possible meanings for {word}:\n'
            number = 1
            # print(definition)
            # print("word:" + str(definition))
            for match in definition:
                output = output + str(number) + ": " + match + "\n"
                number += 1
            return output
    else:
        limit_ratio = 0.75
        close_matches = difflib.get_close_matches(word, words, cutoff=limit_ratio)
        output = f'Could not find word: {word} , did you mean:\n'
        number = 1
        for match in close_matches:
            output = output + str(number) + ": " + match + "\n"
            number += 1
        if len(close_matches) == 0:
            output = f"Could not find similar words tot '{word}', please check your grammar"
        return output

def get_description(word):
    # return get_uni_description(word, JSONVocabulary())
    return get_uni_description(word, MySQLVocabulary())