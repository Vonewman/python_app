""" Fonction recursive qui calcule la somme des <n>
    premiers entiers. Quelle est la complexite de cette fonction
"""

from sys import stdin

def somme(n):
    if n == 1:
        return 1
    else:
        return n + somme(n-1)


if __name__ == "__main__":
    n = int(stdin.readline())
    print("{}".format(somme(n)))
