class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


a = DoublyLinkedListNode(2)
b = DoublyLinkedListNode(4)
c = DoublyLinkedListNode(6)

a.next_node = b
b.next_node = c
b.previous_node = a
c.previous_node = b
