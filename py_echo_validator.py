# =====================================================================
# EXERCICE : py_echo_validator
#
# BUT : vérifier si une chaîne est un PALINDROME (elle se lit pareil
# à l'endroit et à l'envers), en ignorant les espaces et la casse, et
# en ne gardant que les lettres.
# =====================================================================

def echo_validator(text: str) -> bool:
    nettoye = ""
    for char in text:
        if char.isalpha():
            nettoye += char.lower()
    if nettoye == "":
        return False
    return nettoye == nettoye[::-1]


if __name__ == "__main__":
    assert echo_validator("racecar") is True
    assert echo_validator("A man a plan a canal Panama") is True
    assert echo_validator("race a car") is False
    assert echo_validator("Was it a car or a cat I saw") is True
    assert echo_validator("hello") is False
    assert echo_validator("Madam Im Adam") is True
    assert echo_validator("") is False
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def echo_validator_commente(text: str) -> bool:
    # "nettoye" va accueillir une version "propre" de "text" : que des
    # lettres, toutes en minuscule, sans espaces ni ponctuation. Au
    # départ, c'est une chaîne vide, on va la construire petit à petit.
    nettoye = ""

    for char in text:
        # .isalpha() répond True si "char" est une lettre (a-z, A-Z,
        # et aussi les lettres accentuées), et False pour un espace,
        # un chiffre ou de la ponctuation.
        if char.isalpha():
            # .lower() transforme la lettre en minuscule (ex: 'A' -> 'a')
            # pour que "Madam" et "madam" soient traités pareil.
            # On l'ajoute à la fin de "nettoye" avec +=.
            nettoye += char.lower()

    # Schéma pour text = "A man a plan a canal Panama" :
    #   "A man a plan a canal Panama"
    #              |
    #      on garde seulement les lettres, en minuscule
    #              v
    #   "amanaplanacanalpanama"
    #
    # Si après nettoyage il ne reste AUCUNE lettre (ex: text = "123"
    # ou text = ""), on considère que ce n'est pas un palindrome
    # valide : c'est ce que testent les exemples avec echo_validator("").
    if nettoye == "":
        return False

    # nettoye[::-1] veut dire : "prends toute la chaîne, mais en
    # partant du dernier caractère et en reculant jusqu'au premier".
    # C'est la façon la plus courante en Python d'inverser une chaîne.
    # Un palindrome est une chaîne qui est identique à son inverse.
    return nettoye == nettoye[::-1]


assert echo_validator_commente("Was it a car or a cat I saw") \
    == echo_validator("Was it a car or a cat I saw")
