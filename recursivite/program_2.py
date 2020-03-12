""" On considere le probleme consistant a calculer le 
    nombre de facons de construire une rangee de longueur n
    avec des briques de longueurs 2 et 3 
"""

from sys import stdin

def briques(n):
    assert n >= 1
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return briques(n-2) + briques(n-3)

if __name__ == "__main__":
    n = int(stdin.readline())
    print("{}".format(briques(n)))
