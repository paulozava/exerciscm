def verify(isbn):
    isbn_digits = [int(digit) for digit in isbn[:-1] if digit.isdigit()]
    isbn_check = isbn[-1]

    if not (isbn_check.isdigit() or isbn_check == 'X') or len(isbn_digits) != 9:
        return False

    isbn_check = int(isbn_check) if isbn_check.isdigit() else 10
    isbn_digits.append(isbn_check)
    isbn_sum = sum([digit * (10 - multiplier)
                    for multiplier, digit in enumerate(isbn_digits)])

    return isbn_sum % 11 == 0
