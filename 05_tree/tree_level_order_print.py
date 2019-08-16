class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"<Node {self.data}>"


class BinaryTree:
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


def level_order_print(tree: BinaryTree):
    parent_nodes = [tree.head]
    children_nodes = []

    while parent_nodes:

        for node in parent_nodes:
            print(node.data, end=' ')
            if node.left_child is not None:
                children_nodes.append(node.left_child)
            if node.right_child is not None:
                children_nodes.append(node.right_child)
        print()

        parent_nodes = children_nodes
        children_nodes = []


my_tree = BinaryTree(Node(4))
my_tree.add(Node(3))
my_tree.add(Node(3.5))
my_tree.add(Node(2))
my_tree.add(Node(6))
my_tree.add(Node(5))
my_tree.add(Node(7))

level_order_print(my_tree)
