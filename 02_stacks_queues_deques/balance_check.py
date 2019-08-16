def balance_check(string):
    if len(string) % 2 == 1:
        return False

    opening = set('([{')
    matches = {('(', ')'), ('[', ']'), ('{', '}')}

    stack = []

    for paren in string:

        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


print(balance_check('[(])'))
