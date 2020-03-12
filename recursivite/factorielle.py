""" Implementation recursive de la fonction factorielle """
# Author: ABdoulaye Diallo

def factorielle(n):
    assert n >= 0
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

# programme principal

n = int(input())
print("{}".format(factorielle(n)))
