class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def contains_cycle(first):
    slow = first
    fast = first

    while fast is not None and slow is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        return False


def delete_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next


def reverse(head_node):
    current = head_node
    next = None
    previous = None

    while current:
        next = head_node.next
        current.next = previous
        previous = current
        current = next


def find_Kth(head, k):
    current = head
    length = head

    for i in range(0, k):
        length = length.next

    while length.next:
        length = length.next
        current = current.next
    return current
