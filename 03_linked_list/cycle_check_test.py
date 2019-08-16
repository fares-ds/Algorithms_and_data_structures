from nose.tools import assert_equal

# CREATE IN CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = b  # Cycle Here!

# CREATE CYCLE LIST
i = Node(1)
j = Node(2)
k = Node(3)

i.next_node = j
j.next_node = k
k.next_node = i

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z


#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(i), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")


# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
