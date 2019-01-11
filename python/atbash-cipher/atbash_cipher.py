def encode(plain_text):
    plain_text = ''.join([character for character in plain_text.lower() if character.isalnum()])
    map_cipher = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    ciphered_text = plain_text.translate(map_cipher)
    return ' '.join([ciphered_text[i-5:i] for i in range(5, len(ciphered_text) + 4, 5)])


def decode(ciphered_text):
    map_cipher = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    ciphered_text = ciphered_text.replace(' ', '')
    return ciphered_text.translate(map_cipher)
