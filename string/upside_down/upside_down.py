def upsidedown(word):
    """
    Input: a word (a string)

    Output: the word backwards
    """

    return word[::-1]

if __name__ == "__main__":
    word = input()
    print("{}".format(upsidedown(word)))
