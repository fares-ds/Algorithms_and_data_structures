class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"<Node {self.data}>"
