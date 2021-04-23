from TicTacToeHelpers import player_wins,draw,move_allowed

def test_player_wins():
  a1 = [['X','X','X'],['O',' ','O'],['X','O',' ']]
  assert(player_wins(a1,'X'))

  a2 = [['X',' ',' '],['X','O','O'],['X','O',' ']]
  assert(player_wins(a2,'X'))

  a3 = [['X',' ',' '],['O','O','O'],[' ','O','X']]
  assert(player_wins(a3,'O'))

  a4 = [[' ',' ','X'],['X','X','O'],['X','O',' ']]
  assert(player_wins(a4,'X'))


def test_draw():
  a1 = [['X','X','X'],['O',' ','O'],['X','O',' ']]
  assert(not draw(a1)) #nicht alles belegt
  a1 = [['O','X','O'],['X','O','O'],['X','O','X']]
  assert(draw(a1))


def test_move_allowed():
  a1 = [['X','X','X'],['O',' ','O'],['X','O',' ']]
  assert(move_allowed(a1,1,1))
  assert(move_allowed(a1,2,2))
  assert(not move_allowed(a1,4,0)) #außerhalb des Spielfelds
  assert(not move_allowed(a1,0,4)) #außerhalb des Spielfelds
  assert(not move_allowed(a1,0,0)) #weil schon belegt


def run_tests_tictactoehelpers():
  test_player_wins()
  test_draw()
  test_move_allowed()