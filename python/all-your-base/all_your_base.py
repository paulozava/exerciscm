def rebase(input_base, digits, output_base):
    is_rebaseble(input_base, digits, output_base)
    positions = len(digits) - 1
    in_ten_base = sum([digit * (input_base ** (positions - index))
                       for index, digit in enumerate(digits)])
    rebased = []
    while in_ten_base > 0:
        in_ten_base, rest = divmod(in_ten_base, output_base)
        rebased.append(rest)
    rebased.reverse()
    return rebased

def is_rebaseble(input_base, digits, output_base):
    if input_base < 2 or output_base < 2 \
       or any(map(lambda x: x<0 or x>input_base-1, digits[1:])):
        raise ValueError('Impossible to rebase')
