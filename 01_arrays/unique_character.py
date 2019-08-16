def uni_char(string):
    chars = set()
    for letter in string:
        # Check if in set
        if letter in chars:
            return False
        else:
            # Add it to the set
            chars.add(letter)
    return True


# def uni_char(s):
#     return len(set(s)) == len(s)

print(uni_char('agfrgssdfewe'))
