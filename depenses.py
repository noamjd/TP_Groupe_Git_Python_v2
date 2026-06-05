import csv
total = 0
alimentation = 'Alimentation'
total_alimentation = 0
transport = 'Transport'
total_transport = 0
loisirs = 'Loisirs'
total_loisirs = 0
depense_moins = 1000000000000
depense_plus = 0
with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(f"{ligne['date']} | {ligne['categorie']} | {ligne['description']} | {ligne['montant']}")
        try:
            total += float(ligne["montant"])
        except ValueError:
            print(f"Attention : Impossible de lire le montant pour la ligne {ligne}")
        if ligne['categorie'] == alimentation:
            try:
                total_alimentation += float(ligne['montant']) 
            except ValueError:
                print(f"Attention : Impossible de lire le montant pour la ligne {ligne}")
        if ligne['categorie'] == transport:
            try:
                total_transport += float(ligne['montant'])
            except ValueError:
                print(f"Attention : Impossible de lire le montant pour la ligne {ligne}")
        if ligne['categorie'] == loisirs:
            try:
                total_loisirs += float(ligne['montant'])
            except ValueError:
                print(f"Attention : Impossible de lire le montant pour la ligne {ligne}")
        if float(ligne['montant']) < float(depense_moins):
            depense_moins = ligne['montant']
        if float(ligne['montant']) > float(depense_plus):
            depense_plus = ligne['montant']
                      
print(total)
print(f"Détail des dépenses pour l'alimentation : {total_alimentation}")
print(f"Détail des dépenses pour le transport : {total_transport}")
print(f"Détail des dépenses pour les loisirs : {total_loisirs}")
print(f"La dépense la moins élevée est :{depense_moins} et la dépense la plus élevée est:{depense_plus}")


 

