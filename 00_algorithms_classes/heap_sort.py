def heap_sort(lst, size):
    build_heap_bottom_up(lst, size)

    while size > 1:
        lst[size], lst[1] = lst[1], lst[size]
        size -= 1
        restore_down(1, lst, size)


def build_heap_bottom_up(lst, size):
    i = size // 2
    while i >= 1:
        restore_down(i, lst, size)
        i -= 1


def restore_down(i, lst, size):
    current = lst[i]
    left_child = 2 * i
    right_child = 2 * i + 1

    while right_child <= size:
        if current >= lst[left_child] and current >= lst[right_child]:
            lst[i] = current
            return

        elif lst[left_child] > lst[right_child]:
            lst[i] = lst[left_child]
            i = left_child

        else:
            lst[i] = lst[right_child]
            i = right_child

        left_child = 2 * i
        right_child = 2 * i + 1

    if left_child == size and current < lst[left_child]:
        lst[i] = lst[left_child]
        i = left_child
    lst[i] = current


lst_1 = [0, 1, 27, 17, 23, 3, 21, 13, 19, 25, 5, 11, 7, 9, 15]
heap_sort(lst_1, len(lst_1) - 1)
print(lst_1)
