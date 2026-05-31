with open("catalogue.txt", "r", encoding="utf-8") as fichier:
    ligne1 = fichier.readline().split(";")
    ligne2 = fichier.readline().split(";")
    ligne3 = fichier.readline().split(";")
    ligne4 = fichier.readline().split(";")
    ligne5 = fichier.readline().split(";")

lignes = [ligne1, ligne2, ligne3, ligne4, ligne5]

for ligne in lignes:
    print(f"{ligne[0]} ({ligne[1]}) - Réalisateur : {ligne[2]} - Note : {ligne[3]}")
    

    

