################################
# Bitcoin
################################

################################
# Activity 1 - Proof of work
################################

p = 15486869

from time import *

# Question 1

def verification(x, y):
    xsquare = (x**2) % p
    if xsquare == y:
        return True
    else:
        return False

# Test
print("--- Verification x^2 = y modulo p ---")

start_chrono = time()

x = 6543210
y = 8371779
print(verification(x, y))

end_chrono = time()
total_chrono = end_chrono - start_chrono
print("Time of computation (in seconds):", total_chrono)

# Question 2

def square_root(y):
    for x in range(p):
        res = (x ** 2 - y) % p
        if res == 0:
            return x
    return None

# Test
print("--- Search for x st x^2 = y modulo p ---")

start_chrono = time()

y = 8371779
x = square_root(y)
print(x, (x**2-y)%p)

end_chrono = time()
total_chrono = end_chrono - start_chrono
print("Time of computation (in seconds):", total_chrono)
