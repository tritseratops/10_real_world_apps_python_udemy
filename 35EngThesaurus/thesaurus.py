import json
import difflib

def get_description(word):
    word = word.lower()
    f = open('data\\data.json')
    vocabulary = json.load(f)
    words = vocabulary.keys()
    if not word in words:
        if word.capitalize() in words:
            word = word.capitalize()
        elif word.upper() in words:
            word = word.upper()
    if word in words:
        if len(vocabulary[word])==1:
            return vocabulary[word][0]
        else:
            # form listed output
            output = f'Possible meanings for {word}:\n'
            number = 1
            print(vocabulary[word])
            print("word:" + str(vocabulary[word][0]))

            for match in vocabulary[word]:
                output = output + str(number) + ": " + match + "\n"
                number += 1
            return output
    else:
        limit_ratio = 0.75
        close_matches = difflib.get_close_matches(word,vocabulary, cutoff=limit_ratio)
        output = f'Could not find word: {word} , did you mean:\n'
        number = 1
        for match in close_matches:
            output=output+str(number)+": "+match+"\n"
            number+=1
        if len(close_matches)==0:
            output = f"Could not find similar words tot '{word}', please check your grammar"
        return output
