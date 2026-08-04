# =====================================================================
# EXERCICE : py_inter
#
# BUT : renvoyer une chaîne contenant les caractères qui apparaissent
# DANS LES DEUX chaînes (s1 ET s2), sans répétition, et dans l'ordre
# où ils apparaissent dans s1.
# =====================================================================

def inter(s1: str, s2: str) -> str:
    resultat = ""
    for char in s1:
        if char in s2 and char not in resultat:
            resultat += char
    return resultat


if __name__ == "__main__":
    assert inter("hello", "world") == "lo"
    assert inter("banana", "band") == "ban"
    assert inter("abcabc", "bc") == "bc"
    assert inter("abc", "xyz") == ""
    assert inter("", "abc") == ""
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def inter_commente(s1: str, s2: str) -> str:
    # "resultat" va accueillir les caractères communs trouvés, dans
    # l'ordre où on les rencontre en parcourant s1. On part d'une
    # chaîne vide.
    resultat = ""

    for char in s1:
        # Deux conditions doivent être vraies pour ajouter "char" :
        #  1) "char in s2" : est-ce que cette lettre existe QUELQUE
        #     PART dans s2 ? (peu importe où)
        #  2) "char not in resultat" : est-ce qu'on ne l'a pas DEJA
        #     ajoutée avant ? Ca évite les doublons si s1 contient
        #     plusieurs fois la même lettre (ex: "banana" a 3 "a").
        if char in s2 and char not in resultat:
            resultat += char

    # Schéma pour inter("banana", "band") :
    #
    #   s1 = "banana", s2 = "band"
    #
    #   char='b' -> 'b' in "band" ? oui. 'b' not in "" ? oui -> +b   -> resultat="b"
    #   char='a' -> 'a' in "band" ? oui. 'a' not in "b" ? oui -> +a  -> resultat="ba"
    #   char='n' -> 'n' in "band" ? oui. 'n' not in "ba" ? oui -> +n -> resultat="ban"
    #   char='a' -> déjà dans resultat -> on ignore
    #   char='n' -> déjà dans resultat -> on ignore
    #   char='a' -> déjà dans resultat -> on ignore
    #
    #   résultat final : "ban"
    return resultat


assert inter_commente("banana", "band") == inter("banana", "band")
