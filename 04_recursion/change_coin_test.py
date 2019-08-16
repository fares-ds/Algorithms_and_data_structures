from nose.tools import assert_equal


class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)
        print('Passed all tests.')


# Run Test

test = TestCoins()
test.check(rec_coin)
