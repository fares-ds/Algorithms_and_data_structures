def merge_sort(lst):
    # Split each element into partitions of size 1
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Recursively merge adjacent partitions
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i = i + 1

            else:
                lst[k] = right_half[j]
                j = j + 1

            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1
    print(f"Merging {lst}")


arr = [11, 2, 5, 4, 7, 6, 8, 1, 23]
print(arr)
merge_sort(arr)
print(arr)
