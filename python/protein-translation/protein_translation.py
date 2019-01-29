def proteins(strand):
    triplet_to_protein = {'AUG':'Methionine','UUU':'Phenylalanine', 'UUC':'Phenylalanine', 'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine','UAU':'Tyrosine', 'UAC':'Tyrosine', 'UGU':'Cysteine', 'UGC':'Cysteine','UGG':'Tryptophan', 'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}
    translation = [triplet_to_protein[strand[index:index+3]] for index in range(0, len(strand), 3)]
    if 'STOP' in translation:
        translation = translation[:translation.index('STOP')]
    return translation

