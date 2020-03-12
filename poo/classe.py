"""Syntaxe objet."""

# classe
class MaClasse:
    """Definition d'une classe."""
    x = 23
    y = x + 5 # x et y attributs de MaClasse

    def affiche(self):
        """Definition d'une methode."""
        self.z = 42    # attribut d'instance (i.e. de l'objet self)
        print(MaClasse.x, end=" ")
        print(MaClasse.y, end=" ")
        print(self.z) # ...mais pas un attribut d'instance


# programme principal --------------------------------------------
obj = MaClasse() # instancie un objet MaClasse()
obj.affiche() # a l'appel, self = obj. Idem : C.affiche(obj)
         
    
