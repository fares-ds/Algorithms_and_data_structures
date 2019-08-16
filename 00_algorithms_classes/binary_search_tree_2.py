from node import Node


class BinarySearchTree:
    def __init__(self, head: Node):
        self.head = head

    def is_empty(self):
        return self.head is None

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.data == current_node.data:
                raise ValueError(f"A node with the value {new_node.data} already exist.")

            elif new_node.data < current_node.data:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = new_node
                    break

            else:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = new_node
                    break

    def in_order(self):
        self._in_order(self.head)

    def _in_order(self, node):
        if node is None:
            return
        self._in_order(node.left_child)
        print(node)
        self._in_order(node.right_child)

    def find(self, value: int):
        current_node = self.head
        while current_node is not None:
            if value == current_node.data:
                return current_node

            elif value < current_node.data:
                current_node = current_node.left_child

            else:
                current_node = current_node.right_child

        raise LookupError(f"A node with value {value} was not found.")

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.data == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left_child is not None and current_node.left_child.data == value) or \
                    (current_node.right_child is not None and current_node.right_child.data == value):
                return current_node

            elif value < current_node.data:
                current_node = current_node.left_child

            elif value > current_node.data:
                current_node = current_node.right_child

    @classmethod
    def find_rightmost(cls, node: Node) -> Node:
        rightmost_node = node
        while rightmost_node.right_child is not None:
            rightmost_node = rightmost_node.right_child
        return rightmost_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        # We have two children
        if to_delete.left_child and to_delete.right_child:
            rightmost = self.find_rightmost(to_delete.left_child)
            rightmost_parent = self.find_parent(rightmost.data)

            if rightmost_parent != to_delete:
                rightmost_parent.right_child = rightmost.left_child
                rightmost.left_child = to_delete.left_child
            rightmost.right_child = to_delete.right_child

            if to_delete == to_delete_parent.left_child:
                to_delete_parent.left_child = rightmost

            elif to_delete == to_delete_parent.right_child:
                to_delete_parent.right_child = rightmost
            else:
                self.head = rightmost

        # We have one child
        elif to_delete.left_child or to_delete.right_child:
            if to_delete == to_delete_parent.left_child:
                to_delete_parent.left_child = to_delete.right_child or to_delete.left_child
            elif to_delete == to_delete_parent.right_child:
                to_delete_parent.right_child = to_delete.right_child or to_delete.left_child
            else:
                self.head = to_delete.right_child or to_delete.left_child

        # No children
        else:
            if to_delete == to_delete_parent.left_child:
                to_delete_parent.left_child = None
            elif to_delete == to_delete_parent.left_child:
                to_delete_parent.right_child = None
            else:
                self.head = None

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
