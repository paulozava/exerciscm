from itertools import combinations_with_replacement as cwr

def find_minimum_coins(change, coins):
    if change < 1:
        raise ValueError('Impossible to change imaginary money')
    cycles = 1 + (change // min(coins))
    for i in range(1, cycles):
        for found in filter(lambda x: sum(x) == change, cwr(coins, i)):
            return sorted(found)
    raise ValueError('Sorry, we cant change your money today')