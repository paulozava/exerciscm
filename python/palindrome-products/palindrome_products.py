def largest_palindrome(min_factor, max_factor):
    if not min_factor < max_factor:
        raise ValueError('min-factor must be major than max-factor')
    palindromes = find_palindrome(min_factor, max_factor)
    max_mult = max(palindromes.values())
    return set([key
                for key, mult in palindromes.items()
                if mult == max_mult and key[0] <= key[1]])

def smallest_palindrome(min_factor, max_factor):
    if not min_factor < max_factor:
        raise ValueError('min-factor must be major than max-factor')
    palindromes = find_palindrome(min_factor, max_factor)
    min_mult = min(palindromes.values())
    return set([key
                for key, mult in palindromes.items()
                if mult == min_mult and key[0] <= key[1]])

def find_palindrome(min_factor, max_factor):
    return {(mult1, mult2) : (mult1 * mult2)
            for mult1 in range(min_factor, max_factor +1)
            for mult2 in range(min_factor, max_factor +1)
            if str(mult1 * mult2) == str(mult1 * mult2)[::-1]}
