def create_inner_array_from_board(list1D, userInputOfGameSize):
  ''' Erwartet ein Array list1D und eine User-Eingabe von der Spielfeldgröße.
      Sobald die gewünschte Anzahl von Elementen im Array erzeugt wurde (User-Eingabe), wird das Array zurück gegeben. Diese Funktion wird immer von der Funktion ,,create_final_board" aufgerufen, sodass dieses 1-Dimensionale Array dem 2-Dimensionales Array angehängt wird.
  '''
  if(userInputOfGameSize < 1):
    return list1D
  
  list1D.append(" ") #Am Anfang ist das Spielfeld immer mit Leerzeichen besetzt und wird dann durch X oder O ersetzt
  return create_inner_array_from_board(list1D, userInputOfGameSize-1)

def create_final_board(list2D, userInputOfGameSize, userInputOfGameSize2):
  ''' Erwartet ein zweidimensionales Array list2D (leer) und die doppelte User-Eingabe von der gewählten Spielfeldgröße. Die erste User-Eingabe wird für den rekursiven Aufruf bei jedem Durchgang runter gezählt und beendet schlussendlich den rekursiven Aufruf wenn es den Wert von 1 unterschreitet. Die zweite User-Eingabe wird dazu verwendet, dass bei dem rekursiven Aufruf diese Variable sich nicht verändert und man somit immer die selbe      Länge bei der append-Funktion an das Array anhängt.
  Liefert das fertige zweidimensionale Array für unser Tic-Tac-Toe Spielfeld
  '''
  if(userInputOfGameSize < 2):
    return list2D
  else:
    list2D.append(create_inner_array_from_board([], userInputOfGameSize2))
  return create_final_board(list2D, userInputOfGameSize-1, userInputOfGameSize2)

def erzeugeEindimensionalesArray(list1D, gameSize, counter):
  if(counter < gameSize):
    list1D.append(" ")
  else:
    return [list1D]
  return erzeugeEindimensionalesArray(list1D, gameSize, counter+1)