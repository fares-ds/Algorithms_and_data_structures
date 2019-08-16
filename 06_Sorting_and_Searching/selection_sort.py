# def selection_sort(lst):
#     for i in range(len(lst) - 1):
#         min_location = i
#         for j in range(i, len(lst)):
#             if lst[j] < lst[min_location]:
#                 min_location = j
#
#         if min_location != i:
#             lst[min_location], lst[i] = lst[i], lst[min_location]
#
#         print(lst)


def selection_sort(arr):
    # For every slot in array
    for fill_slot in range(len(arr) - 1, 0, -1):
        position_of_max = 0

        # For every set of 0 to fill_slot+1
        for location in range(1, fill_slot + 1):
            # Set maximum's location
            if arr[location] > arr[position_of_max]:
                position_of_max = location

        arr[fill_slot], arr[position_of_max] = arr[position_of_max], arr[fill_slot]


my_list = [12, 2, 4, 7, 1, 3, 9, 10]
print(f"Unsorted list {my_list}")
selection_sort(my_list)
print(my_list)
