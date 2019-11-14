"""
Une liste est une collection qui peut contenir plusieures éléments.
En Python, ces éléments peuvent être de n'importe quel type (int, string, float, list...).
Exemple:
fruits = ["banane", "pomme", "fraise"]
-- Accès à une valeur
Cette liste est composée de trois cellules. On peut accéder à une cellule via son index=adresse.
L'index du premier éléments est 0, celui du deuxième est 1, celui du troisième est 2...
Exemple:
premierFruit = fruits[0]
print(premierFruit) -> "banane"
1. Créer une fonction qui prend une liste en argument est affiche ses 3 premiers éléments.
"""
maListe = [2, 9, 1, 0, 5, 7, 9, 0]



#Solution
"""
def afficherListe(liste):
    for i in range(3):
        element = liste[i]
        print(element)
"""

# 2----------------------------------------------------------------------------------------------------
"""
2. Modifier la fonction précédente pour afficher tous les éléments de la liste.
Indice: len(liste) renvoie la taille d'une liste.
"""



#Solution
"""
def afficherListe(liste):
    for i in range(len(liste)):
        element = liste[i]
        print(element)
        
Il existe une autre méthode pour parcourir tous les éléments d'une collection.
-> for element in collection:
La variale 'element' va successivement prendre comme valeur chaque valeur de la collection.
On peut nommer notre variable comme on veut. On devrait prendre un nom pertinent selon le contexte.

def afficherListe2(liste):
    for fruit in liste:
        print(fruit)
"""

# 3----------------------------------------------------------------------------------------------------
"""
-- Affectation.
Comme pour une variable, on peut affecter une valeur a chaque cellule de notre liste.
Exemple:
On veut changer "banane" en "framboise". On accède a la case via son index, 
et on affecte avec la même syntaxe que pour une variable.
fruits[0] = "framboise"
Maintenant, fruits vaut:
["framboise", "pomme", "fraise"]
3. Créer une fonction qui interverti les deux premières valeur d'une liste passé en argument.
On n'a pas besoin de retourner la liste pour modifier la liste car c'est un objet dynamique.
"""



#Solution
"""
def intervertir(liste):
    premierElement = liste[0]
    deuxiemeElement = liste[1]
    liste[0] = deuxiemeElement
    liste[1] = premierElement

def intervertir2(liste):
    premierElement = liste[0]
    liste[0] = liste[1]
    liste[1] = premierElement

Le langage Python permet la double affectation.
Exemple:
x, y = 2, 5
On affect 2 à x, et 5 à y, en une seule ligne.

def intervertir3(liste):
    liste[0], liste[1] = liste[1], liste[0]
"""