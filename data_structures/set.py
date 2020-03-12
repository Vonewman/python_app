""" Definir les ensembles (sets): X = {a, b, c} et 
    Y = {s, b, d} et afficher les resultats suivants:
"""

X = set('abcd')
Y = set('sbd')

# - les ensembles initiaux
print("ensemble de depart ".center(50, '-'))
print("X = ", X)
print("Y = ", Y)

rien = input('"Entree"')

# le test d'appartenance de l'element 'c' a X et 'a' a Y
print(" appartenance ".center(50, '-'))
print("'c' appartient a X ?", 'c' in X)
print("'a' appartient a Y ?", 'a' in Y)

rien = input('"Entree"')

# les ensembles X-Y et Y-X
print(" difference ".center(50, '-'))
print("X - Y :", X - Y)
print("Y - X :", Y - X)

rien = input('"Entree"')

# union X U Y
print(" union ".center(50, '-'))
print("X | Y: ", X | Y)

rien = input('"Entree"')

# intersection
print(" intersection ".center(50, '-'))
print("X & Y :", X & Y)



