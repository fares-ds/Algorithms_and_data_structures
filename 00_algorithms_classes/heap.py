class HeapEmptyError(Exception):
    pass


class Heap:
    def __init__(self, max_size=16):
        self.heap_list = [None] * max_size
        self.size = 0
        self.heap_list[0] = 99999

    def insert(self, value):
        self.size += 1
        self.heap_list[self.size] = value
        self.restore_up(self.size)

    def restore_up(self, i):
        new_element = self.heap_list[i]
        while self.heap_list[i // 2] < self.heap_list[i] and i > 1:
            self.heap_list[i] = self.heap_list[i // 2]
            self.heap_list[i // 2] = new_element
            i = i // 2

    def delete_root(self):
        if self.size == 0:
            raise HeapEmptyError("Heap is empty")
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.restore_down(1)
        return max_value

    def restore_down(self, i):
        current_key = self.heap_list[i]
        left_child = 2 * i
        right_child = 2 * i + 1

        while right_child <= self.size:
            # Both children are smaller than current_key
            if current_key >= self.heap_list[left_child] and current_key >= self.heap_list[right_child]:
                self.heap_list[i] = current_key
                return
            # One of the children or both are greater than the current_key
            else:
                if self.heap_list[left_child] > self.heap_list[right_child]:
                    self.heap_list[i] = self.heap_list[left_child]
                    i = left_child
                else:
                    self.heap_list[i] = self.heap_list[right_child]
                    i = right_child

            left_child = 2 * i
            right_child = 2 * i + 1

        if left_child == self.size and current_key < self.heap_list[left_child]:
            self.heap_list[i] = self.heap_list[left_child]
            i = left_child
        self.heap_list[i] = current_key

    def __str__(self):
        return f"<Class Heap: {[self.heap_list[item] for item in range(1, self.size)]}>"
