def reverse_string(string):
    # Basic Case
    if len(string) <= 1:
        return string

    # Recursion function
    return reverse_string(string[1:]) + string[0]


print(reverse_string('Hello world'))
