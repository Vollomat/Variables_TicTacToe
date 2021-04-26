from ErzeugungsFunktionen import create_board

def test_create_board():
  assert(create_board(3) == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
  assert(create_board(4) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']])


def run_tests_erzeugungsfunktionen():
  test_create_board()