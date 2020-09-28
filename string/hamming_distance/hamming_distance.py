def hamming_distance(word1, word2):
    """
    Input: two words(strings)

    Ouput: the Hamming distance(an integer)
    """

    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance


if __name__ == "__main__":
    word1 = input()
    word2 = input()
    print("{}".format(hamming_distance(word1, word2)))

