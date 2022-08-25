
"""      
TEXTE = "fichier.txt"

liste = []

with open(TEXTE, "r") as f:
    for line in f:
        if line.startswith("oui"):
            print("trouvé")
            liste.append(line)
            print(liste)
        else:
            print("echec")
"""
"""
def addition(a,b):
    return a + b

print(addition(2,3))


def soustarc (a,b):
    return a - b

def mult (a,b):
    return a *b

def div (a,b):
    return a // 2

print(div(4,2))

def hello ():
    return "Hello World"
    
"""
"""
print("-" * 22)

print(len('abcd'))

print(len({'x':3, 'y': 3}))
"""
######################################
# DEBUT DU PROGRAMME BUDGET JOURNALIER
######################################
import pandas as pd
import matplotlib.pyplot as plt
print("starting")

dotation = int(input("entrer votre budget: "))



    

course = {
  "aliment": [],
  "entretien": []
}
reste = dotation - sum(course["aliment"]) + sum(course["entretien"])

depense = 0


while depense < dotation:
    alimentation = int(input("entrer montant alimen: "))
    entretiens = int(input("entrer montant entre: "))
    if alimentation == 0 or entretiens == 0:
        pass
    if alimentation <0 or entretiens < 0:
        print("le montant ne peut etre négatif")
        pass
    else:
        depense+=alimentation
        depense+=entretiens
        course["entretien"].append(entretiens)
        course["aliment"].append(alimentation)
        print(depense)
print("budget atteint")

df = pd.DataFrame(course)

print(df.describe())

print(df)

df.to_csv("course.csv", index=False)

df.plot()
plt.show()





    













