def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Different lenght of strands')
    hamming = [a.__eq__(b)
            for a, b in zip(strand_a, strand_b)]
    return hamming.count(False)