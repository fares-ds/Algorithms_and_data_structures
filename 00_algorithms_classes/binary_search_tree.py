class TreeEmptyError(Exception):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, value):
        current_node = self.head
        parent = None
        while current_node is not None:
            parent = current_node
            if value < current_node.data:
                current_node = current_node.left_child
            elif value > current_node.data:
                current_node = current_node.right_child
            else:
                print(f"Element {value} already exist in the tree.")
                return

        if parent is None:
            self.head = Node(value)
        elif value < parent.data:
            parent.left_child = Node(value)
        else:
            parent.right_child = Node(value)

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if value < current_node.data:
                current_node = current_node.left_child
            elif value > current_node.data:
                current_node = current_node.right_child
            else:
                return True
        return False

    def find_min(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        current_node = self.head
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.data

    def find_max(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        current_node = self.head
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node.data

    def in_order(self):
        self._in_order(self.head)
        print()

    def _in_order(self, node):
        if node is None:
            return
        self._in_order(node.left_child)
        print(node.data, " ", end='')
        self._in_order(node.right_child)

    def delete(self, value):

        current_node = self.head
        parent = None
        while current_node is not None:
            if current_node.data == value:
                break

            parent = current_node
            if value < current_node.data:
                current_node = current_node.left_child
            elif value > current_node.data:
                current_node = current_node.right_child

        if current_node is None:
            print(f"{value} not found")
            return

        # Node to be deleted is head
        if parent is None:
            in_successor = current_node.right_child
            while in_successor.left_child is not None:
                in_successor = in_successor.left_child

            value = in_successor.data
            self.delete(in_successor.data)
            self.head.data = value

        # Node is leaf.
        elif current_node.left_child is None and current_node.right_child is None:
            if parent.left_child == current_node:
                parent.left_child = None
            elif parent.right_child == current_node:
                parent.right_child = None

        # Node has only one child.
        elif current_node.left_child is None or current_node.right_child is None:
            if parent.right_child == current_node:
                if current_node.right_child is None:
                    parent.right_child = current_node.left_child
                else:
                    parent.right_child = current_node.right_child
            elif parent.left_child == current_node:
                if current_node.left_child is None:
                    parent.left_child = current_node.right_child
                else:
                    parent.left_child = current_node.left_child

        # Node has both children
        else:
            in_successor = current_node.right_child
            while in_successor.left_child is not None:
                in_successor = in_successor.left_child

            value = in_successor.data
            self.delete(in_successor.data)
            if parent.left_child == current_node:
                parent.left_child.data = value
            else:
                parent.right_child.data = value

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


bst = BinarySearchTree()

# print(f"Tree is empty? {bst.is_empty()}")

print("Inserting some values...")

bst.insert(70)
bst.insert(30)
bst.insert(84)
bst.insert(95)
bst.insert(78)
bst.insert(86)
bst.insert(72)
bst.insert(73)
bst.insert(45)
bst.insert(12)
bst.insert(9)
bst.insert(38)
bst.insert(35)
bst.insert(60)

# print(f"The minimum is : {bst.find_min()}")
# print(f"The maximum is : {bst.find_max()}")

print("Printing the tree in In_order : ")
bst.in_order()
bst.delete(70)
bst.in_order()
bst.display()
