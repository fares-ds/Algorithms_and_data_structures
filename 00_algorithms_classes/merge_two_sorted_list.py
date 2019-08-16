def merge_two_lists(lst_1, lst_2):
    full_list = []
    i, j = 0, 0

    while i <= len(lst_1) - 1 and j <= len(lst_2) - 1:
        if lst_1[i] < lst_2[j]:
            full_list.append(lst_1[i])
            i += 1

        elif lst_1[i] > lst_2[j]:
            full_list.append(lst_2[j])
            j += 1

    while i <= len(lst_1) - 1:
        full_list.append(lst_1[i])
        i += 1

    while j <= len(lst_2) - 1:
        full_list.append(lst_2[j])
        j += 1
    return full_list


list_1 = [91, 88, 16, 35, 52,12, 28, 67, 29]
list_1.sort()
list_2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print(f"Merging :{list_1}\nand      {list_2}")
print(merge_two_lists(list_1, list_2))
