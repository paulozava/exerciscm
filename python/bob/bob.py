def hey(phrase=''):
    phrase = phrase.strip()
    if phrase.endswith('?'):
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase is '' or phrase.isspace():
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'