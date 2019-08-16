from functools import lru_cache


# Using recursion
def rec_coin(target, coins):
    # INPUT: Target change amount and list of coin values
    # OUTPUT: Minimum coins needed to make change
    #
    # Note, this solution is not optimized.

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + rec_coin(target - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


# Solving the same problem using dynamic programing
@lru_cache(maxsize=1000)
def rec_coin_dyn(target, coins):
    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + rec_coin_dyn(target - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


print(rec_coin_dyn(63, (1, 5, 10, 25, 50)))
print(rec_coin_dyn.cache_info())
