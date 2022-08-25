import pandas as pd
lesRevenus=[]
course = {
  "aliment": [],
  "entretien": []
}

def revenus():
    while len(lesRevenus) < 4:
        revenu = int(input("entrer vos revenus : "))
        if revenu <0:
            return "incorrect"
        else:
            lesRevenus.append(revenu)
            print(lesRevenus)
    return lesRevenus
def SommeRevenus():
    dotation= sum(lesRevenus)
    print(f"votre dotation du mois est : {dotation}")
    return dotation
def budget():
    depense=0
    while depense < SommeRevenus():
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
def creationDataFra():
    df = pd.DataFrame(course)
    print(df.describe())
    return df
def EnregistrerCsv():
    creationDataFra().to_csv("course.csv", index=False)
    return "votre fichier a été créé"

    
revenus()
SommeRevenus()
budget()
creationDataFra()
EnregistrerCsv()