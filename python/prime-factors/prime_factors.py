def prime_factors(natural_number):
    response = []
    for divisor in range(2, natural_number + 1):
        while True:
            result, rest = divmod(natural_number, divisor)
            if rest == 0:
                natural_number = result
                response.append(divisor)
            else:
                break
        if natural_number == 1:
            break
    return response

# prime_factors(93819012551)
# prime_factors(12)