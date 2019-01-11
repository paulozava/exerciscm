def sum_of_multiples(limit, multiples):
    is_multiple = lambda x, y: x % y == 0 if y != 0 else False
    return sum(set(number
                for number in range(limit)
                for multiple in multiples
                if is_multiple(number, multiple)))
