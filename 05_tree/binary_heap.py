class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def is_empty(self):
        return self.heap_list == [0]

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self._min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[mc], self.heap_list[i] = self.heap_list[i], self.heap_list[mc]
            i = mc

    def _min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[2 * i + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.percolate_down(i)
            i = i - 1

    def __str__(self):
        return f"<Heap List Object>{[self.heap_list[item] for item in range(1, self.current_size)]}"


heap = BinaryHeap()
list_1 = [9, 12, 1, 4, 43, 11, 3, 2]
heap.build_heap(list_1)
print(heap)
# x = heap.del_min()
# print(x)
# print(heap)
# x = heap.del_min()
# print(x)
# print(heap)
# x = heap.del_min()
# print(x)
# print(heap)
# print(heap.is_empty())
