def insertion_sort(lst):

    # For every index in array
    for i in range(1, len(lst)):

        # Set current values and position
        current_value = lst[i]
        position = i - 1

        # Sorted Sublist
        while position >= 0 and current_value < lst[position]:
            lst[position + 1] = lst[position]
            position -= 1
        lst[position + 1] = current_value


my_list = [3, 7, 8, 19, 11, 10, 22, 20, 12, 1, 4, 9, 2]
print(f"Unsorted list {my_list}")
insertion_sort(my_list)
print(my_list)
