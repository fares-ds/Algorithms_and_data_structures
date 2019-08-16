from collections import defaultdict


def compress(s):
    d = defaultdict()
    compress_string = ''

    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    for key, value in d.items():
        compress_string += f'{key}{value}'
    return compress_string


print(compress('AAAAABBBBCCCC'))
print(compress("AAAABBBBCCCCCDDEEEE"))
