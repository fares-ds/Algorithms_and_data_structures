def shell_sort(lst):
    # h = int(input("Enter maximum increment (odd value) : "))
    h = 5
    while h >= 1:
        for i in range(h, len(lst)):
            temp = lst[i]
            j = i - h

            while j >= 0 and lst[j] > temp:
                lst[j + h] = lst[j]
                j = j - h
            lst[j + h] = temp
        print(f"h = {h} {42 * '='}")
        print(lst)
        h = h - 2


my_list = [21, 60, 2, 7, 8, 11, 1, 19, 9, 4, 48, 3, 5, 17, 16, 13, 59]

shell_sort(my_list)
print(my_list)
