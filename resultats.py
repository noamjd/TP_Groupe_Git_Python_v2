import csv 
points_parisfc = 0
points_lyonunited = 0
with open("resultats.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        if ligne['equipe'] == 'Paris FC':
            try:
                points_parisfc = 3*int(ligne['victoires']) + int(ligne['nuls'])
            except ValueError:
                print(f"Impossible de caluler les points de l'équipe : {ligne}")
        if ligne['equipe'] == 'Lyon United':
            try:
                points_lyonunited = 3*int(ligne['victoires']) + int(ligne['nuls'])
            except ValueError:
                print(f"Impossible de caluler les points de l'équipe : {ligne}")                                    
print(f"Les points du paris fc sont : {points_parisfc}") 
print(f"Les points du lyon united sont : {points_lyonunited}")