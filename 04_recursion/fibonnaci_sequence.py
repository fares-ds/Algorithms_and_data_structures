# Using only recursion
def fib_rec(n):
    # Base case
    if n == 1 or n == 2:
        return 1
    else:
        # Recursive case
        return fib_rec(n - 1) + fib_rec(n - 2)


# Using memoization
from functools import lru_cache


@lru_cache()
def fib_dyn(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fib_dyn(n - 2) + fib_dyn(n - 1)


# Using iterations
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a
