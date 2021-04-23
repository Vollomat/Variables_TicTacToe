from Test_GetterFunktionen import run_tests_getter_functions
from Test_ErzeugungsFunktionen import run_tests_erzeugungsfunktionen
from Test_TicTacToeHelpers import run_tests_tictactoehelpers
from Test_ArrayHelpers import run_tests_arrayhelpers

def run_tests():
  run_tests_arrayhelpers()
  run_tests_erzeugungsfunktionen()
  run_tests_getter_functions()
  run_tests_tictactoehelpers()
  print("--------Alle Tests funktionieren--------")



if __name__ == '__main__':
  run_tests()
