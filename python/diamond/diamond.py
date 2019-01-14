from string import ascii_uppercase

def make_diamond(letter):
    letter = letter.upper()
    if letter not in ascii_uppercase:
        raise IOError('not a letter')
    letter_distance = ord(letter) + 1
    upper_diamond = [pattern_print(chr(i)) for i in range(65, letter_distance)]
    middle_diamond = upper_diamond.pop()
    middle_len = len(middle_diamond)
    upper_diamond = [line.center(middle_len) for line in upper_diamond]
    return '\n'.join(upper_diamond + [middle_diamond] + list(reversed(upper_diamond))) + '\n'


def pattern_print(letter):
    pattern = ascii_uppercase[::-1] + ascii_uppercase[1:]
    return ''.join([l if l == letter else ' ' for l in pattern]).strip()