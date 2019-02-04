from random import randint

def private_key(p):
    return randint(2, p-1)

def public_key(p, g, private):
    return g**private % p

def secret(p, public, private):
    return public**private % p


# def is_prime(number):
#     if number > 2:
#         if number % 2 == 0: return False
#         primes = [i for i in range(3, number+1, 2)
#                   if number % i == 0]
#         return len(primes) == 1
#     elif number == 2: return True
#     else: return False

# def private_key(p):
#     prime_found = False
#     while not prime_found:
#         prime_candidate = randint(2,p-1)
#         prime_found = is_prime(prime_candidate)
#     return prime_candidate