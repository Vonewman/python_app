""" Cette fonction prends en argument un entier n et 
    renvoie l'entier 2^n """

from sys import stdin

def puissance_2(n):
    "Fonction recursive"
    if n == 0:
        return 1
    else:
        x = puissance_2(n-1)
        return 2 * x

if __name__ == "__main__":
    n = int(stdin.readline())
    print("{}".format(puissance_2(n)))
