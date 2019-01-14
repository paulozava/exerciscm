class Queen(object):
    def __init__(self, row, column):
        if row not in (1,2,3,4,5,6,7,8) or column not in (1,2,3,4,5,6,7,8):
            raise ValueError('Position not possible')
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        row_distance = another_queen.row - self.row
        column_distance = another_queen.column - self.column
        same_diagonal = row_distance == column_distance
        same_row = self.row == another_queen.row
        same_column = self.column == another_queen.column
        return same_row or same_column or same_diagonal
