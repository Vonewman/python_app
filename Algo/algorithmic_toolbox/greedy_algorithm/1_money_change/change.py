import sys


def get_change(m):
    """ 
    Money change 
    """
    return (m//10) + ((m % 10)//5) + (m % 5)


if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
