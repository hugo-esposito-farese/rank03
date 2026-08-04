# =====================================================================
# EXERCICE : py_number_base_converter
#
# BUT : convertir un nombre écrit dans une base de départ (from_base)
# vers une autre base (to_base). Les bases vont de 2 à 36, avec les
# chiffres 0-9 puis les lettres A-Z pour représenter les valeurs 10 à
# 35. Si l'entrée est invalide, on renvoie "ERROR".
# =====================================================================

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"

    valeur = 0
    for char in number.upper():
        if char not in chiffres[:from_base]:
            return "ERROR"
        valeur = valeur * from_base + chiffres.index(char)

    if valeur == 0:
        return "0"

    resultat = ""
    while valeur > 0:
        reste = valeur % to_base
        resultat = chiffres[reste] + resultat
        valeur = valeur // to_base

    return resultat


if __name__ == "__main__":
    assert number_base_converter("1010", 2, 10) == "10"
    assert number_base_converter("FF", 16, 10) == "255"
    assert number_base_converter("255", 10, 16) == "FF"
    assert number_base_converter("123", 10, 2) == "1111011"
    assert number_base_converter("Z", 36, 10) == "35"
    assert number_base_converter("35", 10, 36) == "Z"
    assert number_base_converter("123", 1, 10) == "ERROR"
    assert number_base_converter("G", 16, 10) == "ERROR"
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def number_base_converter_commente(number: str, from_base: int, to_base: int) -> str:
    # "chiffres" est notre "alphabet" de symboles possibles, dans
    # l'ordre de leur valeur : '0' vaut 0, '1' vaut 1, ..., '9' vaut 9,
    # 'A' vaut 10, 'B' vaut 11, ..., 'Z' vaut 35.
    # La POSITION d'un caractère dans cette chaîne EST sa valeur :
    # chiffres.index('A') vaut 10, exactement ce qu'on veut.
    chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # On vérifie d'abord que les bases demandées sont raisonnables
    # (entre 2 et 36). Si ce n'est pas le cas, inutile d'aller plus
    # loin : on renvoie directement "ERROR".
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"

    # ---- ETAPE 1 : lire "number" (écrit en base from_base) et le
    #                transformer en un entier Python normal ----
    #
    # C'est la même logique qu'on utilise sans y penser en base 10 :
    # pour lire "123", on fait mentalement (1*10 + 2)*10 + 3 = 123.
    # On généralise cette idée à N'IMPORTE QUELLE base : à chaque
    # nouveau chiffre lu, on "décale" la valeur actuelle en la
    # multipliant par la base, puis on ajoute le chiffre suivant.
    valeur = 0
    for char in number.upper():
        # "chiffres[:from_base]" = la sous-chaîne des "from_base"
        # premiers caractères autorisés dans cette base. Par exemple,
        # en base 2, chiffres[:2] = "01" : seuls '0' et '1' sont
        # valides. Si "char" n'y figure pas, c'est un chiffre
        # impossible dans cette base -> "ERROR".
        if char not in chiffres[:from_base]:
            return "ERROR"

        # chiffres.index(char) donne la VALEUR numérique de ce
        # caractère (ex: index('F') = 15). On "décale" la valeur
        # actuelle vers la gauche (comme ajouter un chiffre en base
        # 10) en la multipliant par from_base, puis on ajoute la
        # valeur du nouveau chiffre.
        valeur = valeur * from_base + chiffres.index(char)

    # Schéma pour number="FF", from_base=16 :
    #   valeur = 0
    #   char='F' : valeur = 0*16 + 15 = 15
    #   char='F' : valeur = 15*16 + 15 = 255
    #   -> valeur (entier Python normal) = 255

    # ---- ETAPE 2 : transformer cet entier en une chaîne dans to_base ----
    if valeur == 0:
        return "0"  # cas particulier : 0 s'écrit "0" dans toutes les bases

    resultat = ""
    while valeur > 0:
        # Le RESTE de la division par to_base nous donne le chiffre
        # le PLUS A DROITE (le moins significatif) qu'il reste à
        # écrire. C'est la technique classique de changement de base :
        # on épluche le nombre par divisions successives.
        reste = valeur % to_base

        # chiffres[reste] transforme ce reste numérique (ex: 15) en
        # son symbole (ex: 'F'). On l'ajoute au DEBUT du résultat
        # (et pas à la fin !) car on trouve les chiffres du nombre
        # dans l'ordre INVERSE (du moins significatif au plus
        # significatif).
        resultat = chiffres[reste] + resultat

        # La division ENTIERE (//) retire le chiffre qu'on vient de
        # traiter : on continue avec ce qu'il reste à convertir.
        valeur = valeur // to_base

    # Schéma pour valeur=255, to_base=16 :
    #   255 % 16 = 15 ('F')  -> resultat = "F"     ; valeur = 255//16 = 15
    #   15  % 16 = 15 ('F')  -> resultat = "FF"     ; valeur = 15//16  = 0
    #   valeur == 0 -> on arrête -> résultat final = "FF"
    return resultat


assert number_base_converter_commente("FF", 16, 10) \
    == number_base_converter("FF", 16, 10)
