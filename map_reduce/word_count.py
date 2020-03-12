from collections import defaultdict

def wordCount(text):
    " Compter le nombre d'occurence de chaque mot dans un ensemble de textes "

    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts

# Nous allons travailler sur deux extraits du texte de la chanson
# "Le Jour se leve" de Grand Corps Malade

D1 = {"./lot1.txt" : "jour leve notre grisaille"}
D2 = {"./lot2.txt" : "trottoir notre ruelle notre tour"}
D3 = {"./lot3.txt" : "jour leve notre envie vous"}
D4 = {"./lot4.txt" : "faire comprendre tous notre tour"}

# L'operation map
def map(key, value):
    intermediate = []
    for word in value.split():
        intermediate.append((word, 1))
    return intermediate

def reduce(key, values):
    result = 0
    for c in values:
        result = result + c
    return (key, result)
