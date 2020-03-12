"""Implementation de la fonction puissance, 
   qui calcule x a la puissance n.
 """

from sys import stdin

def  puissance(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * puissance(x, n-1)

# programme principal

if __name__ == "__main__":
    x, n = map(int, stdin.readline().split())
    print(puissance(x, n))

