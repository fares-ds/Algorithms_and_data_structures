def bubble_sort(lst):
    for i in range(len(lst) - 1):

        swaps = 0
        for j in range(len(lst) - i - 1):

            if lst[j + 1] < lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                swaps += 1

        if swaps == 0:
            break
        print(lst)


my_list = [12, 2, 4, 7, 1, 3, 9, 10]
print(f"Unsorted list {my_list}")
bubble_sort(my_list)
# print(my_list)
