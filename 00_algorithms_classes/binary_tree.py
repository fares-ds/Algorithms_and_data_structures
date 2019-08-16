from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        self._display(self.head, 0)
        print()

    def _display(self, p, tree_level):
        if p is None:
            return
        self._display(p.right_child, tree_level + 1)
        print()

        for i in range(tree_level):
            print("     ", end='')
        print(p.data)
        self._display(p.left_child, tree_level + 1)

    def preorder(self):
        self._preorder(self.head)
        print()

    def _preorder(self, node):
        if node is None:
            return
        print(node.data, " ", end='')
        self._preorder(node.left_child)
        self._preorder(node.right_child)

    def inorder(self):
        self._inorder(self.head)
        print()

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left_child)
        print(node.data, " ", end='')
        self._inorder(node.right_child)

    def postorder(self):
        self._postorder(self.head)
        print()

    def _postorder(self, node):
        if node is None:
            return
        self._postorder(node.left_child)
        self._postorder(node.right_child)
        print(node.data, " ", end='')

    def level_order(self):
        if self.head is None:
            print("Tree is empty")
            return

        qu = deque()
        qu.append(self.head)

        while len(qu) != 0:
            p = qu.popleft()
            print(p.data + " ", end='')
            if p.left_child is not None:
                qu.append(p.left_child)
            if p.right_child is not None:
                qu.append(p.right_child)

    def height(self):
        return self._height(self.head)

    def _height(self, node):
        if node is None:
            return 0
        height_left = self._height(node.left_child)
        height_right = self._height(node.right_child)

        if height_left > height_right:
            return 1 + height_left
        return 1 + height_right

    def create_tree(self):
        self.head = Node('P')
        self.head.left_child = Node('Q')
        self.head.right_child = Node('R')
        self.head.left_child.left_child = Node('A')
        self.head.left_child.right_child = Node('B')
        self.head.right_child.left_child = Node('X')


bt = BinaryTree()
bt.create_tree()

bt.display()
print()

print("Preorder : ")
bt.preorder()
print("")

print("Inorder : ")
bt.inorder()
print()

print("Postorder : ")
bt.postorder()
print()

print(f"Height of tree is {bt.height()}")
