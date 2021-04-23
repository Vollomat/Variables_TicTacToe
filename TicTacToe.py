from ErzeugungsFunktionen import create_board
from AusgabeFunktionen import board_to_string
from ArrayHelpers import insertIntoList
from TicTacToeHelpers import is_game_over, move_allowed


def actual_player(counter):
  '''Erwartet den aktuellen Counter von moves und gibt den aktuellen Spieler als Character zurück (X oder O)
  '''
  if(counter % 2 == 0):
    print("Spieler X ist dran")
    return 'X'
  else:
    print("Spieler O ist dran")
    return 'O'



def startOfTheGame():
  '''Lässt das Tic-Tac-Toe Spiel beginnen! Fragt den User nach der gewünschten Spielfeldgröße und überprüft ihn auf Gültigkeit. Malt das Spielfeld über die Funktion board_to_string zum ersten Mal auf zum grafischen Überblick für den User und startet die moves Funktion, welche einer GameLoop-Funktion entspricht. Bei einer ungültigen Eingabe wird der User darauf hingewiesen und darf nochmal sein Glück versuchen.
  '''
  print("Willkommen beim dynamischen Tic-Tac-Toe!")
  print("Sie können sich im Folgenden eine Spielfeldgröße zwischen 3 bis 9 selbst aussuchen")
  playerinput = input("Geben Sie die gewünschte Spielfeldgröße ein: ")
  
  try: gameSize = int(playerinput)
  except ValueError: print("Dies ist keine Zahl!"), startOfTheGame()

  if(gameSize > 2 and gameSize < 10):
    mylist = create_board([], gameSize, 0)
    print(board_to_string(mylist, len(mylist)))
    moves(mylist, 0) #Spieler X darf beginnen2
  else:
    print("Ihre gewählte Spielgröße von " + playerinput + " verstößt gegen die Vorgaben. Versuchen Sie doch mal eine Spielgröße zwischen 3 bis 9!")
    startOfTheGame()



def moves(spielfeld, counter):
  '''Erwartet ein Spielfeld und den aktuellen Counter. Es handelt sich hier um den GameLoop. Der User wird immer abgefragt, wo er nun als nächstes seinen Zug platzieren will. Wenn dies gültig ist, dann wird der Zug in einem neuen Spielfeld platziert um Seiteneffekte zu vermeiden. Nach jedem Zug wird kontrolliert, ob wer gewonnen hat und ob ein Unentschieden vorliegt. Dann ist das Spiel beendet, sonst rekursiver Aufruf der Methode bis einer gewinnt oder es unentschieden ausgeht. Außerdem wird nach jedem Zug das Spielfeld in der Konsole ausgegeben.
  '''
  player_at_the_moment = actual_player(counter)

  rowInput = int(input("An welcher freien Zeile wollen Sie Ihren nächsten Zug verwenden?: "))
  columnInput = int(input("An welcher freien Spalte wollen Sie Ihren nächsten Zug verwenden?: "))

  neuesSpielfeld = insertIntoArray(spielfeld, rowInput, columnInput, player_at_the_moment, counter)
  
  print(board_to_string(neuesSpielfeld, len(neuesSpielfeld)))

  if(is_game_over(neuesSpielfeld)):
    return
  
  moves(neuesSpielfeld, counter+1)



def insertIntoArray(spielfeld, rowInput, columnInput, player_at_the_moment, counter):

  if(move_allowed(spielfeld, rowInput, columnInput)):
    neuesSpielfeld = insertIntoList(spielfeld, rowInput, columnInput, player_at_the_moment)
  else:
    print("Ihr Zug war ungültig. Als Strafe ist nun Spieler " + actual_player(counter+1) + " dran!")
    neuesSpielfeld = spielfeld
  
  return neuesSpielfeld
