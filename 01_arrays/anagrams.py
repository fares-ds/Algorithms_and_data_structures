# sort the string
def sort_string(string):
    sorted_list = sorted(string)
    new_string = ''.join(sorted_list)
    return new_string


# elimination of all spaces
def string_abrute(string):
    string_list = string.split(' ')
    new_string = ''.join(string_list)
    return sort_string(new_string)


def anagram(s1, s2):
    s1 = string_abrute(s1)
    s2 = string_abrute(s2)
    if s1 == s2:
        return True
    return False


print(anagram(' dog', 'god'))
print(anagram('clint eastwood', 'old west action'))
print(anagram('aba', 'bab'))
print(anagram('public relations', 'crap built on lies'))
print(anagram(' 1 2', '1 2 '))
