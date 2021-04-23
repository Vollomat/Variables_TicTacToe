def create_inner_array_from_board(list1D, userInputOfGameSize):
  ''' Erwartet ein leeres eindimensionales Array list1D und eine User-Eingabe von der Spielfeldgröße.
      Sobald die gewünschte Anzahl von Elementen im Array erzeugt wurde (User-Eingabe), wird das Array zurückgegeben. Diese Funktion wird immer von der Funktion create_final_board aufgerufen, sodass dieses 1-Dimensionale Array dem 2-Dimensionales Array angehängt wird.
  '''
  if(userInputOfGameSize < 1):
    return list1D
  
  list1D.append(" ") #Am Anfang ist das Spielfeld immer mit Leerzeichen besetzt und wird dann durch X oder O ersetzt
  return create_inner_array_from_board(list1D, userInputOfGameSize-1)



def create_final_board(list2D, gameSize, gameSize2):
  ''' Erwartet ein zweidimensionales Array list2D (mit der ersten Spalte von unserem Spiel) von der Funktion create_board und die doppelte User-Eingabe von der gewählten Spielfeldgröße. Die erste User-Eingabe wird für den rekursiven Aufruf bei jedem Durchgang runter gezählt und beendet schlussendlich den rekursiven Aufruf, wenn es den Wert von 3 unterschreitet. Die zweite User-Eingabe wird dazu verwendet, dass bei dem rekursiven Aufruf diese Variable sich nicht verändert und man somit immer die selbe Länge bei der append-Methode an das Array anhängt.
  Liefert das fertige zweidimensionale Array für unser variables Tic-Tac-Toe Spielfeld
  '''
  if(gameSize < 2):
    return list2D
  else:
    list2D.append(create_inner_array_from_board([], gameSize2))
  return create_final_board(list2D, gameSize-1, gameSize2)



def create_board(list1D, gameSize, counter):
  '''Diese Funktion dient dazu, dass in der 0. Zeile der 2D-Liste schon die richtige Anzahl an " " stehen. Ruft nachfolgend die Funtkion create_final_board auf.
  '''
  if(counter < gameSize):
    list1D.append(" ")
  else:
    list2D = [list1D]
    return create_final_board(list2D, gameSize, gameSize)
  return create_board(list1D, gameSize, counter+1)