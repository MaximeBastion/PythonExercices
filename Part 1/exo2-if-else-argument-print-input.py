"""
1. Créer une fonction qui affiche dans la console si un age passé en paramètre est considéré majeur ou mineur.
Indice: utilise print(string) pour afficher du texte dans la console.
"""



#Solution
"""
def estMajeur(age):
    if age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
"""

# 2----------------------------------------------------------------------------------------------------
"""
2. Dans la fonction, demander directement à l'utilisateur son age via la console plutôt que de le passer en argument.
Indice: utilise input(string) pour demander à l'utilisateur de rentrer une valeur dans la console.
Indice: tu peux convertir d'un type de variable à un autre. Par exemple, utilise int(string) pour récupérer
 un nombre entier après avoir demander l'âge.
"""



#Solution
"""
def estMajeur():
    age = int(input("Quel age avez-vous ?: "))
    if age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
"""

# 3----------------------------------------------------------------------------------------------------
"""
3. L'âge majeur change selon le pays. 
Ajoute un paramètre pour permettre d'appeler la fonction avec différents âges de majorité.
"""



#Solution
"""
def estMajeur(ageMajeur):
    age = int(input("Quel age avez-vous ?: "))
    if age >= ageMajeur:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
"""