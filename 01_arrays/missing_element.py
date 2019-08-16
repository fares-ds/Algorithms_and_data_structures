# def finder(arr_1, arr_2):
#     return sum(arr_1) - sum(arr_2)

import collections


def finder(arr_1, arr_2):
    # Using default dict to avoid key errors
    d = collections.defaultdict(int)
    # Add a count for every instance in Array 1
    for num in arr_2:
        d[num] += 1

    for num in arr_1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(finder(arr1, arr2))
