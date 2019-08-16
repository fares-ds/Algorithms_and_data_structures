def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:

        mid = (first + last) // 2

        if lst[mid] == item:
            found = True

        else:
            if lst[mid] > item:
                first = mid + 1
            else:
                last = mid - 1
    return found


def rec_binary_search(lst, item):
    if len(lst) == 0:
        return False

    else:

        mid = len(lst) // 2

        if lst[mid] == item:
            return True

        else:
            if lst[mid] > item:
                return rec_binary_search(lst[:mid], item)
            else:
                return rec_binary_search(lst[mid+1:], item)


list_1 = list(range(1, 14, 2))
print(binary_search(list_1, 7))
print(rec_binary_search(list_1, 6))
