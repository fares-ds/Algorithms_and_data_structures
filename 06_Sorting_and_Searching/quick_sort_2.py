def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr) - 1)


def quick_sort_help(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_help(arr, first, split_point - 1)
        quick_sort_help(arr, split_point + 1, last)


def partition(arr, first, last):
    pivot_value = arr[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark


lst = [11, 2, 5, 4, 7, 6, 8, 1, 23]
print(lst)
quick_sort(lst)
print(lst)
