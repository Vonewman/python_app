import numpy as np

# Tri aleatoire


def tri_alea(T, n=1000):
    T = T.copy()
    for i in range(0, n):
        i, j = np.random.randint(0, len(T), 2)
        if i < j and T[i] > T[j]:
            T[i], T[j] = T[j], T[i]

    return T


# Tri aleatoire au cas ou i > j


def tri_alea2(T, n=1000):
    T = T.copy()
    for i in range(0, n):
        i = np.random.randint(0, len(T) - 1)
        j = np.random.randint(i + 1, len(T))
        if T[i] > T[j]:
            T[i], T[j] = T[j], T[i]

    return T


if __name__ == '__main__':
    tableau = [1, 3, 4, 5, 3, 2, 7, 11, 10, 9, 8, 0]
    print(tri_alea2(tableau))
