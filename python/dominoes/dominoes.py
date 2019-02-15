import numpy as np

def chain(dominoes):
    dominoes = sorted(dominoes)
    black, white = dominoes[0]
    dominoes = dominoes[1:]
    chain_dom = [(black, white)]
    while dominoes:
        if white not in list(np.array(dominoes).flat):
            raise Exception('DOMINOOOOOOES')
        for domino in dominoes:
            if white in domino:
                dominoes.remove(domino)
                if domino.index(white) == 1:
                    domino = domino[::-1]
                chain_dom.append(domino)
                black, white = domino
                break
    return chain_dom