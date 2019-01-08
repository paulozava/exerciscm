class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.__string_to_matrix(matrix_string)

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [row[index] for row in self.matrix]

    def __string_to_matrix(self, string):
        return [list(map(int, line.split(' ')))
                for line in string.split('\n')]