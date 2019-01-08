from string import punctuation as punctuations



def pradronization(words):
    no_space, single_space, double_space = '', ' ', '  '
    words = words.replace('-', single_space)
    for punctuation in punctuations:
        words = words.replace(punctuation, no_space)
    while double_space in words:
        words = words.replace(double_space, single_space)
    words = words.upper()
    return words


def abbreviate(words):
    words = pradronization(words)
    return ''.join([word[0] for word in words.split(' ')])
