from AusgabeFunktionen import board_to_string
from ErzeugungsFunktionen import create_final_board
from GetterFunktionen import get_row
from GetterFunktionen import get_column
from GetterFunktionen import get_diag1
from GetterFunktionen import get_diag2


def any_of(a, f):
  ''' Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  return any(map(f,a))


def contains_three(l, c, sameCounter):
  '''Prüft, ob die Liste l mindestens 3x das Zeichen c enthält.
     Liefert False, wenn l nicht mindestens 3x dasselbe Zeichen c enthält.
     Bei einer leeren Liste wird False zurückgeben.
     Es wird eine Liste l erwartet, sowie das zu überprüfende Char c und ein Zähler, der hochzählt bei einem Hit zwischen Char c und einem Element innerhalb der Liste. Sobald aber das Char nicht dem Element in der Liste entspricht, wird der Zähler auf 0 wieder gesetzt. Sobald der Zähler größer als 2 ist (also sobald er 3 ist) wird True zurückgegeben. Falls der Zähler dies in der ganzen Liste l nie erreicht wird False zurückgegeben.
  '''
  if l == []:
    return False
  
  head, *tail = l

  if(head != []):
    if(head == c):
     sameCounter = sameCounter + 1
    else: 
      sameCounter = 0
    if(sameCounter > 2):
      return True
    else:
      return contains_three(tail, c, sameCounter)


def test_contains_three():
  l1 = ['X', 'X', 'X']
  assert(contains_three(l1, 'X', 0))
  l2 = ['X', 'X', 'O', 'X', 'X', 'X']
  assert(contains_three(l2, 'X', 0))
  l3 = ['X', 'X', 'O', 'O', 'X', 'X']
  assert(not contains_three(l3, 'X', 0))
  l4 = ['X', 'X', 'O', 'O', 'O', 'X']
  assert(contains_three(l4, 'O', 0))




def row_contains_only(a,i,c):
  '''Erwartet ein zweidimensionales Array a, eine Zahl i
     und ein Zeichen c.
     Liefert True, wenn die i-te Zeile nur das Zeichen c enthält.
  '''
  return contains_three(get_row(a,i),c,0)

def column_contains_only(a,i,c):
  '''Erwartet ein zweidimensionales Array a, eine Zahl i
     und ein Zeichen c.
     Liefert True, wenn die i-te Zeile nur das Zeichen c enthält.
  '''
  return contains_three(get_column(a,i),c,0)

def test_row_contains_only():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  assert(row_contains_only(a1,0,'X'))
  assert(not row_contains_only(a1,1,'X'))
  assert(not row_contains_only(a1,2,'X'))

def diag1_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links oben nach rechts unten geht, nur das Zeichen c enthält.'''
  return contains_three(get_diag1(a), c,0)

def diag2_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links unten nach rechts oben geht, nur das Zeichen c enthält.'''
  return contains_three(get_diag2(a), c, 0)

def player_wins(a,c):
  '''Erwartet ein zweidimensionales Array a.
     Liefert True, wenn eine Zeile, Spalte oder Diagonale nur c enthält.
  '''
  rows = [get_row(a,i) for i in range(len(a))]
  cols = [get_column(a,i) for i in range(len(a))]
  print("Die Länge vom Array beträgt: " + str(len(a)))
  for i in range(len(a)):
    print(i)
  diags = [get_diag1(a), get_diag2(a)]

  contains_three_c = lambda l: contains_three(l,c,0)
  return any_of(rows + cols + diags, contains_three_c)
  

def player_X_wins(a):
  return player_wins(a,'X')

def player_O_wins(a):
  return player_wins(a,'O')


def test_player_X_wins():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  # [TODO] Mehr Tests für Diagonalen und Spalten hinzufügen.
  assert(player_X_wins(a1))

  a2 = [['X',' ',' '],['X','O','O'],['X','O',' ']]
  assert(player_X_wins(a2))

  a3 = [['X',' ',' '],['X','X','O'],[' ','O','X']]
  assert(player_X_wins(a3))

  a4 = [[' ',' ','X'],['X','X','O'],['X','O',' ']]
  assert(player_X_wins(a4))

def test_player_O_wins():
  #[TODO]
  pass # Platzhalter: Statement, das nichts macht


def startOfTheGame():
  print("Willkommen beim dynamischen Tic-Tac-Toe!")
  print("Sie können sich im Folgenden eine Spielfeldgröße zwischen 3 bis 9 selbst aussuchen")
  playerinput = input("Geben Sie die gewünschte Spielfeldgröße ein: ")
  gameSize = int(playerinput)

  if(gameSize > 2 and gameSize < 10):
    mylist = create_final_board([[]],gameSize,gameSize)
    print("Zeile 197: Die Länge vom Array beträgt: " + str(len(mylist)))
    print(board_to_string(mylist, len(mylist)))
    moves(mylist, 0) #Spieler X darf beginnen
  else:
    print("Ihre gewählte Spielgröße von " + playerinput + " verstößt gegen die Vorgaben. Versuchen Sie doch mal eine Spielgröße zwischen 3 bis 9!")

def moves(spielfeld, counter):
  if(counter % 2 == 0):
    print("Spieler X ist dran")
  else:
    print("Spieler O ist dran")
  rowInput = int(input("An welcher freien Zeile wollen Sie Ihren nächsten Zug verwenden?: "))
  columnInput = int(input("An welcher freien Spalte wollen Sie Ihren nächsten Zug verwenden?: "))
  print("Der User hat in Zeile 208/209 eingegeben " + str(rowInput) + " | "+ str(columnInput))

  if(spielfeld[rowInput][columnInput] == " "):
    if(counter % 2 == 0):   #Also X
      neuesSpielfeld = insertIntoList(spielfeld, rowInput, columnInput, 'X')
    else: 
      neuesSpielfeld = insertIntoList(spielfeld, rowInput, columnInput, 'O')
  else:
    print("Diese Stelle ist schon mit " + spielfeld[rowInput][columnInput] + " belegt")
  print(board_to_string(neuesSpielfeld, len(neuesSpielfeld)))
  if(player_X_wins(neuesSpielfeld)):
    print("Der Spieler X hat gewonnen!!!")
    return;
  if(player_O_wins(neuesSpielfeld)):
    print("Der Spieler O hat gewonnen!!!")
    return;
  print("Bis hierhin geht es nicht")
  moves(neuesSpielfeld, counter+1)


def insertIntoList(l, rowInput, columnInput, c):
  l[rowInput][columnInput] = c
  return l

startOfTheGame()

test_contains_three()
test_row_contains_only()
test_player_X_wins()
test_player_O_wins()