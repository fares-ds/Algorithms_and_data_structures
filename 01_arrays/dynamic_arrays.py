import ctypes


class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.a = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError("Index out of range!")
        return self.a[item]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if capacity isn't enough
        self.a[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        b = self.make_array(new_capacity)
        for k in range(self.n):
            b[k] = self.a[k]

        self.a = b
        self.capacity = new_capacity

    @classmethod
    def make_array(cls, new_capacity):
        return (new_capacity * ctypes.py_object)()

    # def __str__(self):
    #     return str(self)
    def __iter__(self):
        pass


arr = DynamicArray()
for _ in range(5):
    arr.append(_)
print(arr[4])

# print(arr)
