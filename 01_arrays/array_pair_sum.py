import time
import random


def pair_sum(arr, k):
    seen = set()
    combination = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            combination.add((max(num, target), min(num, target)))
    return len(combination)


start_list = time.time()
my_list = [i for i in range(1000000)]
random.shuffle(my_list)
end_list = time.time()

print(f"Creating the list... {end_list - start_list}")

start = time.time()
print(pair_sum(my_list, 400000))
end = time.time()

print(f"Time = {end - start}")
