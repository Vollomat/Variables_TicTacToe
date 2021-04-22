from ErzeugungsFunktionen import create_board
from AusgabeFunktionen import board_to_string
from ArrayHelpers import insertIntoList
from TicTacToeHelpers import player_X_wins,player_O_wins


def actual_player(counter):
  if(counter % 2 == 0):
    print("Spieler X ist dran")
    return "X"
  else:
    print("Spieler O ist dran")
    return "O"

def startOfTheGame():
  print("Willkommen beim dynamischen Tic-Tac-Toe!")
  print("Sie können sich im Folgenden eine Spielfeldgröße zwischen 3 bis 9 selbst aussuchen")
  playerinput = input("Geben Sie die gewünschte Spielfeldgröße ein: ")
  gameSize = int(playerinput)

  if(gameSize > 2 and gameSize < 10):
    mylist = create_board([], gameSize, 0)
    print(board_to_string(mylist, len(mylist)))
    moves(mylist, 0) #Spieler X darf beginnen2
  else:
    print("Ihre gewählte Spielgröße von " + playerinput + " verstößt gegen die Vorgaben. Versuchen Sie doch mal eine Spielgröße zwischen 3 bis 9!")
    startOfTheGame()

def moves(spielfeld, counter):
  
  player_at_the_moment = actual_player(counter)

  rowInput = int(input("An welcher freien Zeile wollen Sie Ihren nächsten Zug verwenden?: "))
  columnInput = int(input("An welcher freien Spalte wollen Sie Ihren nächsten Zug verwenden?: "))

  neuesSpielfeld = insertIntoArray(spielfeld, rowInput, columnInput, player_at_the_moment, counter)
  
  print(board_to_string(neuesSpielfeld, len(neuesSpielfeld)))

  if(player_X_wins(neuesSpielfeld)):
    print()
    print("---------------------------------------------------------------------")
    print("Der Spieler X hat gewonnen!!!")
    print("---------------------------------------------------------------------")
    return;
  if(player_O_wins(neuesSpielfeld)):
    print()
    print("---------------------------------------------------------------------")
    print("Der Spieler O hat gewonnen!!!")
    print("---------------------------------------------------------------------")
    return;
  
  
  moves(neuesSpielfeld, counter+1)


def insertIntoArray(spielfeld, rowInput, columnInput, c, counter):

  if(spielfeld[rowInput][columnInput] == " " and (0 < rowInput < len(spielfeld)) 
  and (0 < columnInput < len(spielfeld))):
    neuesSpielfeld = insertIntoList(spielfeld, rowInput, columnInput, c)
  else:
    print("Ihr Zug war ungültig. Als Strafe ist nun Spieler " + actual_player(counter+1) + " dran!")
    neuesSpielfeld = spielfeld
  
  return neuesSpielfeld
