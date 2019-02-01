from itertools import permutations

def solve(puzzle):
    '''
    brute force
    very slow at 5 different letters or more
    :param puzzle: a string
    :return: a dictionary with letters and values
    '''
    unique_letters = ''.join(set(letter
                                for letter in puzzle
                                if letter.isalpha()))
    for solution_candidate in permutations(map(str, range(10)), r=len(unique_letters)):
        to_translate = str.maketrans(unique_letters, ''.join(solution_candidate))
        to_eval = puzzle.translate(to_translate)
        try:
            if eval(to_eval):
                return {letter:int(value) for letter, value in zip(unique_letters, solution_candidate)}
        except:
            continue
    return {}