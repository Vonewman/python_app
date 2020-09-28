def conjugation(verb):
    """
    Input: a verb(string)

    Output: conjugation of the verb
            in the present continuous
    """
    if verb[-1] == "e":
        verb = verb[:-1]

    return verb + "ing"

if __name__ == "__main__":
    verb = input()
    print("I am " +  conjugation(verb))
    print("You are " + conjugation(verb))
    print("He is " + conjugation(verb))
    print("We are " + conjugation(verb))
    print("You are " + conjugation(verb))
    print("They are " + conjugation(verb))

