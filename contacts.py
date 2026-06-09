contacts = {}

with open("contacts.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        nom , email , num = ligne.split("|")
        print(f"{nom} -> {email}/{num}")
        contacts[nom] = (email, num)

demande = input("Entrer un nom : ")
secu = demande.title().strip()
if secu in contacts:
    print(contacts[secu])
else:
    print('Contact introuvable')