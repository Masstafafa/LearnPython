#coding:utf-8

""" 
Nommer une variable : 
doit commencer par une lettre ou un underscore (_)
ne doit pas contenir de caractères spéciaux ou d'accents
ne pas conternir d'espaces
utiliser des underscores (_)

types standards :
entier numérique (int)
nombre flottant (float)
chaines de caractères (str)
booléen (bool)
autres (listes, dictionnaires, tuples, etc...)

Fonctions vues :
print()                             -> afficher à l'écran
input()                             -> lire au clavier
type()                              -> retourne le type d'une donnée, variable, etc...
str.format()                        -> formater une chaine
int() float() str() bool()          -> "caster" une donnée, la convertir
"""


age_personne = 14 
prixHT = 120.45
age_personne_2 = "25"
continuer_partie = True / False


texte = "L'âge de la personne est {} et le prix HT est de {} euros."
print(texte.format(age_personne, prixHT))
#pareil que
print("L'âge de la personne est {} et le prix HT est de {} euros.".format(age_personne, prixHT))


nom_joueur = input("Choisissez un nom de joueur : ")

print("Bienvenue,", nom_joueur)


prixHT = input("Entrez un prix HT : ")
prixHT = int(prixHT)

PrixTTC = prixHT + (prixHT * 20 / 100)

print("Prix TTC = ", PrixTTC)

