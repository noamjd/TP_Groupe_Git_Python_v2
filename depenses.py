import csv
with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(f"{ligne['date']} | {ligne['categorie']} | {ligne['description']} | {ligne['montant']}")

for ligne in lecteur:
    total = 0
    total += float(ligne['montant'])
print(total)