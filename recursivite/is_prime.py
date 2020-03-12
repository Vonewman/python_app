""" La fonction is_prime determine si un entier n donne 
    en argument est premier ou pas. """

from sys import stdin

def is_prime(n):

    d = 2

    while(n % d != 0):
        d = d + 1

    if d == n:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(stdin.readline())
    print("{}".format(is_prime(n)))
