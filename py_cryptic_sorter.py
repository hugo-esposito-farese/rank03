# =====================================================================
# EXERCICE : py_cryptic_sorter
#
# BUT : trier une liste de chaînes selon 3 critères, dans cet ordre :
#   1. D'abord par LONGUEUR (les plus courtes en premier)
#   2. Si égalité de longueur : ordre alphabétique SANS tenir compte
#      des majuscules/minuscules
#   3. Si toujours égalité : par NOMBRE DE VOYELLES (croissant)
#   4. Si toujours égalité : on garde l'ordre d'origine (tri STABLE)
#
# INTERDIT : sorted() et list.sort() ne sont pas autorisés !
# =====================================================================

def cryptic_sorter(strings: list[str]) -> list[str]:

    def compter_voyelles(mot):
        total = 0
        for lettre in mot.lower():
            if lettre in "aeiou":
                total += 1
        return total

    def cle_de_tri(mot):
        return (len(mot), mot.lower(), compter_voyelles(mot))

    resultat = list(strings)
    for i in range(1, len(resultat)):
        courant = resultat[i]
        cle_courant = cle_de_tri(courant)
        j = i - 1
        while j >= 0 and cle_de_tri(resultat[j]) > cle_courant:
            resultat[j + 1] = resultat[j]
            j -= 1
        resultat[j + 1] = courant
    return resultat


if __name__ == "__main__":
    assert cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]) == \
        ["cat", "dog", "apple", "banana", "elephant"]
    assert cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]) == \
        ["aaa", "AAA", "bbb", "BBB"]
    assert cryptic_sorter(["hello", "world", "hi", "test"]) == \
        ["hi", "test", "hello", "world"]
    assert cryptic_sorter([]) == []
    assert cryptic_sorter([""]) == [""]
    print("Tous les tests sont passés !")


# =====================================================================
# VERSION COMMENTÉE (même logique, pour bien comprendre le "pourquoi")
# =====================================================================

def cryptic_sorter_commente(strings: list[str]) -> list[str]:

    def compter_voyelles(mot):
        # On compte les voyelles en minuscule pour ne pas dépendre de
        # la casse : "Elephant".lower() -> "elephant".
        total = 0
        for lettre in mot.lower():
            if lettre in "aeiou":
                total += 1
        return total

    def cle_de_tri(mot):
        # Une CLE DE TRI, c'est ce qu'on compare à la place du mot
        # lui-même pour décider qui passe avant qui. Ici on renvoie un
        # TUPLE (une sorte de "paquet" ordonné et non modifiable de
        # plusieurs valeurs) : (longueur, mot_en_minuscule, voyelles).
        #
        # Pourquoi un tuple ? Parce que Python sait comparer deux
        # tuples élément par élément, EXACTEMENT dans l'ordre de nos 3
        # critères :
        #   - il compare d'abord le 1er élément (la longueur)
        #   - s'il y a égalité, il compare le 2e (le mot en minuscule)
        #   - s'il y a encore égalité, il compare le 3e (les voyelles)
        # C'est très exactement ce que demande l'énoncé !
        return (len(mot), mot.lower(), compter_voyelles(mot))

    # On travaille sur une COPIE de la liste de départ (list(strings))
    # plutôt que sur "strings" directement, pour ne pas modifier la
    # liste que l'appelant nous a donnée.
    resultat = list(strings)

    # ---- TRI PAR INSERTION ----
    # Interdiction d'utiliser sorted()/list.sort() : il faut donc
    # coder l'algorithme de tri nous-mêmes. Le "tri par insertion"
    # fonctionne comme quand on trie des cartes à jouer dans sa main :
    # on prend les cartes une par une, et on insère chaque nouvelle
    # carte à sa bonne place parmi celles déjà triées avant elle.
    #
    # "i" avance sur chaque élément de la liste, à partir du 2e
    # élément (index 1) : le tout premier élément (index 0) est
    # considéré comme "déjà trié tout seul".
    for i in range(1, len(resultat)):

        # "courant" est l'élément qu'on doit replacer à la bonne
        # position parmi resultat[0..i-1] (qui sont déjà triés).
        courant = resultat[i]
        cle_courant = cle_de_tri(courant)

        # "j" commence juste avant "courant", et va reculer tant
        # qu'on trouve des éléments plus grands que "courant" (donc
        # qui doivent passer APRES lui).
        j = i - 1

        # Tant que : (1) on n'est pas sorti du début de la liste, ET
        # (2) l'élément juste avant est "plus grand" que "courant"
        # -> on décale cet élément d'une case vers la droite pour lui
        # faire de la place, et on recule encore.
        while j >= 0 and cle_de_tri(resultat[j]) > cle_courant:
            resultat[j + 1] = resultat[j]
            j -= 1

        # Ici, la bonne place pour "courant" est juste après "j"
        # (soit parce qu'on est arrivé au début, soit parce que
        # l'élément en j n'est plus plus grand que "courant").
        resultat[j + 1] = courant

    # Schéma pour ["bbb", "aaa"] (2 éléments de même longueur) :
    #   i=1 : courant="aaa", cle_courant=(3,"aaa",3)
    #         j=0 : cle_de_tri("bbb")=(3,"bbb",3) > (3,"aaa",3) -> VRAI
    #               on décale "bbb" en position 1 -> ["bbb","bbb"]
    #               j devient -1, la boucle while s'arrête
    #         on place "aaa" en position j+1 = 0 -> ["aaa","bbb"]
    #
    # Pourquoi ce tri est-il STABLE (garde l'ordre d'origine en cas
    # d'égalité totale) ? Parce qu'on utilise ">" (strictement plus
    # grand) et non ">=" dans le while : un élément égal à "courant"
    # ne sera JAMAIS décalé, donc l'élément déjà présent avant garde
    # sa position relative devant le nouvel élément égal.
    return resultat


assert cryptic_sorter_commente(["apple", "cat", "banana", "dog", "elephant"]) \
    == cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])
