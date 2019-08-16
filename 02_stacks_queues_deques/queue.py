class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"<Queue Object> : {[item for item in self.items]}"


queue = Queue()
print(queue.is_empty())

queue.enqueue("one")
queue.enqueue("two")
queue.enqueue("three")

print(queue)
print(f"Queue size : {queue.size()}")
queue.dequeue()
print(queue)
