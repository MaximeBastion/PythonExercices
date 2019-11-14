"""
1. Créer une fonction qui affiche dans la console les entiers naturels de 0 à 4,
 séparés par des retours à la ligne.
0
1
2
3
4
"""



#Solution
"""
def afficherNombres():
    print("0")
    print("1")
    print("2")
    print("3")
    print("4")
"""

"""
Pour répéter plusieurs fois une action, on peut utiliser la boucle for.
Les instructions se trouvant dans la boucle for sont répétées autant de fois
 que la valeur pour l'argument de range(n). La valeur de x va itérérer de 0 à n - 1.
"""
#Exemple
"""
def afficherNombres():
    for i in range(5):
        print(i)
"""

# 2----------------------------------------------------------------------------------------------------
"""
2. Reprendre l'exemple pour faire en sorte que l'on puisse appeler la fonction en préciseant le dernier nombre.
"""



#Solution
"""
def afficherNombres(n):
    for i in range(n + 1):
        print(i)
"""

# 3----------------------------------------------------------------------------------------------------
"""
3. Modifier la fonction pour afficher le carré des nombres de 0 à n.
"""



#Solution
"""
def afficherNombres(n):
    for i in range(n + 1):
        print(i * i)
"""

# 4----------------------------------------------------------------------------------------------------
"""
4. Créer une fonction qui renvoie la somme des entiers naturels de 0 à n, n étant en argument/paramètre.
"""



#Solution
"""
def sommeEntiers(n):
    somme = 0
    for i in range(n + 1):
        somme = somme + i
    return somme
"""