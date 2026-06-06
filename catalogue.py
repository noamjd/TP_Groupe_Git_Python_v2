films = []

# Lit le fichier ligne par ligne (ignorer la première ligne d'en-tête)
with open("catalogue.txt", "r", encoding="utf-8") as fichier:
    next(fichier)
    for ligne in fichier:
        ligne = ligne.strip().split(";")
        films.append(ligne)
        

#Affiche chaque film : "Inception (2010) - Réalisateur : Nolan - Note : 9/10"
for film in films:
    print(f"{film[0]} ({film[1]}) - Réalisateur : {film[2]} - Note : {film[3]}/10")

#Affiche uniquement les films avec une note ≥ 9 
noteSup =[]   
for film in films:
    if int(film[3]) >= 9:
        noteSup.append(film[0])
print(f"Les films ayant une note supérieur ou égale a 9 sont : {noteSup}")
        
#Affiche uniquement les films avec une note ≥ 9
somme = 0
for film in films:
    somme += int(film[3])
moyenne = somme/len(films)
print(f"La note moyenne des films est {moyenne}")

#Ajoute un nouveau film de ton choix à la fin du fichier
with open("catalogue.txt", "a", encoding="utf-8") as fichier:
    fichier.write("Batman;2008;Nolan;10\n")

films = []
with open("catalogue.txt", "r", encoding="utf-8") as fichier:
    next(fichier)
    for ligne in fichier:
        films.append(ligne.strip().split(";"))

#Relit et réaffiche le catalogue complet pour confirmer l'ajout
for film in films:
    print(f"{film[0]} ({film[1]}) - Réalisateur : {film[2]} - Note : {film[3]}")