def insertion_sort(lst):
    for i in range(1, len(lst)):

        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = temp


my_list = [3, 7, 8, 19, 11, 10, 22, 20, 12, 1, 4, 9, 2]
insertion_sort(my_list)
print(my_list)
