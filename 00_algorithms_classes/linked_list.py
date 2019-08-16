class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add_item(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def add_head(self, data):
        new_first_node = Node(data)
        new_first_node.next, self.head.next = self.head.next, new_first_node

    def delete_item(self, index):
        if index >= self.length():
            print('ERROR: "delete_item" Index out of range!')
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node, current_node = current_node, current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get_item(self, index):
        if index >= self.length():
            print('ERROR: "get_item" Index out of range!')
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1


my_list = LinkedList()
my_list.add_item(23)
my_list.add_item(213)
my_list.add_item(223)
my_list.add_item(253)
my_list.add_item(2367)
my_list.add_head(11111)

my_list.display()
print(my_list.length())
print(f"Element at index 3 is {my_list.get_item(3)}")
my_list.delete_item(0)
print(my_list.length())
print(f"Element at index 3 is {my_list.get_item(3)}")
my_list.display()
