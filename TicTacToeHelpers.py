from ArrayHelpers import any_of, contains_three, get_row, get_column, get_diag1, get_diag2, contains_one

def player_wins(a,c):
  '''Erwartet ein zweidimensionales Array a.
     Liefert True, wenn eine Zeile, Spalte oder Diagonale nur c enthält.
  '''
  rows = [get_row(a,i) for i in range(len(a))]
  cols = [get_column(a,i) for i in range(len(a))]
  diags = [get_diag1(a), get_diag2(a)]

  contains_three_c = lambda l: contains_three(l,c,0)
  return any_of(rows + cols + diags, contains_three_c)
  

def player_X_wins(a):
  return player_wins(a,'X')

def player_O_wins(a):
  return player_wins(a,'O')


def draw(a):
  '''Liefert True, falls das Spiel beendet und unentschieden ist.'''
  #[TODO] Prüfen, ob das Spielfeld voll ist (nur noch 'X' oder 'O').
  list = [get_row(a,i) for i in range(len(a))]
  return not contains_one(list," ")

def move_allowed(spielfeld, row, col):
  '''Prüft, ob an Stelle (row,col) ein Zug gemacht werden darf.'''
  return row in range(len(spielfeld)) and col in range(len(spielfeld[row])) and spielfeld[row][col] == " "

def game_finished(spielfeld):
  '''Liefert True, falls das Spiel zu Ende ist.'''
  return player_X_wins(spielfeld) or player_O_wins(spielfeld) or draw(spielfeld)