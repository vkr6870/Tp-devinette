"""Écris un programme qui fait jouer l’utilisateur à un jeu de devinette.
Objectif
L’ordinateur choisit au hasard un nombre compris entre 0 et 100.
Le joueur a 5 chances pour deviner ce nombre.
Règles du jeu
À chaque tour, l’utilisateur entre un nombre entre 0 et 100.
Le programme indique ensuite :
"C’est plus grand" si le nombre à deviner est plus grand que la proposition,
"C’est plus petit" si le nombre à deviner est plus petit.
Si le joueur trouve le bon nombre, le programme affiche :
"Bravo ! Tu as trouvé le nombre !"
et la partie se termine immédiatement.
Si le joueur n’a plus d’essais, le programme affiche :
"Dommage, le nombre était X."
(où X est le nombre à deviner)."""

from random import *

def devinette() :
    time = 0
    rando = randint(0,100)
    for i in range(5) :
        n = int(input("entrez un nombre entier positif :"))
        if n == rando :
            return("Bravo ! Tu as trouvé le nombre !")
        if n < rando :
            print("C’est plus grand")
        else :
             print("C’est plus petit")
    return("Dommage, le nombre était", rando)
    
print(devinette())