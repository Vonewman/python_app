import numpy as np


def estimation_pi(n=10000):
    rnd = np.random.rand(1000, 2)
    norme = rnd[:, 0] ** 2 + rnd[:, 1] ** 2
    dedans = norme <= 1
    dedans_entier = dedans.astype(np.int64)
    return dedans_entier.sum() / dedans.shape[0] * 4


pi = estimation_pi()


def surface_cercle_pi(r, pi):
    return r ** 2 * pi


if __name__ == "__main__":
    print(surface_cercle_pi(5, pi))
