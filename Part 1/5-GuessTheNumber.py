"""
Game n°1 : Guess the number
1. Il est temps de développer notre premier mini-jeu.
Le programme génère un nombre aléatoire, qui sera le nombre secret.
L'utilisteur doit essayer de deviner ce nombre.
Après chaque essai, le programme indique à l'utilisateur si le nombre correspond au secret,
 est inférieur ou est supérieur.
Une partie se termine quand l'utilisateur a deviné le nombre secret.
Aide: Pour générer un nombre entier aléatoire entre 1 et 10, utilise:
r = random.randint(1, 10)
"""
import random  # random.randint() appartient à la libraire random, il nous faut donc l'importer



#Solution
"""
def guessTheNumber():
    secret = random.randint(1, 10)
    demanderNombre(secret)


def demanderNombre(secret):
    guess = int(input("Devinez le nombre secret: "))
    if guess == secret:
        print("Vous avez gagné")
    elif guess > secret:  # elif est un raccourci pour faire else: if
        print("Trop grand")
        demanderNombre(secret)
    else:
        print("Trop petit")
        demanderNombre(secret)
"""

# 2----------------------------------------------------------------------------------------------------
"""
2. Ajouter un compteur du nombre d'essais.
Quand une partie se termine, le programme affiche à l'utilisateur une phrase pour indiquer
 le nombre d'essais qu'il a effectués pour trouver le nombre secret.
Indice: On peut concaténer (coller) des strings entre elles avec un +.
Exemple:
print("conca" + "ténation") -> "concaténation"
Attention a bien vérifié que les éléments de la concaténation soient des strings.
Convertir avec str() si besoin.
"""



#Solution
"""
def guessTheNumber():
    secret = random.randint(1, 10)
    compteurEssais = 0
    nEssais = demanderNombre(secret, compteurEssais)
    print("Vous avez devinez le nombre en " + str(nEssais) + " essais.")

def demanderNombre(secret, compteurEssais):
    guess = int(input("Devinez le nombre secret: "))
    compteurEssais += 1  # Les opérations arithmétiques (addition, soustraction, multiplication...)
    #  peuvent être contractées. i += 1  <=>  i = i + 1
    if guess == secret:
        print("Vous avez gagné!")
    elif guess > secret:  # elif est un raccourci pour faire else: if
        print("Trop grand")
        return demanderNombre(secret, compteurEssais)
    else:
        print("Trop petit")
        return demanderNombre(secret, compteurEssais)
    return compteurEssais
"""

# 3----------------------------------------------------------------------------------------------------
"""
3. A la fin de la partie, le programme demande à l'utilisateur s'il veut refaire une partie ou quitter le programme.
Aide: On peut utiliser les variables booléennes.
Une variable booléenne peut valoir soit True, soit False (vrai ou faux).
"""



#Solution
"""
def main():
    joueurVeutContinuer = True
    while joueurVeutContinuer:
        guessTheNumber()
        joueurVeutContinuer = bool(input("Recommencer ?: "))

def guessTheNumber():
    secret = random.randint(1, 10)
    compteurEssais = 0
    nEssais = demanderNombre(secret, compteurEssais)
    print("Vous avez devinez le nombre en " + str(nEssais) + " essais.")

def demanderNombre(secret, compteurEssais):
    guess = int(input("Devinez le nombre secret: "))
    compteurEssais += 1  # Les opérations arithmétiques (addition, soustraction, multiplication...)
    #  peuvent être contractées. i += 1  <=>  i = i + 1
    if guess == secret:
        print("Vous avez gagné!")
    elif guess > secret:  # elif est un raccourci pour faire else: if
        print("Trop grand")
        return demanderNombre(secret, compteurEssais)
    else:
        print("Trop petit")
        return demanderNombre(secret, compteurEssais)
    return compteurEssais
"""