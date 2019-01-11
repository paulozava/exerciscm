def sieve(limit):
    sieve_list = set([2])
    if 0 < limit <= 2:
        return list(sieve_list)
    else:
        for number in range(3, limit + 1, 2):
            for prime in sieve_list:
                if number % prime == 0:
                    break
            else:
                sieve_list.add(number)
    return sorted(sieve_list)