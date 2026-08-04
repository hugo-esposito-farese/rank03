# =====================================================================
# EXERCICE : py_whisper_cipher
#
# BUT : coder un "chiffre de César" : décaler chaque LETTRE dans
# l'alphabet d'un certain nombre de positions (shift). Les caractères
# non-alphabétiques restent inchangés. Le décalage peut être négatif.
# On garde la majuscule/minuscule d'origine.
# =====================================================================

def whisper_cipher(text: str, shift: int) -> str:
    resultat = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            position = ord(char) - base
            nouvelle_position = (position + shift) % 26
            resultat += chr(base + nouvelle_position)
        else:
            resultat += char
    return resultat


if __name__ == "__main__":
    assert whisper_cipher("hello", 3) == "khoor"
    assert whisper_cipher("Hello World!", 1) == "Ifmmp Xpsme!"
    assert whisper_cipher("xyz", 3) == "abc"
    assert whisper_cipher("ABC123def", 5) == "FGH123ijk"
    assert whisper_cipher("", 10) == ""
    assert whisper_cipher("abc", -3) == "xyz"
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def whisper_cipher_commente(text: str, shift: int) -> str:
    resultat = ""

    for char in text:
        if char.isalpha():
            # ord(char) donne le CODE NUMERIQUE d'un caractère (chaque
            # caractère a un numéro unique en informatique). Par
            # exemple ord('a') = 97, ord('A') = 65.
            #
            # On veut travailler avec une position "0 à 25" DANS
            # L'ALPHABET (peu importe la casse), donc on doit d'abord
            # savoir quelle est la "base" à soustraire : celle de 'a'
            # si la lettre est minuscule, celle de 'A' si elle est
            # majuscule. C'est ce que fait cette ligne, avec un "if"
            # écrit sur une seule ligne (opérateur ternaire) :
            # "base = ord('A') si char est en majuscule, sinon ord('a')"
            base = ord('A') if char.isupper() else ord('a')

            # "position" est la place de la lettre DANS L'ALPHABET,
            # de 0 (a ou A) à 25 (z ou Z).
            # Exemple : char='h' -> ord('h')=104, base=ord('a')=97
            #           position = 104 - 97 = 7 (h est la 8e lettre,
            #           donc à l'index 7 en partant de 0)
            position = ord(char) - base

            # On ajoute le décalage "shift" à cette position, puis on
            # fait "% 26" (modulo 26, car l'alphabet a 26 lettres)
            # pour "boucler" si on dépasse la fin (ou le début) de
            # l'alphabet.
            #
            # Exemple avec un shift négatif : position=0 ('a'), shift=-3
            #   0 + (-3) = -3
            #   -3 % 26 = 23   (en Python, le modulo d'un nombre négatif
            #                   renvoie directement un résultat positif,
            #                   donc ça boucle automatiquement vers la
            #                   fin de l'alphabet -> 23 correspond à 'x')
            nouvelle_position = (position + shift) % 26

            # chr() fait l'inverse d'ord() : elle transforme un code
            # numérique en caractère. "base + nouvelle_position"
            # recalcule le bon code numérique (en gardant la bonne
            # casse, minuscule ou majuscule, grâce à "base").
            resultat += chr(base + nouvelle_position)
        else:
            # Un caractère qui n'est pas une lettre (chiffre, espace,
            # ponctuation) est recopié tel quel, sans aucun décalage.
            resultat += char

    # Schéma pour whisper_cipher("xyz", 3) :
    #   x : position=23, (23+3)%26 = 26%26 = 0  -> 'a'
    #   y : position=24, (24+3)%26 = 27%26 = 1  -> 'b'
    #   z : position=25, (25+3)%26 = 28%26 = 2  -> 'c'
    #   résultat : "abc"  (on a "bouclé" après 'z' pour revenir à 'a')
    return resultat


assert whisper_cipher_commente("xyz", 3) == whisper_cipher("xyz", 3)
assert whisper_cipher_commente("abc", -3) == whisper_cipher("abc", -3)
