def permute(s):
    out = []

    # Base case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, letter in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            print(s[:i] + s[i + 1:])
            permutations = permute(s[:i] + s[i + 1:])
            # print(permutations)
            for perm in permutations:
                # Add it to output
                out += [letter + perm]
    return out


def permute_2(lst):
    # Base case
    if len(lst) == 0:
        yield []

    elif len(lst) == 1:
        yield lst

    else:
        # For every letter in string
        for i, letter in enumerate(lst):

            # For every permutation resulting from Step 2 and 3 described above
            permutations = permute_2(lst[:i] + lst[i + 1:])
            # print(permutations)
            for perm in permutations:
                # Add it to output
                yield [letter] + perm


# permutation_1 = permute('abcd')
# print(permutation_1)

permutation_2 = permute_2(list('abcd'))
for permutation in permutation_2:
    print(permutation)
