from ErzeugungsFunktionen import create_inner_array_from_board, create_board

def test_create_inner_array_from_board():
  assert(create_inner_array_from_board([], 5) == [' ', ' ', ' ', ' ', ' '])
  assert(create_inner_array_from_board([], 7) == [' ', ' ', ' ', ' ', ' ', ' ', ' '])
  assert(create_inner_array_from_board([], 3) == [' ', ' ', ' '])


def test_create_board():
  assert(create_board([], 3, 0) == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
  assert(create_board([], 4, 0) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']])


def run_tests_erzeugungsfunktionen():
  test_create_inner_array_from_board()
  test_create_board()