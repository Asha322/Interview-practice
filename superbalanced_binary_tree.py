# check if binary tree is superbalanced (no 2 leaf node depths differ by more than 1)

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_superbalanced(root):
    if root is None:
        return True
    depths = []
    nodes = [(root, 0)]
    while len(nodes) > 0:
        current, depth = nodes.pop(0)
        if (not current.left) and (not current.right) and depth not in depths:
            if len(depths) > 1:
                return False
            if len(depths) == 1 and abs(depths[0] - depth) > 1:
                return False
            else:
                depths.append(depth)
        else:
            if current.left:
                nodes.append((current.left, depth + 1))
            if current.right:
                nodes.append((current.right, depth + 1))
    return True


def test_full_tree():
    tree = BinaryTreeNode(5)
    left = tree.insert_left(8)
    right = tree.insert_right(6)
    left.insert_left(1)
    left.insert_right(2)
    right.insert_left(3)
    right.insert_right(4)
    assert is_superbalanced(tree) is True


def test_one_leaf_node():
    tree = BinaryTreeNode(1)
    tree.insert_left(2)
    tree.insert_left(4)
    assert is_superbalanced(tree) is True


def test_non_balanced_tree():
    tree = BinaryTreeNode(1)
    left = tree.insert_left(2)
    left2 = left.insert_left(4)
    left3 = left2.insert_left(5)
    tree.insert_right(3)
    assert is_superbalanced(tree) is False
