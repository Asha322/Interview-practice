# Find second largest element in a binary search tree


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


def find_max(root):
    while root.right:
        root = root.right
    return root.value


def find_second_largest(root):
    while root:
        if root.left and not root.right:
            return find_max(root.left)
        if root.right and not root.right.left and not root.right.right:
            return root.value
        root = root.right


def test_full_tree():
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(70)
    left.insert_left(10)
    left.insert_right(40)
    right.insert_left(60)
    right.insert_right(80)
    assert find_second_largest(tree) == 70


def test_largest_has_a_left_child():
    tree = BinaryTreeNode(50)
    tree.insert_left(30)
    right = tree.insert_right(70)
    right.insert_left(60)
    assert find_second_largest(tree) == 60


def test_largest_has_a_left_subtree():
    tree = BinaryTreeNode(50)
    tree.insert_left(30)
    right = tree.insert_right(70)
    rightleft = right.insert_left(60)
    rightleft.insert_right(65)
    assert find_second_largest(tree) == 65


def test_second_largest_is_root_node():
    tree = BinaryTreeNode(50)
    tree.insert_left(30)
    tree.insert_right(70)
    assert find_second_largest(tree) == 50