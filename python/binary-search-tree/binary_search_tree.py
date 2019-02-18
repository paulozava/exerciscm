from itertools import cycle

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.last_add = cycle(['left', 'left', 'right', 'right'])

    def add(self, number):
        if self.left == None:
            self.left = number
        elif self.right == None:
            self.right = number
        elif isinstance(self.left, int):
            self.left = TreeNode(self.left, number)
        elif isinstance(self.right, int):
            self.right = TreeNode(self.right, number)
        else:
            if next(self.last_add) == 'left':
                self.left.add(number)
            else:
                self.right.add(number)
            self.last_add = self.last_add[::-1]

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.tree = tree_data

    def data(self):
        return self.tree

    def tree

    def sorted_data(self):
        pass
