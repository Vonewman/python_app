""" Liste en intension.
    Calcul d'une somme
"""

s1 = 0
for i in range(10):
    s1 = s1 + i

print(" somme (boucle for) ".center(50, '-'))
print("somme =", s1, '\n')

rien = input('"Entree"')

s2 = sum([i for i in range(10)])

print(" somme (liste en intension) ".center(50, '-'))
print("somme =", s2)
