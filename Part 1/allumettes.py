def main():
    print("\nJeu des allumettes :")
    print("La partie commence avec un ensemble d'allumettes, typiquement 21.")
    print("Tour à tour, les deux joueurs vont enlever 1, 2 ou 3 allumettes.")
    print("Le joueur qui enleve la dernière remporte la partie.")

    auTourDuJoueur1 = True
    nAllumettes = demanderNAllumettes()

    while not partieEstTerminee(nAllumettes):  # Boucle de jeu
        nAllumettes = jouer(auTourDuJoueur1, nAllumettes)
        auTourDuJoueur1 = not auTourDuJoueur1  # On inverse la valeur du booléen pour faire jouer l'autre joueur

    numeroDuJoueur = "2" if auTourDuJoueur1 else "1"  # Opérateur ternaire
    print("\nPartie terminée, le gagnant est le joueur " + numeroDuJoueur + "\n")


def demanderNAllumettes():
    n = eval(input("\nEntrez le nombre initial d'allumettes : "))
    return n


def jouer(auTourDuJoueur1, nAllumettes):
    numeroDuJoueur = "1" if auTourDuJoueur1 else "2"  # Opérateur ternaire
    print("\n" + "-" * 20 + " Tour du joueur " + numeroDuJoueur + " " + "-" * 20)

    afficherAllumettes(nAllumettes)

    n = eval(input("\nCombien d'allumette(s) prenez-vous ? (1, 2 ou 3) : "))
    nAllumettes -= n

    return nAllumettes


def afficherAllumettes(nAllumettes):
    allumette = "| "
    message = "\nIl reste " + str(nAllumettes) + " allumette(s)\n"
    for i in range(nAllumettes):
        message += allumette
    print(message)


def partieEstTerminee(nAllumettes):
    return nAllumettes <= 0


main()
