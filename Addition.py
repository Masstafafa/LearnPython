#coding:utf-8

"""
Opérateurs en Python :  + (addition)
                        - (soustraction)
                        + (multiplication)
                        / (division)
                        % (modulo) -> reste d'une division euclidienne


variable = variable + X
variable += X

variable = variable - X
variable -= variable

variable =  variable * X
variable *= variable
"""

calcul = 5 / 2
calcul = int(calcul)
calcul2 = 5 % 2
calcul2 = int(calcul2)

print("Résultat =", calcul, "reste", calcul2)


niveau_personnage = input("Niveau de départ? ")
niveau_personnage = int(niveau_personnage)

print("Niveau du perso, ", niveau_personnage)

print("Combat réussi, tu gagnes un niveau !")
niveau_personnage = niveau_personnage +1
#idemn à
niveau_personnage += niveau_personnage

Print("Niveau du perso", niveau_personnage)