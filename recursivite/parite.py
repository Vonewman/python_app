""" Ce programme determine la parite d'une fonction """
# Autheur: Abdoulaye Diallo

from sys import stdin

def pair(n):
    return (n == 0) or impair(n-1)

def impair(n):
    return (n != 0) and pair(n-1)

if __name__ == "__main__":
    n = int(stdin.readline())
    print("{}".format(impair(n)))
