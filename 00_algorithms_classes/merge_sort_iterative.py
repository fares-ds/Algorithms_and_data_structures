def merge_sort(lst):
    sorted_lst = [None] * len(lst)
    size = 1
    while size <= len(lst) - 1:
        sort_pass(lst, sorted_lst, size, len(lst))
        print(sorted_lst)
        size = size * 2


def sort_pass(lst, sorted_lst, size, length):
    low_1 = 0
    while low_1 + size <= length - 1:
        up_1 = low_1 + size - 1
        low_2 = low_1 + size
        up_2 = low_2 + size - 1

        if up_2 >= length:
            up_2 = length - 1

        merge(lst, sorted_lst, low_1, up_1, low_2, up_2)
        low_1 = up_2 + 1
    for i in range(low_1, length):
        sorted_lst[i] = lst[i]

    copy(lst, sorted_lst, length)


def merge(lst, sorted_lst, low_1, up_1, low_2, up_2):
    i, j, k = low_1, low_2, low_1

    while i <= up_1 and j <= up_2:
        if lst[i] <= lst[j]:
            sorted_lst[k] = lst[i]
            i += 1

        else:
            sorted_lst[k] = lst[j]
            j += 1
        k += 1

    while i <= up_1:
        sorted_lst[k] = lst[i]
        i += 1
        k += 1

    while j <= up_2:
        sorted_lst[k] = lst[j]
        j += 1
        k += 1


def copy(lst, sorted_lst, length):
    for i in range(length):
        lst[i] = sorted_lst[i]


list_1 = [91, 88, 16, 35, 52, 12, 28, 67, 29]
print(f"This list {list_1} sorted using 'Merge Sort'")
merge_sort(list_1)
print(list_1)
