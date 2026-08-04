# =====================================================================
# EXERCICE : py_twist_sequence
#
# BUT : faire tourner (rotation) un tableau vers la DROITE de k
# positions. k peut être plus grand que la taille du tableau (il faut
# alors "boucler").
# =====================================================================

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0:
        return []
    k = k % len(arr)
    if k == 0:
        return arr[:]
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    assert twist_sequence([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert twist_sequence([1, 2, 3], 1) == [3, 1, 2]
    assert twist_sequence([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert twist_sequence([1, 2, 3], 5) == [2, 3, 1]
    assert twist_sequence([], 3) == []
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def twist_sequence_commente(arr: list[int], k: int) -> list[int]:
    # Un tableau vide n'a rien à faire tourner : on renvoie
    # directement une liste vide, sans quoi la ligne "k % len(arr)"
    # plus bas ferait une division par zéro et ferait planter le
    # programme.
    if len(arr) == 0:
        return []

    # k peut être plus grand que la taille du tableau (ex: k=5 pour
    # un tableau de 3 éléments). Faire une rotation de 5 sur 3
    # éléments revient exactement au même que faire une rotation de
    # 5 % 3 = 2 (après une rotation complète de 3, on est revenu au
    # point de départ, donc seul le "reste" compte).
    # L'opérateur % (modulo) ramène ainsi k dans l'intervalle
    # [0, len(arr) - 1], peu importe sa valeur de départ.
    k = k % len(arr)

    if k == 0:
        # Aucune rotation à faire : on renvoie une COPIE du tableau
        # (arr[:] copie tous les éléments dans une nouvelle liste)
        # plutôt que "arr" lui-même, pour ne pas renvoyer l'objet
        # d'origine tel quel.
        return arr[:]

    # arr[-k:] veut dire : "les k DERNIERS éléments du tableau"
    # (l'index négatif compte à partir de la fin : -1 est le dernier
    # élément, -2 l'avant-dernier, etc.)
    #
    # arr[:-k] veut dire : "tous les éléments SAUF les k derniers"
    #
    # Une rotation à droite de k = "les k derniers éléments passent
    # devant, suivis de tout le reste" : on colle donc ces deux
    # morceaux dans cet ordre avec "+".
    #
    # Schéma pour arr = [1,2,3,4,5], k = 2 :
    #
    #   [1, 2, 3, 4, 5]
    #    \_______/ \__/
    #     arr[:-2]  arr[-2:]
    #     [1,2,3]   [4,5]
    #
    #   résultat = arr[-2:] + arr[:-2] = [4,5] + [1,2,3] = [4,5,1,2,3]
    return arr[-k:] + arr[:-k]


assert twist_sequence_commente([1, 2, 3, 4, 5], 2) == twist_sequence([1, 2, 3, 4, 5], 2)
