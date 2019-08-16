class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        current_node = self.head
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next_node
        return counter

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next_node is None:
                    break
                last_node = last_node.next_node
            last_node.next_node = new_node

    def insert_head(self, new_head):
        new_head.next_node, self.head = self.head, new_head

    def insert_middle(self, node, index):
        if index < 0 or index > self.length():
            print("Index out of range")
            return
        if index is 0:
            self.insert_head(node)
            return
        previous_node = self.head
        current_node = self.head
        counter = 0
        while True:
            if counter == index:
                previous_node.next_node, node.next_node = node, current_node
                break
            previous_node = current_node
            current_node = current_node.next_node
            counter += 1

    def delete_end(self):
        current_node = self.head
        last_node = self.head
        while True:
            if current_node.next_node is None:
                last_node.next_node = None
                del current_node
                break
            last_node = current_node
            current_node = current_node.next_node

    def delete_node(self, index):
        if index < 0 or index > self.length() - 1:
            print("Index out of range")
            return
        if index == self.length() - 1:
            self.delete_end()
            return
        if index == 0:
            new_head = self.head.next_node
            self.head = new_head
            return
        elif index <= self.length():
            current_node = self.head
            previous_node = self.head
            counter = 0
            while current_node.next_node is not None:
                if counter == index:
                    previous_node.next_node = current_node.next_node
                    del current_node
                    break
                previous_node = current_node
                current_node = current_node.next_node
                counter += 1

    def reverse_list(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_element = current_node.next_node
            current_node.next_node, previous_node = previous_node, current_node
            current_node = next_element
        self.head = previous_node

    def bubble_sort(self):
        end = None
        while end != self.head.next_node:
            current_node = self.head
            while current_node.next_node != end:
                if current_node.data > current_node.next_node.data:
                    current_node.data, current_node.next_node.data = current_node.next_node.data, current_node.data
                current_node = current_node.next_node
            end = current_node

    def print_list(self):
        if self.head is None:
            print("Your list is empty")
            return
        current_node = self.head
        while current_node is not None:
            if current_node.next_node is not None:
                print(f"{current_node.data} => ", end='')
            else:
                print(f"{current_node.data}")
            current_node = current_node.next_node

    def __str__(self):
        return f"Linked List class"


linked_list = LinkedList()

# Adding item at the end
first_node = Node("Fares")
linked_list.insert_end(first_node)
second_node = Node("Alberto")
linked_list.insert_end(second_node)
third_node = Node("Ze Roberto")
linked_list.insert_end(third_node)
zero_node = Node("Venous Junior")

# Adding item at the beginning
linked_list.insert_head(zero_node)

# Adding items at the middle
middle_node = Node("Douglas Costa")
linked_list.insert_middle(middle_node, 1)
linked_list.print_list()

linked_list.bubble_sort()
linked_list.print_list()
print(linked_list)
