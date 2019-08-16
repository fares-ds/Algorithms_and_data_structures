def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    mid = (first + last) // 2
    number_of_iterations = 0
    while last >= first:
        number_of_iterations += 1
        print(number_of_iterations)
        if item == lst[mid]:
            return mid

        elif item > lst[mid]:
            first = mid + 1

        else:
            last = mid - 1

        mid = (first + last) // 2

    return f"Element {item} not found."


sorted_list = list(range(12, 43, 2))
print(sorted_list)
# print(f"Element 41 is found at index {binary_search(sorted_list, 41)}")
print(binary_search(sorted_list, 12))
