class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


def tree_max(node):
    if not node:
        return float("-inf")
    max_left = tree_max(node.left)
    max_right = tree_max(node.right)
    return max(node.key, max_left, max_right)


def tree_min(node):
    if not node:
        return float("inf")
    min_left = tree_min(node.left)
    min_right = tree_min(node.right)
    return min(node.key, min_left, min_right)


def verify(node):
    if not node:
        return True
    if tree_max(node.left) <= node.key <= tree_min(node.right) and verify(node.left) and verify(node.right):
        return True
    else:
        return False


root = Node(10, "Hello")
root.left = Node(5, "Five")
root.right = Node(30, "Thirty")

print(verify(root))

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root))
