# Programme de calcul de 2^n

def puissance(n):
    c = n
    p = 1
    while c > 0:
        p = p * 2
        c = c - 1

    return p

n = int(input())
print(puissance(n))
