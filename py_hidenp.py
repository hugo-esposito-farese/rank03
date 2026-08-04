# =====================================================================
# EXERCICE : py_hidenp
#
# BUT : vérifier si "small" est une SOUS-SEQUENCE de "big".
# Une sous-séquence = toutes les lettres de "small" se retrouvent
# dans "big", DANS LE MÊME ORDRE, mais pas forcément côte à côte.
# Sensible à la casse.
# =====================================================================

def hidenp(small: str, big: str) -> bool:
    index_small = 0
    for char in big:
        if index_small < len(small) and char == small[index_small]:
            index_small += 1
    return index_small == len(small)


if __name__ == "__main__":
    assert hidenp("abc", "a1b2c3") is True
    assert hidenp("ace", "abcde") is True
    assert hidenp("aec", "abcde") is False
    assert hidenp("", "abc") is True
    assert hidenp("abc", "ab") is False
    assert hidenp("aaaa", "aaa") is False
    assert hidenp("sing", "subsequence testing") is True
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def hidenp_commente(small: str, big: str) -> bool:
    # "index_small" est un COMPTEUR/CURSEUR : il indique quelle
    # lettre de "small" on est en train de chercher en ce moment.
    # Au départ, on cherche la toute première lettre de "small"
    # (celle à l'index 0).
    index_small = 0

    # On parcourt "big" caractère par caractère.
    for char in big:

        # Deux conditions doivent être vraies en même temps :
        #  1) index_small < len(small) : il reste encore au moins une
        #     lettre de "small" à trouver (sinon on a déjà terminé,
        #     inutile de continuer à chercher).
        #  2) char == small[index_small] : le caractère actuel de
        #     "big" correspond EXACTEMENT à la lettre de "small" qu'on
        #     est en train de chercher.
        if index_small < len(small) and char == small[index_small]:
            # On a trouvé la lettre recherchée ! On avance le curseur
            # d'une case : la prochaine fois, on cherchera la lettre
            # SUIVANTE de "small".
            index_small += 1

        # Si la condition est fausse (mauvaise lettre, ou recherche
        # déjà terminée), on ne fait rien : on continue simplement à
        # avancer dans "big" au prochain tour de boucle.

    # Schéma pour hidenp("ace", "abcde") :
    #
    #   big:    a    b    c    d    e
    #   small:  a    -    c    -    e      (on cherche a, puis c, puis e)
    #   index_small:  0->1  1    1->2  2    2->3
    #
    # A la fin, si index_small est arrivé exactement à len(small),
    # cela veut dire qu'on a trouvé TOUTES les lettres de "small",
    # dans le bon ordre, quelque part dans "big". Sinon, il en
    # manquait au moins une.
    return index_small == len(small)


assert hidenp_commente("ace", "abcde") == hidenp("ace", "abcde")
