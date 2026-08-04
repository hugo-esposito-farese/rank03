# =====================================================================
# EXERCICE : py_bracket_validator
#
# BUT : vérifier si les parenthèses/crochets/accolades d'une chaîne
# sont bien "équilibrés" : chaque symbole ouvrant doit avoir son
# symbole fermant correspondant, dans le bon ordre, et bien imbriqué.
# Types autorisés : (), [], {}
# =====================================================================

def bracket_validator(s: str) -> bool:
    paires = {')': '(', ']': '[', '}': '{'}
    pile = []
    for char in s:
        if char in '([{':
            pile.append(char)
        elif char in ')]}':
            if not pile or pile.pop() != paires[char]:
                return False
    return len(pile) == 0


if __name__ == "__main__":
    assert bracket_validator("()") is True
    assert bracket_validator("()[]{}") is True
    assert bracket_validator("(]") is False
    assert bracket_validator("([)]") is False
    assert bracket_validator("{[]}") is True
    assert bracket_validator("hello(world)") is True
    assert bracket_validator("((())") is False
    assert bracket_validator("") is True
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def bracket_validator_commente(s: str) -> bool:
    # "paires" est un dictionnaire (dict) : une structure qui associe
    # une CLE à une VALEUR. Ici, chaque symbole FERMANT (la clé) est
    # associé au symbole OUVRANT qu'il est censé refermer (la valeur).
    # Exemple : paires[')'] vaut '(' -> "si je vois ')', j'attends '('"
    paires = {')': '(', ']': '[', '}': '{'}

    # "pile" est une liste Python utilisée comme une PILE (stack) :
    # une structure de données où on ajoute et retire des éléments
    # uniquement par le dernier ajouté (comme une pile d'assiettes :
    # on pose une assiette sur le dessus, on retire celle du dessus).
    # Au départ, la pile est vide : aucun symbole ouvrant en attente.
    pile = []

    # On parcourt la chaîne "s" caractère par caractère. A chaque tour
    # de boucle, "char" contient UN SEUL caractère de la chaîne.
    for char in s:

        # Cas 1 : le caractère est un symbole OUVRANT.
        if char in '([{':
            # .append() ajoute "char" à la FIN de la liste "pile",
            # donc "sur le dessus" de notre pile d'assiettes.
            pile.append(char)

        # Cas 2 : le caractère est un symbole FERMANT.
        elif char in ')]}':
            # "not pile" vaut True si la pile est VIDE (une liste vide
            # est considérée comme "fausse" en Python : bool([]) == False).
            # ".pop()" retire ET renvoie le DERNIER élément de la
            # liste (celui du dessus de la pile) ; la liste "pile"
            # devient donc plus courte d'un élément après cet appel.
            #
            # La condition vérifie deux choses, reliées par "or" :
            #   - la pile est-elle vide ? (un fermant sans ouvrant en
            #     attente -> invalide)
            #   - OU le dernier ouvrant empilé n'est pas celui que ce
            #     symbole fermant attend (paires[char]) ?
            # Si l'une des deux est vraie, la chaîne est invalide et
            # on arrête tout de suite avec return False.
            if not pile or pile.pop() != paires[char]:
                return False

        # Si le caractère n'est ni ouvrant ni fermant (une lettre par
        # exemple, comme dans "hello(world)"), on ne fait rien de
        # spécial : aucune des deux conditions ci-dessus n'est vraie,
        # donc on passe directement au caractère suivant.

    # Schéma de ce qui se passe avec l'exemple "([)]" :
    #
    #   caractère   action                      contenu de "pile"
    #   ---------   ------------------------    ------------------
    #   (           ouvrant -> empilé            ['(']
    #   [           ouvrant -> empilé            ['(', '[']
    #   )           fermant -> pop() = '['       ['(']
    #               mais paires[')'] = '('
    #               '[' != '('  -> return False immédiatement
    #
    # Si on arrive jusqu'ici (aucun "return False" ne s'est déclenché),
    # la chaîne est valide SEULEMENT si la pile est vide : cela
    # signifie que chaque symbole ouvrant empilé a bien été retiré par
    # un symbole fermant correspondant. S'il reste des éléments dans
    # la pile, c'est qu'il manque des fermetures (ex: "((())").
    return len(pile) == 0


assert bracket_validator_commente("([)]") == bracket_validator("([)]")
assert bracket_validator_commente("{[]}") == bracket_validator("{[]}")
