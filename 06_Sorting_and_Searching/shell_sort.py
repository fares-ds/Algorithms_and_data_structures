def shell_sort(lst):
    sub_list_count = len(lst) // 2

    # While we still have sub lists
    while sub_list_count > 0:
        for start in range(sub_list_count):

            # Use a gap insertion
            gap_insertion_sort(lst, start, sub_list_count)

        sub_list_count = sub_list_count // 2


def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_value = lst[i]
        position = i

        # Using the Gap
        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position = position - gap

        # Set current value
        lst[position] = current_value


my_list = [3, 7, 8, 19, 11, 10, 22, 20, 12, 1, 4, 9, 2]
print(f"Unsorted list {my_list}")
shell_sort(my_list)
print(my_list)
