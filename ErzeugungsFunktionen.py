def create_board(gameSize):
  '''Diese Funktion dient dazu, dass in der 0. Zeile der 2D-Liste schon die richtige Anzahl an " " stehen. Ruft nachfolgend die Funtkion create_final_board auf.
  '''
  return [[" " for j in range(gameSize)] for i in range(gameSize)]