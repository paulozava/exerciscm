from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers

def rotate(text, key):
    cipher_lowers = lowers[key:] + lowers[:key]
    cipher_uppers = uppers[key:] + uppers[:key]
    return text.translate(str.maketrans(lowers, cipher_lowers))\
               .translate(str.maketrans(uppers, cipher_uppers))
