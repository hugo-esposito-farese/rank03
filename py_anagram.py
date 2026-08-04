# =====================================================================
# EXERCICE : py_anagram
#
# BUT : vérifier si deux chaînes sont des ANAGRAMMES, c'est-à-dire
# qu'elles contiennent exactement les mêmes lettres, avec les mêmes
# quantités, en ignorant la casse et les espaces.
# =====================================================================

def anagram(s1: str, s2: str) -> bool:
    nettoye1 = s1.lower().replace(" ", "")
    nettoye2 = s2.lower().replace(" ", "")
    return sorted(nettoye1) == sorted(nettoye2)


if __name__ == "__main__":
    assert anagram("listen", "silent") is True
    assert anagram("Triangle", "Integral") is True
    assert anagram("Dormitory", "Dirty Room") is True
    assert anagram("hello", "world") is False
    assert anagram("", "") is True
    assert anagram("abc", "abcc") is False
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def anagram_commente(s1: str, s2: str) -> bool:
    # On "nettoie" chaque chaîne pour ignorer les différences qui ne
    # doivent pas compter :
    #  - .lower() met tout en minuscule ("Room" -> "room")
    #  - .replace(" ", "") retire tous les espaces (le 2e argument ""
    #    est une chaîne vide : on remplace chaque espace par "rien")
    nettoye1 = s1.lower().replace(" ", "")
    nettoye2 = s2.lower().replace(" ", "")

    # sorted(une_chaine) prend une chaîne de caractères et renvoie une
    # LISTE de ces caractères, triés dans l'ordre alphabétique.
    # Exemple : sorted("dormitory") -> ['d','i','m','o','o','r','r','t','y']
    #
    # L'idée clé : deux mots sont des anagrammes si et seulement si
    # ils contiennent EXACTEMENT les mêmes lettres (juste dans un
    # ordre différent). Or, si on trie deux listes de lettres
    # identiques, on obtient forcément deux listes IDENTIQUES,
    # peu importe l'ordre de départ. On peut donc simplement comparer
    # les deux versions triées avec "==".
    #
    # Schéma pour "Dormitory" et "Dirty Room" :
    #   nettoye1 = "dormitory" -> trié -> [d,i,m,o,o,r,r,t,y]
    #   nettoye2 = "dirtyroom" -> trié -> [d,i,m,o,o,r,r,t,y]
    #   les deux listes triées sont identiques -> True
    return sorted(nettoye1) == sorted(nettoye2)


assert anagram_commente("Dormitory", "Dirty Room") \
    == anagram("Dormitory", "Dirty Room")
