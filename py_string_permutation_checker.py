# =====================================================================
# EXERCICE : py_string_permutation_checker
#
# BUT : vérifier si deux chaînes sont des PERMUTATIONS l'une de
# l'autre (mêmes caractères, mêmes quantités). Sensible à la casse :
# espaces et ponctuation comptent comme des caractères normaux.
# =====================================================================

def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    assert string_permutation_checker("abc", "bca") is True
    assert string_permutation_checker("abc", "def") is False
    assert string_permutation_checker("listen", "silent") is True
    assert string_permutation_checker("hello", "bello") is False
    assert string_permutation_checker("", "") is True
    assert string_permutation_checker("a", "") is False
    assert string_permutation_checker("Abc", "abc") is False
    assert string_permutation_checker("a gentleman", "elegant man") is True
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def string_permutation_checker_commente(s1: str, s2: str) -> bool:
    # Si les deux chaînes n'ont pas la même longueur, elles ne
    # peuvent absolument pas être des permutations l'une de l'autre
    # (une permutation ne fait que réarranger les caractères, elle
    # n'en ajoute ni n'en enlève). Autant s'arrêter tout de suite,
    # c'est aussi plus rapide que de trier pour rien.
    if len(s1) != len(s2):
        return False

    # Comme dans l'exercice "anagram", on compare les deux chaînes
    # triées lettre par lettre. sorted(s1) donne la liste des
    # caractères de s1 rangés par ordre alphabétique.
    #
    # DIFFERENCE avec "anagram" : ici on ne fait NI .lower() NI
    # suppression des espaces, car cet exercice est sensible à la
    # casse et compte espaces/ponctuation comme des caractères
    # normaux. C'est pour ça que string_permutation_checker("Abc", "abc")
    # renvoie False : 'A' (majuscule) et 'a' (minuscule) sont deux
    # caractères DIFFERENTS pour Python.
    return sorted(s1) == sorted(s2)


assert string_permutation_checker_commente("a gentleman", "elegant man") \
    == string_permutation_checker("a gentleman", "elegant man")
