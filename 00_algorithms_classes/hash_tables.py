class InvalidOperationException(Exception):
    pass


class StudentRecord:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def __str__(self):
        return f"{self.student_id} {self.student_name}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print("_____")
            return

        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data} ", end='')
            current_node = current_node.next_node
        print()

    def search(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.data.get_student_id() == item:
                return current_node.data
            current_node = current_node.next_node
        else:
            return None

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.next_node = self.head
        self.head = temp

    def delete_node(self, item):
        if self.head is None:
            print("List is empty.")
            return

        # Deletion of first node
        if self.head.data.get_student_id() == item:
            self.head = self.head.next_node
            return

        # Deletion in between or at the end
        current_node = self.head
        while current_node.next_node is not None:
            if current_node.next_node.data.get_student_id() == item:
                break
            current_node = current_node.next_node

        if current_node.next_node is None:
            print(f"Element {item} not in list.")
        else:
            current_node.next_node = current_node.next_node.next_node


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.array = [None] * self.table_size
        self.size = 0

    def hash(self, key):
        return key % self.table_size

    def display_table(self):
        for i in range(self.table_size):
            print(f"[{i}] --> ", end='')
            if self.array[i] is not None:
                self.array[i].display_list()
            else:
                print("_____")

    def insert(self, new_record):
        key = new_record.get_student_id()
        h = self.hash(key)

        if self.array[h] is None:
            self.array[h] = LinkedList()
        self.array[h].insert_in_beginning(new_record)
        self.size += 1

    def search(self, key):
        h = self.hash(key)
        if self.array[h] is not None:
            return self.array[h].search(key)
        return None

    def delete(self, key):
        h = self.hash(key)
        if self.array[h] is not None:
            self.array[h].delete_node(key)
            self.size -= 1
        else:
            print(f"Value {key} not present.")


size = int(input("Enter initial size of table : "))
table = HashTable(size)

while True:
    print("1. Insert a record.")
    print("2. Search a record.")
    print("3. Delete a record.")
    print("4. Display table.")
    print("5. Exit.")

    option = int(input("Enter your option : "))

    if option == 1:
        id = int(input("Enter student id : "))
        name = input("Enter student name : ")
        a_record = StudentRecord(id, name)
        table.insert(a_record)

    elif option == 2:
        id = int(input("Enter a key to be searched : "))
        a_record = table.search(id)

        if a_record is None:
            print("Key not found.")
        else:
            print(a_record)

    elif option == 3:
        id = int(input("Enter a key to be deleted : "))
        table.delete(id)

    elif option == 4:
        table.display_table()

    elif option == 5:
        break

    else:
        print("Wrong option.")

    print()
