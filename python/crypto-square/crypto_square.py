def encode(plain_text):
    normalized_text = [letter.lower()
                       for letter in plain_text
                       if letter.isalnum()]
    normalized_len = len(normalized_text)
    height, width = closest_retangle_paramethers(normalized_len)
    spaces_to_add = (height * width) - normalized_len
    normalized_text.extend([' '] * spaces_to_add)
    words_list = [normalized_text[i - height:i]
                  for i in range(height, height * width + 1, height)]
    encrypted = ' '.join(map(''.join, zip(*words_list))).strip()
    return encrypted

def closest_retangle_paramethers(lenght, range_to_seek=10):
    for i in range(range_to_seek):
        found = balanced_diplets(lenght + i)
        if found:
            return found
    else:
        return lenght, 1

def balanced_diplets(length):
    for divisor in range(length - 1, 1, -1):
        operator, rest = divmod(length, divisor)
        if rest == 0 and divisor >= operator and divisor - operator <= 1:
            return divisor, operator
    else:
        return False