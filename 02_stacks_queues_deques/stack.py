class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"<Stack Object> : {[item for item in self.items]}"

    def __iter__(self):
        return iter(self.items)


stack = Stack()
stack.push(231)
stack.push(230)
stack.push(243)
stack.push(213)
print(f"The top element is {stack.peek()}")
stack.pop()
print(f"The top element is {stack.peek()}")
print(stack.size())
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
print(stack)
for _ in stack:
    print(_)