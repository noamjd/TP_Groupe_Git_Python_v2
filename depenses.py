import csv

with open("depenses.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['date']} | {ligne['categorie']} | {ligne['description']} | {ligne['montant']} EUR")
