def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)


def _quick_sort(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        _quick_sort(lst, first, split_point - 1)
        _quick_sort(lst, split_point + 1, last)


def partition(lst, low, up):
    pivot_index = get_pivot(lst, low, up)
    pivot_value = lst[pivot_index]
    lst[pivot_index], lst[low] = lst[low], lst[pivot_index]
    border = low

    for i in range(low, up + 1):
        if lst[i] < pivot_value:
            border += 1
            lst[i], lst[border] = lst[border], lst[i]
    lst[low], lst[border] = lst[border], lst[low]
    return border


def get_pivot(lst, low, up):
    mid = (up + low) // 2
    pivot = up
    if lst[mid] < lst[up]:
        pivot = mid

    elif lst[low] < lst[up]:
        pivot = low
    return pivot


arr = [11, 2, 5, 4, 7, 6, 8, 1, 23]
print(arr)
quick_sort(arr)
print(arr)
