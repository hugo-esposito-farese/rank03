# =====================================================================
# EXERCICE : py_shadow_merge
#
# BUT : fusionner deux listes DEJA TRIEES en une seule liste triée.
# =====================================================================

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    resultat = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            resultat.append(list1[i])
            i += 1
        else:
            resultat.append(list2[j])
            j += 1
    resultat += list1[i:]
    resultat += list2[j:]
    return resultat


if __name__ == "__main__":
    assert shadow_merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert shadow_merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert shadow_merge([1], [2, 3, 4]) == [1, 2, 3, 4]
    assert shadow_merge([], [1, 2, 3]) == [1, 2, 3]
    assert shadow_merge([1, 1, 2], [1, 3, 3]) == [1, 1, 1, 2, 3, 3]
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def shadow_merge_commente(list1: list[int], list2: list[int]) -> list[int]:
    # "resultat" va accueillir la liste finale fusionnée et triée.
    resultat = []

    # "i" et "j" sont deux CURSEURS séparés : "i" indique où on en
    # est dans list1, "j" indique où on en est dans list2. C'est la
    # technique dite "à deux pointeurs".
    i = 0
    j = 0

    # Tant qu'il reste au moins un élément non traité DANS LES DEUX
    # listes, on continue à comparer.
    while i < len(list1) and j < len(list2):
        # Comme list1 et list2 sont DEJA triées, on sait que
        # list1[i] est le plus petit élément RESTANT de list1, et
        # list2[j] est le plus petit élément RESTANT de list2.
        # Il suffit donc de comparer CES DEUX-LA pour savoir lequel
        # doit passer en premier dans le résultat.
        if list1[i] <= list2[j]:
            resultat.append(list1[i])
            i += 1  # on avance seulement dans list1, celle qu'on a utilisée
        else:
            resultat.append(list2[j])
            j += 1  # on avance seulement dans list2, celle qu'on a utilisée

    # A la sortie de la boucle "while", UNE des deux listes est
    # entièrement épuisée (son curseur a atteint sa longueur), mais
    # il peut rester des éléments dans l'AUTRE liste. Comme cette
    # liste restante est déjà triée, on peut la coller directement à
    # la fin du résultat, sans rien recalculer.
    #
    # list1[i:] veut dire "tous les éléments de list1 à partir de
    # l'index i jusqu'à la fin". Si list1 est déjà épuisée (i == len),
    # list1[i:] vaut simplement [] (une liste vide), donc ça ne
    # rajoute rien : ces deux lignes fonctionnent dans tous les cas,
    # sans avoir besoin de "if".
    resultat += list1[i:]
    resultat += list2[j:]

    # Schéma pour shadow_merge([1,3,5], [2,4,6]) :
    #   i=0,j=0 : list1[0]=1 <= list2[0]=2 -> +1, i=1   resultat=[1]
    #   i=1,j=0 : list1[1]=3 <= list2[0]=2 ? non -> +2, j=1  resultat=[1,2]
    #   i=1,j=1 : list1[1]=3 <= list2[1]=4 -> +3, i=2   resultat=[1,2,3]
    #   i=2,j=1 : list1[2]=5 <= list2[1]=4 ? non -> +4, j=2  resultat=[1,2,3,4]
    #   i=2,j=2 : list1[2]=5 <= list2[2]=6 -> +5, i=3   resultat=[1,2,3,4,5]
    #   i=3 == len(list1) -> la boucle while s'arrête
    #   list1[3:] = []  (rien à ajouter)
    #   list2[2:] = [6] -> resultat=[1,2,3,4,5,6]
    return resultat


assert shadow_merge_commente([1, 3, 5], [2, 4, 6]) == shadow_merge([1, 3, 5], [2, 4, 6])
