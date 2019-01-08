import re

def word_count(phrase):
    finds = re.findall(r"[a-z]+\'?[a-z]+|\d+", phrase.lower())
    return {word: finds.count(word)
            for word in set(finds)}