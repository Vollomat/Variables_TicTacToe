from GetterFunktionen import get_row, get_column, get_diag1, get_diag2
from functools import reduce

def any_of(a, f):
  ''' Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  return any(map(f,a))


def contains_one(l, c):
  '''Prüft, ob die Liste l mindestens 1x das Zeichen c enthält.
     Liefert False, wenn l nicht mindestens 1x das Zeichen c enthält.
     Die Liste wird zuerst zu einer 1D Liste umgewandelt
     Es wird eine 2D-Liste l (das Spielfeld) erwartet, sowie das zu überprüfende Char c (immer für die Funktion draw verwendet, um zu schauen ob noch mindestens ein " " vorhanden ist auf dem Spielfeld)
  '''
  list1D = reduce(lambda x,y :x+y ,l)

  return c in list1D


def contains_three(l, c, sameCounter):
  '''Prüft, ob die Liste l mindestens 3x das Zeichen c enthält.
     Liefert False, wenn l nicht mindestens 3x dasselbe Zeichen c enthält.
     Bei einer leeren Liste wird False zurückgeben.
     Es wird eine Liste l erwartet, sowie das zu überprüfende Char c und ein Zähler, der hochzählt bei einem Hit zwischen Char c und einem Element innerhalb der Liste. Sobald aber das Char nicht dem Element in der Liste entspricht, wird der Zähler auf 0 wieder gesetzt. Sobald der Zähler größer als 2 ist (also sobald er 3 ist) wird True zurückgegeben. Falls der Zähler dies in der ganzen Liste l nie erreicht wird False zurückgegeben. Rekursiv.
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


def insertIntoList(l, rowInput, columnInput, c):
  '''In einer 2D-Liste (Spielfeld) wird an der Stelle rowInput|rowInput der char c eingefügt (aktueller Spieler).
  '''
  l[rowInput][columnInput] = c
  return l
