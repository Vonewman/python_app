""" Implementation d'une file LIFO avec une liste. """

def pile(*args):
    p = []
    if not args:
        return p
    for elem in args:
        p.append(elem)
    return list(p)

def empile(p, a):
    p.append(a)


def depile(p):
    try:
        return p.pop()
    except:
        print("La pile est vide !")


# programme principal
print(" Pile initiale ".center(50, '-'))
lifo = pile(5, 8, 9)
print("lifo :", lifo, '\n')

rien = input('"Entree"')

print(" Empilage ".center(50, '-'))
for i in range(5):
    depile(lifo)
    print("lifo :", lifo)


rien = input('"Entree"')


print(" Depilages ".center(50, '-'))
for i in range(5):
    depile(lifo)
    print("lifo :", lifo)
    
