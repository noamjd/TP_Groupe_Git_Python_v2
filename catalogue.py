# Lit le fichier ligne par ligne (ignorer la première ligne d'en-tête)
with open("catalogue.txt", "r", encoding="utf-8") as fichier:
    ligne1 = fichier.readline().split(";")
    ligne2 = fichier.readline().split(";")
    ligne3 = fichier.readline().split(";")
    ligne4 = fichier.readline().split(";")
    ligne5 = fichier.readline().split(";")
    ligne6 = fichier.readline().split(";")

lignes = [ ligne2, ligne3, ligne4, ligne5, ligne6]

#Affiche chaque film : "Inception (2010) - Réalisateur : Nolan - Note : 9/10"
for ligne in lignes:
    print(f"{ligne[0]} ({ligne[1]}) - Réalisateur : {ligne[2]} - Note : {ligne[3]}")

#Affiche uniquement les films avec une note ≥ 9    
for ligne in lignes:
    if int(ligne[3]) >= 9:
        print(ligne[0])
        
#Affiche uniquement les films avec une note ≥ 9
somme = 0
for ligne in lignes:
    somme += int(ligne[3])
    moyenne = somme/len(lignes)
print(moyenne)


    

