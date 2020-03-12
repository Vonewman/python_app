""" Les dictionnaires en Python

    Extraire les mots d'un texte, et leur frequence
"""

def compterMots(texte):
    dict = {}
    listeMots = texte.split()

    for mot in listeMots:
        if mot in dict:
            dict[mot] = dict[mot] + 1
        else:
            dict[mot] = 1
    return dict

res = compterMots("Ala Met Asn Glu Met Cys Asn Glu Hou Met Gli Asn Asn")


for c in res.keys():
    print(c, "-->", res[c])

