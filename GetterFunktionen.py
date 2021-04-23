def get_row(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Zeile aus a.
  '''
  return a[i]


def get_column(a, i):
  '''Erwartet ein zweidimensionales Array a und eine Zahl i.
     Liefert die i-te Spalte aus a.
  '''
  return [a[j][i] for j in range(len(a))]


def get_diag1(a):
  '''Liefert die Diagonale in a, die von links oben nach rechts unten geht.'''
  return [a[i][i] for i in range(len(a))]


def get_diag2(a):
  '''Liefert die Diagonale in a, die von rechts oben nach links unten geht.'''
  return [a[i][-i-1] for i in range(len(a))]