def linear_search(lst, element):
    for item in lst:
        if item == element:
            return True
    return False


lst_1 = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
print(linear_search(lst_1, 14))
