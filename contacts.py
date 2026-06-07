contacts = {}

with open("contacts.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        contacts = {ligne}
        ligne = ligne.split("|")
        print(f"{ligne[0]} -> {ligne[1]} / {" ".join(ligne[2])} ")
        
demande = input("Entrer un contact : ")
contact = contacts.get(demande)

if contact:
    print(f"{demande} -> {contact[0]} / {contact[1]}")
else:
    print("Contact introuvable")
        

    
