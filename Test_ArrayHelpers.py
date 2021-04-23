from ArrayHelpers import contains_three, contains_one


def test_contains_three():
  l1 = ['X', 'X', 'X']
  assert(contains_three(l1, 'X', 0))
  l2 = ['X', 'X', 'O', 'X', 'X', 'X']
  assert(contains_three(l2, 'X', 0))
  l3 = ['X', 'X', 'O', 'O', 'X', 'X']
  assert(not contains_three(l3, 'X', 0))
  l4 = ['X', 'X', 'O', 'O', 'O', 'X']
  assert(contains_three(l4, 'O', 0))

def test_contains_one():
  l1 = ['X', 'X', 'O', 'X', 'X', 'X']
  l2 = ['X', 'X', 'O', ' ', 'X', 'X']
  l3 = [['X', 'X', 'O', 'O', 'X', 'X'], ['X', 'X', 'O', ' ', 'X', 'X'], ['X', 'X', 'O', ' ', 'X', 'X']]
  assert(not contains_one(l1, " "))
  assert(contains_one(l2, " "))
  assert(contains_one(l3, " "))


def run_tests_arrayhelpers():
  test_contains_three()
  test_contains_one()