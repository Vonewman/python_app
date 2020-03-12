# Program illustrant la division euclidienne avec la boucle while

n = int(input())
d = int(input())

q = 0
r = n
while r >= d:
    q = q + 1
    r = r - d


print(q)
