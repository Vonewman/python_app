# Operations elementaires sur les matrices

def creer_matrice(n, p, v):
    """cree une nouvelle matrice de taille nxp.
    initialisee avec la valeur v"""
    return [[v] * p for i in range(n)]

def copie_matrice(m):
    """copie une matrice(mais pas ses elements)"""
    return [m[i][:] for i in range(len(m))]


def dimensions(m):
    """verifie que m est bien une matrice,
    et renvoie ses dimensions (lignes, colonnes)"""
    n = len(m)
    assert n > 0
    p = len(m[0])
    assert p > 0
    for r in m:
        assert len(r) == p
    return (n, p)

def transpose(m):
    """transpose une matrice"""
    n, p = dimensions(m)
    return [[m[i][j] for i in range(n)] for j in range(p)]


def multi_matrice(a, b):
    """multiplie deux matrices"""
    n, p = dimensions(a)
    q, r = dimensions(b)
    assert q == p
    c = creer_matrice(n, r, 0)
    for i in range(n):
        for j in range(r):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
                return c
