result1 = []

for i in "abc":
    for j in "de":
        result1.append(i+j)

print(" boucle for imbriquee ".center(50, '-'))
print(result1, "\n")

rien = input('"Entree"')

result2 = [i+j for i in "abc" for j in "de"]
print(" liste de comprehension ".center(50, "-"))
print(result2)
