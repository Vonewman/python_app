from math import pi

# fonction qui calcule la surface
# d'un cercle de rayon r.


def surface_cercle(r):
    """
    Input: rayon r
    Output: surface du cercle
    """

    return r ** 2 * pi


if __name__ == "__main__":
    r = int(input())
    print(surface_cercle(r))
