def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]


my_list = list(range(1, 99, 2))
my_list.reverse()
print(my_list)
selection_sort(my_list)
print(my_list)
