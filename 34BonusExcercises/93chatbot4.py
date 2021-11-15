import datetime
import difflib


vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

from datetime import datetime
def foo(query, vocabulary):
    if query in vocabulary.keys():
        return vocabulary[query]
    else:
        return vocabulary[sorted(vocabulary, key=lambda x: difflib.SequenceMatcher(None, x, query).ratio())[-1]]


print(foo('tell me the time', vocabulary))