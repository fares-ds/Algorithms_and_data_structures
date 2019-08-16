class Queue:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def push(self, item):
        self.items.append(item)

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head

    def __repr__(self):
        return f"Queue({[item for item in self.items]})"


queue = Queue()
queue.push('one')
queue.push('two')
queue.push('Three')
queue.push('Four')
print(queue)
queue.pop()
print(queue)
