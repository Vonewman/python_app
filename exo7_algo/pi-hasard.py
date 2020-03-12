import random

"""Ce programme calcul les premieres decimales de pi 
par la methode de Monte Carlo, c.a.d avec l'aide du hasard.
On considere le carre de cote 1, le cercle de rayon 1 centre
a l'origine, d'equation x**2 + y**2 = 1, et la portion de disque dans
le carre."""

Tir = 0         # NUmero du Tir
NbTirDansLeDisque = 0     # NOmbre de tir dans le disque

while (Tir < 1000):
    Tir = Tir + 1
    # On tir au hasard un point (x, y) dans [0,1] x [0, 1]
    x = random.random()
    y = random.random()
    if (x*x+y*y <= 1):   # On est dans le disque
        NbTirDansLeDisque = NbTirDansLeDisque + 1


MonPi  = 4*NbTirDansLeDisque / Tir
print("Valeur experimentale de Pi: %0.3f" %MonPi)

