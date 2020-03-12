result1 = []

for i in range(6):
    result1.append(i+3)

print(" boucle for ".center(50, '-'))
print(result1, '\n')

rien = input('"Entree"')

result2 = [i+3 for i in range(6)]

print(" liste de comprehension ".center(50, '-'))
print(result2)
