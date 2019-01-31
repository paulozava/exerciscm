import numpy as np

class WordSearch(object):
    def __init__(self, puzzle):
        self.__horizontal = puzzle
        self.__vertical = None
        self.__diagonal_topdown = None
        self.__diagonal_bottonup = None

    def search(self, word):
        # horizontal
        if self.__is_inside__(word, self.__horizontal):
            return True

        # vertical
        if not self.__vertical:
            self.__vertical = list(map(''.join, zip(*self.__horizontal)))
        if self.__is_inside__(word, self.__vertical):
            return True

        # diagonal top down
        rows_in_puzzle = len(self.__horizontal)
        matrix = np.array(list(map(list, self.__horizontal)))
        if not self.__diagonal_topdown:
            self.__diagonal_topdown = [''.join(matrix.diagonal(i))
                                       for i in range(1-rows_in_puzzle, rows_in_puzzle)]
        if self.__is_inside__(word, self.__diagonal_topdown):
            return True

        # diagonal bottom up
        matrix = matrix[::-1, :]
        if not self.__diagonal_bottonup:
            self.__diagonal_bottonup = [''.join(matrix.diagonal(i))
                                        for i in range(1-rows_in_puzzle, rows_in_puzzle)]
        if self.__is_inside__(word, self.__diagonal_bottonup):
            return True

        return False

    def __is_inside__(self, word, to_seek):
        for line in to_seek:
            if word in line or word[::-1] in line:
                return True
        return False