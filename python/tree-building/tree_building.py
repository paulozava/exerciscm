class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def build_tree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if records:
        check_tree_integrity(ordered_id)

    trees = [Node(ordered_id[id])
             for id in range(len(ordered_id))
             for branches in records
             if is_tree_member(id, branches, ordered_id)]

    branches = {}
    for id in range(len(ordered_id)):
        for node in trees:
            if id == node.node_id:
                branches = node
        for node in records:
            if node.parent_id == id:
                for child in trees:
                    if node.record_id == child.node_id and child.node_id != 0:
                        branches.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root


def is_tree_member(i, j, ordered_id):
    if ordered_id[i] == j.record_id:
        check_branches_integrity(j)
        return True
    return False


def check_branches_integrity(j):
    if j.record_id == 0 and j.parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    if j.record_id < j.parent_id:
        raise ValueError('Parent id must be lower than child id')
    if j.record_id == j.parent_id and j.record_id != 0:
        raise ValueError('Tree is a cycle')


def check_tree_integrity(ordered_id):
    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError('Tree must be continuous')
    elif ordered_id[0] != 0:
        raise ValueError('Tree must start with id 0')
