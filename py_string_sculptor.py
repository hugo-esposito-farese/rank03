# =====================================================================
# EXERCICE : py_string_sculptor
#
# BUT : transformer une chaîne en alternant minuscule/majuscule, mais
# UNIQUEMENT pour les lettres. La 1ère lettre doit être en minuscule,
# la 2e en majuscule, la 3e en minuscule, etc. Un ESPACE réinitialise
# l'alternance.
# =====================================================================

def string_sculptor(text: str) -> str:
    resultat = ""
    doit_etre_majuscule = False
    for char in text:
        if char == " ":
            resultat += char
            doit_etre_majuscule = False
        elif char.isalpha():
            if doit_etre_majuscule:
                resultat += char.upper()
            else:
                resultat += char.lower()
            doit_etre_majuscule = not doit_etre_majuscule
        else:
            resultat += char
    return resultat


if __name__ == "__main__":
    assert string_sculptor("hello") == "hElLo"
    assert string_sculptor("Hello World") == "hElLo wOrLd"
    assert string_sculptor("abc123def") == "aBc123DeF"
    assert string_sculptor("Python3.9!") == "pYtHoN3.9!"
    assert string_sculptor("") == ""
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def string_sculptor_commente(text: str) -> str:
    # "resultat" va accueillir la chaîne finale, construite lettre
    # par lettre.
    resultat = ""

    # "doit_etre_majuscule" est un booléen (True/False) qui joue le
    # rôle d'un INTERRUPTEUR : il nous dit si la PROCHAINE lettre
    # alphabétique rencontrée doit être mise en majuscule ou non.
    # On commence à False car la toute première lettre doit être en
    # minuscule (voir l'énoncé).
    doit_etre_majuscule = False

    for char in text:

        if char == " ":
            # Un espace ne change pas lui-même de casse (il n'a pas
            # de majuscule/minuscule), mais il RESET l'alternance :
            # la prochaine lettre après un espace repart à minuscule.
            resultat += char
            doit_etre_majuscule = False

        elif char.isalpha():
            # On regarde l'état actuel de l'interrupteur pour décider
            # comment écrire cette lettre.
            if doit_etre_majuscule:
                resultat += char.upper()
            else:
                resultat += char.lower()

            # "not doit_etre_majuscule" inverse le booléen : True
            # devient False, et False devient True. C'est ainsi qu'on
            # PREPARE l'alternance pour la PROCHAINE lettre.
            doit_etre_majuscule = not doit_etre_majuscule

        else:
            # Un chiffre ou un symbole de ponctuation (comme '1', '.',
            # '!') reste inchangé, et surtout NE FAIT PAS basculer
            # l'interrupteur : il ne "compte pas" dans l'alternance.
            resultat += char

    # Schéma pour text = "abc123def" :
    #
    #   char  type        interrupteur avant   action           interrupteur après
    #   a     lettre      False                minuscule 'a'    True
    #   b     lettre      True                 majuscule 'B'    False
    #   c     lettre      False                minuscule 'c'    True
    #   1     chiffre     (inchangé)           '1' tel quel     True (ne bouge pas)
    #   2     chiffre     (inchangé)           '2' tel quel     True (ne bouge pas)
    #   3     chiffre     (inchangé)           '3' tel quel     True (ne bouge pas)
    #   d     lettre      True                 majuscule 'D'    False
    #   e     lettre      False                minuscule 'e'    True
    #   f     lettre      True                 majuscule 'F'    False
    #
    #   résultat final : "aBc123DeF"
    return resultat


assert string_sculptor_commente("Hello World") == string_sculptor("Hello World")
