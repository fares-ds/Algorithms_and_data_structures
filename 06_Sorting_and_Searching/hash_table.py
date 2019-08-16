class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, val):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = val

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = val

            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(hash_value, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = val
                else:
                    self.data[next_slot] = val

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


h = HashTable(7)
h[1] = "One"
h[4] = "Four"
h[6] = "Six"

print(h[6])

