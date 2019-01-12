def nth_prime(number):
    if number < 1:
        raise ValueError('Non')
    primes, test_number = [2], 3
    while len(primes) < number:
        found = True
        for prime in primes:
            if test_number % prime == 0:
                found = False
                break
        if found:
            primes.append(test_number)
        test_number += 2
    return primes[number - 1]