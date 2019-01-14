TOKENS = {'         || ': '1', '  | ___  |  ': '2', '    ___  || ': '3',
          ' |   _   || ': '4', ' |  ___   | ': '5', ' || ___   | ': '6',
          '    _    || ': '7', ' || ___  || ': '8', ' |  ___  || ': '9',
          ' || _ _  || ': '0'}


def convert(input_grid):
    digits_in = int(len(max(input_grid)) / 3)
    iter_input = zip(*input_grid)
    digits = ''
    for _1 in range(digits_in):
        token = ''
        for _2 in range(3):
            token += ''.join(next(iter_input))
        if token in TOKENS.keys():
            digit = TOKENS[token]
        else:
            digit = '?'
        digits += digit
    return digits
