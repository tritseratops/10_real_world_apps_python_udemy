import json

class JSONVocabulary():
    def __init__(self):
        f = open('data\\data.json')
        self.vocabulary = json.load(f)
    def get_words(self):
        return self.vocabulary.keys()
    def get_definitions(self, word):
        return self.vocabulary[word]


print(JSONVocabulary().get_definitions('rain'))