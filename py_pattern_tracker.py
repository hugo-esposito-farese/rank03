# =====================================================================
# EXERCICE : py_pattern_tracker
#
# BUT : compter le nombre de paires de chiffres CONSECUTIFS valides
# dans une chaîne. Une paire est valide si le 2e chiffre vaut
# EXACTEMENT le 1er chiffre + 1. Attention : 9 suivi de 0 n'est PAS
# valide (pas de "bouclage").
# =====================================================================

def pattern_tracker(text: str) -> int:
    compteur = 0
    for i in range(len(text) - 1):
        premier = text[i]
        second = text[i + 1]
        if premier.isdigit() and second.isdigit():
            if int(second) == int(premier) + 1:
                compteur += 1
    return compteur


if __name__ == "__main__":
    assert pattern_tracker("123") == 2
    assert pattern_tracker("12a34") == 2
    assert pattern_tracker("987654321") == 0
    assert pattern_tracker("01234567") == 7
    assert pattern_tracker("abc") == 0
    assert pattern_tracker("1a2b3c4") == 0
    assert pattern_tracker("112233") == 2
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def pattern_tracker_commente(text: str) -> int:
    # "compteur" va compter le nombre de paires valides trouvées.
    compteur = 0

    # On veut regarder la chaîne DEUX caractères à la fois : le
    # caractère à la position i, et celui juste après, à la position
    # i+1. range(len(text) - 1) s'arrête un cran plus tôt que la
    # longueur totale, exactement pour que "i + 1" ne dépasse jamais
    # la fin de la chaîne.
    #
    # Exemple avec text de longueur 5 (indices 0,1,2,3,4) :
    # range(5-1) = range(4) -> i prend les valeurs 0,1,2,3
    # (on ne va pas jusqu'à i=4, car il n'y aurait pas de "i+1" après)
    for i in range(len(text) - 1):
        premier = text[i]        # le caractère "de gauche" de la paire
        second = text[i + 1]     # le caractère "de droite" de la paire

        # .isdigit() répond True si le caractère est un chiffre
        # ('0' à '9'). On doit vérifier que LES DEUX caractères de la
        # paire sont bien des chiffres avant de les comparer, sinon
        # on ne peut pas faire int() dessus (une lettre ferait planter
        # le programme).
        if premier.isdigit() and second.isdigit():
            # int(premier) transforme le CARACTERE '3' en le NOMBRE 3
            # pour pouvoir faire un calcul dessus. On vérifie que le
            # second chiffre est exactement "un de plus" que le
            # premier.
            #
            # Remarque importante sur le "9 suivi de 0" : si premier='9'
            # et second='0', on calcule int('0')==int('9')+1, soit
            # 0 == 10, ce qui est FAUX. Le "bouclage" n'a donc jamais
            # lieu automatiquement, exactement comme demandé.
            if int(second) == int(premier) + 1:
                compteur += 1

    # Schéma pour text = "112233" :
    #   paires examinées : (1,1) (1,2) (2,2) (2,3) (3,3)
    #   valides ?          non   oui   non   oui   non
    #   -> compteur final = 2
    return compteur


assert pattern_tracker_commente("112233") == pattern_tracker("112233")
