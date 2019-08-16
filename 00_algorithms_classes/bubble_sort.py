def bubble_sort(lst):
    for i in range(len(lst) - 1):

        swaps = 0
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                swaps += 1

        if swaps == 0:
            break


my_list = [3, 7, 8, 12, 1, 2, 4, 9, 11, 5, 19, 10, 20, 21]
print(f"The length of your list is {len(my_list)}")
bubble_sort(my_list)
print(my_list)
