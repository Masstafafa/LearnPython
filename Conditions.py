#coding:utf-8

"""
Opérateurs de comparaison :     == (égal à)
                                != (différent de)
                                < (plus petit que)
                                > (plus grand que)
                                <= (pls petit ou égal à)
                                >= (plus grand ou égal à)


Conditions multiples :          and (ET)
                                or (OU)
                                in / not in (Dans / Pas dans)

Mot clés des conditions :       if / elif / else
"""

identifiant = "Jason"
mot_de_passe = "password123"

print("Interface de connexion")

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe / ")

if user_id == identifiant and user_password == mot_de_passe:
    print("Vousêtes connectés, bienvenue, user_id")


lettre_hasard = "b"

if lettre_hasard in "aeiouy":
    print("c'est une voyelle")
else:
    print("C'est une consonne")


age = 24

if age == 18:
    print("tu viens d'être majeur")
elif age == 50:
    print("tu viens d'avoir 50ans")
elif age == 60:
    print("Tu viens d'avoir 60 ans")
else:
    print("tu as", age, "ans")


age = input("Quel âge as-tu? ")
age = int(age)

"""
age > 0 ET <= 100 --> 0 < age <= 100
"""

if 0 < age <= 100:
    print("L'age est validé")
else:
    print("l'age est incorrect")

    
