def quick_sort(lst):
    _sort(lst, 0, len(lst) - 1)


def _sort(lst, low, up):
    if low >= up:
        return

    pivot = partition(lst, low, up)
    _sort(lst, low, pivot - 1)
    _sort(lst, pivot + 1, up)


def partition(lst, low, up):
    pivot = lst[low]
    i = low + 1
    j = up

    while i <= j:
        while lst[i] < pivot and i < up:
            i += 1

        while lst[j] > pivot:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        else:
            break
    lst[low], lst[j] = lst[j], pivot
    return j


lst_test = [5, 3, 1, 9, 6, 4, 7, 2]

quick_sort(lst_test)
print(lst_test)
