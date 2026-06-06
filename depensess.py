import csv
alimentation = 'Alimentation'
total_alimentation = 0
transport = 'Transport'
total_transport = 0
loisirs = 'Loisirs'
total_loisirs = 0
total = 0
depense_basse = 0
depense_haute = 0
with open("depenses.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['date']} | {ligne['categorie']} | {ligne['description']} | {ligne['montant']} EUR")
        try:
            total += float(ligne["montant"])
        except ValueError:
            print(f"impossible de calculer le total : {ligne}")
        try:
            if ligne["categorie"] == "Alimentation":
                total_alimentation += float(ligne["montant"])
            
        except ValueError:
            print(f"impossible de calculer le total_alimentation : {ligne}")
        try:
            if ligne["categorie"] == "Transport":
                total_transport += float(ligne["montant"])
                
        except ValueError:
            print(f"impossible de calculer le total_alimentation : {ligne}")
        try:
            if ligne["categorie"] == "Loisirs":
                total_loisirs += float(ligne["montant"])
                
        except ValueError:
            print(f"impossible de calculer le total_alimentation : {ligne}")        
        if float(ligne["montant"]) < float(depense_basse):
            depense_basse = ligne["montant"]
        if float(ligne["montant"]) > float(depense_haute):
            depense_haute = ligne["montant"]    
    nouvelle_depense = {
    "date": "2024-01-20",
    "categorie": "Alimentation",
    "description": "Pizzeria",
    "montant": "18.50"
}

with open("depenses.csv", "a", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "categorie", "description", "montant"])
    writer.writerow(nouvelle_depense)
                                      
print(f"total: {total}")
print(f"total: {total_alimentation}")
print(f"total: {total_transport}")
print(f"total: {total_loisirs}")
print(f"total: {nouvelle_depense}")