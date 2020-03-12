# -*- coding:Utf-8 -*-

# count the occurences of a given character in a string 

def count(string, ch):
    "find the index of the character (ch) in the string (string)"
    i, nb_count = 0, 0             # initialisation
    while i < len(string):
        if string[i] == ch:
            nb_count = nb_count + 1 
        i = i + 1
    return nb_count

def countWord(string):
    # count the number of words in the string (string)
    if len(string) == 0:
        return 0
    nb_word = 1
    for c in string:
        if c == " ":
            nb_word = nb_word + 1
    return nb_word

# Test
if __name__ == '__main__':
    print(countWord("Small streams make the big rivers"))
