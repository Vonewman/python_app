"""Classe avec constructeur."""

class Vecteur2D:
    """Les Vecteurs plans."""

    def __init__(self, x0=0, y0=0):
        """Constructeur avec parametres par defaut."""
        self.x = x0
        self.y = y0


    def __add__(self, autre):
        """ Addition vectorielle. """
        return Vecteur2D(self.x+autre.x, self.y+autre.y)

    def __str__(self):
        """ Affichage d'un Vecteur2D. """

        return "Vecteur({:g}, {:g})".format(self.x, self.y)

# programme principal ---------------------------------------
v1, v2 = Vecteur2D(1.2, 2.3), Vecteur2D(3.4, 4.5)

print(v1)
print(v2)
print(v1 + v2)
