def classify(number):
    if number < 1:
        raise ValueError('Number needs to be a Natural one')
    factors_sum = sum([factor
                       for factor in range(1, int(number/2) + 1)
                       if number % factor == 0])
    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    else:
        return "deficient"