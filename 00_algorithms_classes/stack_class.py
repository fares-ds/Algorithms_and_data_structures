class Stack:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __repr__(self):
        return f"Stack({[item for item in self.items]})"


stack = Stack()
stack.push('one')
stack.push('two')
stack.push('three')
stack.push('four')
print(stack)
stack.pop()
print(stack)
new_stack = Stack(['one', 'two', 'three', 'four'])
print(new_stack)
