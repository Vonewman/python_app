""" Implementation de la fonction puissance_rapide en 
    utilisant le principe de recurrence forte.
    Cette fonction calcule x a la puissance n.
"""
# Author: Abdoulaye Diallo

from sys import stdin

def puissance_rapide(x, n):
    if n == 0:
        return 1
    else:
        r = puissance_rapide(x, n // 2)
        if n % 2 == 0:
            return r * r
        else:
            return x * r * r


if __name__ == "__main__":
    x, n = map(int, stdin.readline().split())
    print("{}".format(puissance_rapide(x, n)))
