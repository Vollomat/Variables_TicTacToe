from GetterFunktionen import get_row, get_column, get_diag1, get_diag2

def any_of(a, f):
  ''' Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  return any(map(f,a))



def contains_one(l, c):
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
      return True
    else:
      return contains_three(tail, c)

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

def diag1_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links oben nach rechts unten geht, nur das Zeichen c enthält.'''
  return contains_three(get_diag1(a), c,0)

def diag2_contains_only(a, c):
  '''Liefert True, falls die Diagonale, die von links unten nach rechts oben geht, nur das Zeichen c enthält.'''
  return contains_three(get_diag2(a), c, 0)

def insertIntoList(l, rowInput, columnInput, c):
  l[rowInput][columnInput] = c
  return l
