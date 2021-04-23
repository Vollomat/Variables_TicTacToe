from ArrayHelpers import contains_three, row_contains_only, column_contains_only


def test_contains_three():
  l1 = ['X', 'X', 'X']
  assert(contains_three(l1, 'X', 0))
  l2 = ['X', 'X', 'O', 'X', 'X', 'X']
  assert(contains_three(l2, 'X', 0))
  l3 = ['X', 'X', 'O', 'O', 'X', 'X']
  assert(not contains_three(l3, 'X', 0))
  l4 = ['X', 'X', 'O', 'O', 'O', 'X']
  assert(contains_three(l4, 'O', 0))

def test_row_contains_only():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  assert(row_contains_only(a1,0,'X'))
  assert(not row_contains_only(a1,1,'X'))
  assert(not row_contains_only(a1,2,'X'))

