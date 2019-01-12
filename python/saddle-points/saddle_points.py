##unfinished


def saddle_points(matrix):
    if not matrix:
        return set([])
    rows, columns = len(matrix), len(max(matrix))
    row_check = [element == max(elements)
                 for elements in matrix
                 for element in elements]

    col_check = [element == min(elements)
                 for elements in zip(*matrix)
                 for element in elements]

    return set([(pos // rows, pos % columns)
            for pos in range(rows * columns)
            if row_check[pos] and col_check[((rows * pos) % (rows * columns)) + pos//columns]])