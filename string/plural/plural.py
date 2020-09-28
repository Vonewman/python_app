def plural(word):
    """
    Input: a string called word

    Output: the plural of word
    """

    string = ''
    if word[-1] == 'y':
        word = word[:-1]
        string = word + "ies"
    elif word[-1] == 's':
        string = word + "es"
    else:
        string = word + 's'

    return string

# Test
if __name__ == "__main__":
    assert(plural("city") == "cities")
    assert(plural("bus")  == "buses")
    assert(plural("cat") == "cats")
    assert(plural("plural") == "plurals")
