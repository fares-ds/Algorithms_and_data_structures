class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node):
    current_node = node
    marker = node

    while marker is not None and marker.next_node is not None:

        current_node = current_node.next_node
        marker = marker.next_node.next_node

        # For circle linked list
        if current_node == marker:
            return True

    return False
