from GetterFunktionen import get_column
from GetterFunktionen import get_row
from GetterFunktionen import get_diag1
from GetterFunktionen import get_diag2

def test_get_row():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_row(a1,0) == [1,2,3])
  a2 = [[1,2,3,4,5,6],[4,5,6,5],[7,8,9,1,2]]
  assert(get_row(a2,0) == [1,2,3,4,5,6])

def test_get_column():
  a1 = [[1,2,3],[4,5,6],[7,8,9]]
  assert(get_column(a1,0) == [1,4,7])

def test_get_diag1():
  #[TODO]
  return True

def test_get_diag2():
  #[TODO]
  return True