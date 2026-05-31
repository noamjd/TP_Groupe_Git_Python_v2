try:
    fichier = open("catalogue.txt", "r", encoding="utf-8")
    contenu = fichier.read()
    print(contenu)
    fichier.close()
except FileNotFoundError:
    print("Fichier introuvable")
