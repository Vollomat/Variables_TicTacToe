from TicTacToeHelpers import player_wins


def test_player_X_wins():
  a1 = [['X','X','X'],['O',' ','O'],['X','O',' ']]
  # [TODO] Mehr Tests für Diagonalen und Spalten hinzufügen.
  assert(player_wins(a1,'X'))

  a2 = [['X',' ',' '],['X','O','O'],['X','O',' ']]
  assert(not player_wins(a2,'X'))

  a3 = [['X',' ',' '],['O','O','O'],[' ','O','X']]
  assert(player_wins(a3,'O'))

  a4 = [[' ',' ','X'],['X','X','O'],['X','O',' ']]
  assert(not player_wins(a4,'X'))

def test_player_O_wins():
  #[TODO]
  pass # Platzhalter: Statement, das nichts macht