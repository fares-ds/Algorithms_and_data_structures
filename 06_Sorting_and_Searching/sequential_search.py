def seq_search(lst, item):
    position = 0
    found = False

    while position < len(lst) and not found:

        if lst[position] == item:
            found = True

        else:
            position += 1

    return found


def ordered_seq_search(lst, item):
    position = 0
    found = False
    stopped = False

    while position < len(lst) and not found and not stopped:
        print(lst[position])

        if lst[position] == item:
            found = True

        elif lst[position] > item:
            stopped = True

        else:
            position += 1

    return found


list_1 = [9, 1, 7, 21, 3, 2]
print(seq_search(list_1, 2))

list_2 = list(range(1, 14, 2))
print(ordered_seq_search(list_2, 6))
