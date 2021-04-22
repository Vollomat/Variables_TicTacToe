def delimitation(s, userInputOfGameSize):
  '''Erwartet einen String (leer beim 1. Aufruf) und eine User-Eingabe von der Spielfeldgröße. Diese Funktion dient dazu, dass bei der Ausgabe sich die Felder des Tic-Tac-Toe-Spielfelds gut abgrenzen lassen. Die Funktion liefert den "Abgrenzungs-String" zurück, abhängig von der Spielfeldgröße.
  '''
  if(userInputOfGameSize<1):
    return s[1:]
  else:
    if(userInputOfGameSize==1):
      s += "--"
    else:
      s += "---+"
  return delimitation(s, userInputOfGameSize-1)

def board_to_string(b, userInputOfGameSize):
  '''Erwartet eine Liste b und eine User-Eingabe von der Spielfeldgröße. Die Methode erzeugt einen fertig aufgeteilten String, der dann im Form eines Spielfelds auf der Konsole ausgegeben werden kann mithilfe von print()
  '''
  lines = [" | ".join(line) for line in b]
  s = "\n" + delimitation("", userInputOfGameSize)+"\n"
  return s.join(lines)