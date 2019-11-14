import random


def main():
    print("\nJeu des allumettes :")
    print("La partie commence avec un ensemble d'allumettes, typiquement 21.")
    print("Tour à tour, les deux joueurs vont enlever 1, 2 ou 3 allumettes.")
    print("Le joueur qui enlève la dernière remporte la partie.")

    ia = eval(input("\nVoulez-vous jouer contre l'ordinateur ? (1 ou 0) : "))
    nAllumettes = demanderNAllumettes()

    auTourDuJoueur1 = random.randint(0, 1) == 1  # Le joueur qui commence est déterminé aléatoirement
    print("\nLe joueur " + getNumeroJoueur(auTourDuJoueur1) + " commence")

    while not partieEstTerminee(nAllumettes):  # Boucle de jeu
        nAllumettes = jouer(auTourDuJoueur1, nAllumettes, ia)
        auTourDuJoueur1 = not auTourDuJoueur1  # On inverse la valeur du booléen pour faire jouer l'autre joueur

    print("\nPartie terminée, le gagnant est le joueur " + getNumeroJoueur(auTourDuJoueur1, True) + "\n")


def demanderNAllumettes():
    return eval(input("\nEntrez le nombre initial d'allumettes : "))


def jouer(auTourDuJoueur1, nAllumettes, ia):
    print("\n" + "-" * 20 + " Tour du joueur " + getNumeroJoueur(auTourDuJoueur1) + " " + "-" * 20)

    afficherAllumettes(nAllumettes)

    n = 1
    if ia and not auTourDuJoueur1:  # On teste si l'ordinateur devrait jouer
        n = getIANombreAllumettes(nAllumettes)
        print("\nL'ordinateur prend " + str(n) + getTextAllumettes(nAllumettes))
    else:
        n = demanderNAllumettesAPrendre(nAllumettes)
    nAllumettes -= n

    return nAllumettes


def afficherAllumettes(nAllumettes):
    allumette = "| "
    message = "\nIl reste " + str(nAllumettes) + getTextAllumettes(nAllumettes) + "\n"
    for i in range(nAllumettes):
        message += allumette
    print(message)


def partieEstTerminee(nAllumettes):
    return nAllumettes <= 0


def getIANombreAllumettes(nAllumettes):  # L'IA adopte la stratégie de prendre un nombre d'allumettes
    if nAllumettes <= 3:  # qui laisse un nombre d'allumettes multiple de 4.
        return nAllumettes  # Sa victoire est assurée s'il commence.
    if nAllumettes == 4:
        return 1
    return nAllumettes % 4


def demanderNAllumettesAPrendre(total):
    reponseJoueur = 10
    while reponseJoueur not in [1, 2, 3] or reponseJoueur > total:
        reponseJoueur = eval(input("\nCombien d'allumette(s) prenez-vous ? (1, 2 ou 3) : "))
    return reponseJoueur


def getNumeroJoueur(auTourDuJoueur1, inverser=False):  # Renvoie dans le numéro du joueur en string
    if inverser:
        auTourDuJoueur1 = not auTourDuJoueur1
    return "1" if auTourDuJoueur1 else "2"


def getTextAllumettes(nAllumettes):
    return " allumettes" if nAllumettes > 1 else " allumette"


main()
