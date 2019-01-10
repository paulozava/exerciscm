from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers

def rotate(text, key):
    cypher_lowers = lowers[key:] + lowers[:key]
    cypher_uppers = uppers[key:] + uppers[:key]
    return text.translate(str.maketrans(lowers, cypher_lowers))\
               .translate(str.maketrans(uppers, cypher_uppers))
