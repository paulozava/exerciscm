def is_armstrong(number):
    number_str = str(number)
    digits = len(number_str)
    armstrong_candidate = sum([int(digit) ** digits for digit in number_str])
    return armstrong_candidate == number