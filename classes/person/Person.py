class Person:
    """Classe definissant une personne caracterisee par :
- son nom
- son prenom
- son lieu de residence """

    def __init__(self):
        "Methode constructeur"
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 33
        self.lieu_residence = "Paris"


if __name__ == "__main__":
    jean = Person()
    jean.nom
    jean.prenom
    jean.lieu_residence
