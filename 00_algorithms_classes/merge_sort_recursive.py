def merge_sort(lst):
    sorted_lst = [None] * len(lst)
    sort(lst, sorted_lst, 0, len(lst) - 1)


def sort(lst, sorted_lst, low, up):
    if low == up:
        return

    mid = (low + up) // 2
    # Sort the left side
    sort(lst, sorted_lst, low, mid)
    # Sort the right side
    sort(lst, sorted_lst, mid + 1, up)

    # Merge the two sorted lists
    merge(lst, sorted_lst, low, mid, mid + 1, up)

    copy(lst, sorted_lst, low, up)


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


def copy(lst, sorted_lst, low, up):
    for i in range(low, up + 1):
        lst[i] = sorted_lst[i]


list_1 = [91, 88, 16, 35, 52, 12, 28, 67, 29]
print(f"This list {list_1} sorted using 'Merge Sort'")
merge_sort(list_1)
print(list_1)
