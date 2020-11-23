class Personne:
    """Classe representant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "James"

    def __str__(self):
        return "{0} {1}".format(self.prenom, self.nom)


class AgentSpecial(Personne):
    """Classe definissant un agent special.
    Elle herite de la classe Personne.
    """
    def __init__(self, nom, matricule):
        Personne.__init__(self, nom)
        self.matricule = matricule

    def __str__(self):
        return "Agent {0}, matricule {1}".format(self.nom,
                                                 self.matricule)


if __name__ == '__main__':
    agent = AgentSpecial("Bond", "18327-121")
    print(agent.nom)
    print(agent)
    print(agent.prenom)
