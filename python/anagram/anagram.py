from itertools import permutations

def find_anagrams(word, candidates):
    word_permutations = set(permutations(word.lower()))
    return [candidate
           for candidate in candidates
           if candidate.lower() != word.lower() and tuple(candidate.lower()) in word_permutations]