SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 'SUBLIST', 'SUPERLIST', 'EQUAL', 'UNEQUAL'

def check_lists(first=None, second=None):
    first, second = '.'.join(map(str, first)), '.'.join(map(str, second))
    if first == second: return EQUAL
    elif first in second: return SUBLIST
    elif second in first: return SUPERLIST
    else: return UNEQUAL
