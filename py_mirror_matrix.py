# =====================================================================
# EXERCICE : py_mirror_matrix
#
# BUT : on reçoit une matrice 2D (une liste de listes de nombres), et
# on doit renvoyer une NOUVELLE matrice où CHAQUE LIGNE est inversée
# (comme un effet miroir horizontal).
# =====================================================================

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    resultat = []
    for ligne in matrix:
        resultat.append(ligne[::-1])
    return resultat


if __name__ == "__main__":
    assert mirror_matrix([[1, 2, 3], [4, 5, 6]]) == [[3, 2, 1], [6, 5, 4]]
    assert mirror_matrix([[1, 2], [3, 4], [5, 6]]) == [[2, 1], [4, 3], [6, 5]]
    assert mirror_matrix([[7]]) == [[7]]
    assert mirror_matrix([[1, 2, 3, 4]]) == [[4, 3, 2, 1]]
    assert mirror_matrix([[-1, -2], [-3, -4]]) == [[-2, -1], [-4, -3]]
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def mirror_matrix_commente(matrix: list[list[int]]) -> list[list[int]]:
    # "matrix" est une LISTE DE LISTES : chaque élément de "matrix"
    # est lui-même une liste (une "ligne"). Exemple pour [[1,2,3],[4,5,6]] :
    #   matrix[0] -> [1, 2, 3]   (première ligne)
    #   matrix[1] -> [4, 5, 6]   (deuxième ligne)
    #
    # "resultat" va accueillir la nouvelle matrice, construite ligne
    # par ligne. On part d'une liste vide.
    resultat = []

    for ligne in matrix:
        # A chaque tour de boucle, "ligne" contient UNE liste complète
        # (une ligne entière de la matrice), par exemple [1, 2, 3].
        #
        # ligne[::-1] crée une NOUVELLE liste avec les mêmes éléments
        # mais dans l'ordre inverse : [1, 2, 3] devient [3, 2, 1].
        # Important : ça ne modifie PAS "ligne" d'origine, ça en crée
        # une copie inversée -> c'est pour ça qu'on ne touche jamais à
        # la matrice reçue en paramètre.
        ligne_inversee = ligne[::-1]

        # On ajoute cette ligne inversée à notre résultat, à la fin.
        resultat.append(ligne_inversee)

    # Schéma pour matrix = [[1,2,3],[4,5,6]] :
    #
    #   [1, 2, 3]  --miroir-->  [3, 2, 1]   -> devient resultat[0]
    #   [4, 5, 6]  --miroir-->  [6, 5, 4]   -> devient resultat[1]
    #
    #   resultat final = [[3, 2, 1], [6, 5, 4]]
    return resultat


assert mirror_matrix_commente([[1, 2, 3], [4, 5, 6]]) \
    == mirror_matrix([[1, 2, 3], [4, 5, 6]])
