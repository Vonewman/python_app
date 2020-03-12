n = 10

somme = 0

for i in range(1, n+1):
    somme = somme + i*i*i
print(somme)


def somme_entiers(n):
    "renvoie la somme des entiers naturels de 1 a n"
    return n*(n+1)/2

def somme_cubes(n):
    "renvoie la somme des entiers cubiques de 1 a n"
    somme = 0
    for i in range(1, n+1):
        somme = somme + i**3
    return somme

# Test
n = 12
if somme_cubes(n) == (somme_entiers(n)**2):
    print("Pour n =", n, "l'assertion est vraie.")
else:
    print("L'assertion est fausse!")
