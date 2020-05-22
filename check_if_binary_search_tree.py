# check if a binary tree is a binary search tree


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


def check_if_binary_search_tree(root, min, max):
    if not root:
        return True
    return check_if_binary_search_tree(root.left, min, root.value) and \
           check_if_binary_search_tree(root.right, root.value, max) and max >= root.value >= min


def if_binary_search_tree(root):
    return check_if_binary_search_tree(root, -float('inf'), float('inf'))


def test_non_binary():
    tree = BinaryTreeNode(5)
    left = tree.insert_left(8)
    right = tree.insert_right(6)
    left.insert_left(1)
    left.insert_right(2)
    right.insert_left(3)
    right.insert_right(4)
    assert if_binary_search_tree(tree) is False


def test_one_leaf_binary_search():
    tree = BinaryTreeNode(5)
    tree.insert_left(4)
    assert if_binary_search_tree(tree) is True


def test_one_leaf_not_binary_search():
    tree = BinaryTreeNode(5)
    tree.insert_left(9)
    assert if_binary_search_tree(tree) is False


def test_one_node():
    tree = BinaryTreeNode(5)
    assert if_binary_search_tree(tree) is True


def test_larger_binary_search():
    tree = BinaryTreeNode(5)
    left = tree.insert_left(2)
    right = tree.insert_right(8)
    left.insert_left(1)
    left.insert_right(3)
    right.insert_left(6)
    right.insert_right(9)
    assert if_binary_search_tree(tree) is True

