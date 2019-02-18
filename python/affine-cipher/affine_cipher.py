def encode(plain_text, a, b):
    # E(x) = (ax + b) mod m
    e = lambda letter, a, b: chr(97 + (a*(ord(letter)-97) + b) % 26)
    return ''.join([e(letter, a, b) for letter in plain_text.lower() if letter.isalpha()])


def decode(ciphered_text, a, b):
    # D(y) = a ^ -1(y - b) mod m
    d = lambda y, a, b: chr(97 + int(((ord(y) - 97 - b)/a) % 26))
    pass
