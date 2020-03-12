u_0 = int(input())

u = u_0
n = 0
while u > 0:
    u = 0.5 * u - 3 * n
    n = n + 1
n = n - 1

print(u)
