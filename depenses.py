import csv

with open("depenses.csv", "r") encoding="utf-8") as f:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        depense = [
 {"Alimentation", "Courses", "supermarche": 42.50},
 {"Transport", "Ticketmetro": 1.90},
 {"Loisirs", "Cinema":12.00}
 {"Alimentation", "Restaurant", "midi":12.00}
 {"Trasnport", "Essence":55.00}
 {"Loisirs","livre", "python":22.90}
]

x ====
total = Alimentation,Courses,supermarche + Transport,Ticket,metro + Loisirs,Cinema + Alimentation,Restaurant,midi + Transport,Essence + Loisirs,Livre,Python
total = float(total) = 150.100
            