import csv

with open("depenses.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['date']} | {ligne['categorie']} | {ligne['description']} | {ligne['montant']} EUR")
totaldepense = 42.50 + 1.90 + 12.00 + 15.80 + 55.00 + 22.90 = 150.10
print(totaldepense)
totalalimentation = 42.50 + 15.80 = 58.30
print(totalalimentation)
totaltransport = 1.90 + 55.00 = 56.90
print(totaltransport)
totalloisirs = 12.00 + 22.90 = 23.90
print(totalloisirs)
hautedepense = 55.00
bassedepense = 1.90
print(hautedepense)
print(bassedepense)