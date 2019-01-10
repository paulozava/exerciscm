def to_rna(dna_strand):
    dna_to_rna = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([dna_to_rna[base] for base in dna_strand])
