from GetterFunktionen import get_column,get_row,get_diag1,get_diag2

def test_get_row():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_row(a1,0) == [1,2,3])
  a2 = [[1,2,3,4,5,6],[4,5,6,5],[7,8,9,1,2]]
  assert(get_row(a2,0) == [1,2,3,4,5,6])

def test_get_column():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  a2 = [[1,2,3,4,5,6],[4,5,6,5],[7,8,9,1,2]]
  assert(get_column(a1,0) == [1,4,7])
  assert(get_column(a2,3) == [4,5,1])

def test_get_diag1():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  a2 = [[1,2,3,4,5],[4,5,6,4,5],[7,8,9,4,5],[7,8,9,4,5],[7,8,9,4,5]]
  assert(get_diag1(a1) == [1,5,9])
  assert(get_diag1(a2) == [1,5,9,4,5])

def test_get_diag2():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  a2 = [[1,2,3,4,5],[4,5,6,4,5],[7,8,9,4,5],[7,8,9,4,5],[7,8,9,4,5]]
  assert(get_diag2(a1) == [7,5,3])
  assert(get_diag2(a2) == [7,8,9,4,5])

def run_tests_getter_functions():
  test_get_row()
  test_get_column()
  test_get_diag1()
  test_get_diag2()