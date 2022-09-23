from re import RegexFlag
from time import time


class View:
    
    def __init__(self):
        pass

    def titre(self, message):
        print("----------------------------------------------------------------------------------")
        print(f"{message}")
        print("----------------------------------------------------------------------------------")

    def accueil(self, message=None):
        if message != None:
            print(message)
        print("1. Créer un nouveau tournoi")
        print("2. Créer un nouveau joueur")
        print("3. Sélectionner un tournoi")
        print("4. Rapport")
        print("5. Quitter")
        print("----------------------------------------------------------------------------------")

    def creerTournoi(self):
        tournament_name = input("Nom du tournoi : ")
        while tournament_name == "":
            print(f"Le nom du tournoi est obligatoire")
            tournament_name = input("Nom du tournoi : ")
            
        tournament_location = input("Lieu du tournoi : ")
        while tournament_location == "":
            print(f"Le lieu du tournoi est obligatoire")
            tournament_location = input("Lieu du tournoi : ")

        tournament_date = input("Date du tournoi au format jj/mm/aaaa : ")
        # ou si on veut que l'utilisateur ne puisse pas entrer autre chose qu'une date au format jj/mm/aaaa
        while tournament_date == "" or not tournament_date[2] == "/" or not tournament_date[5] == "/":
            if tournament_date == "":
                print(f"La date du tournoi est obligatoire")
            else:
                print(f"La date du tournoi doit être au format jj/mm/aaaa")
            tournament_date = input("Date du tournoi : ")
            
        print("Contrôle du temps : " )
        print(" 1. Bullet (1 min + 0 sec)")
        print(" 2. Blitz (3 min + 2 sec)")
        print(" 3. Coup rapide (5 min + 3 sec)")
        tournament_time_control = input("Veuillez selectionner le numéro de votre choix : ")
        while tournament_time_control == "":
            print(f"Le contrôle du temps est obligatoire")
            tournament_time_control = input("Contrôle du temps : ")
        while tournament_time_control != "1" and tournament_time_control != "2" and tournament_time_control != "3":
            tournament_time_control = input("Veuillez saisir un choix valide : ")
        if tournament_time_control == "1":
            tournament_time_control = "Bullet"
        elif tournament_time_control == "2":
            tournament_time_control = "Blitz"
        elif tournament_time_control == "3":
            tournament_time_control = "Coup rapide"

        tournament_description = input("Description du tournoi : ")
        while tournament_description == "":
            print(f"La description du tournoi est obligatoire")
            tournament_description = input("Description du tournoi : ")

        tournament = {
            "tournament_name": tournament_name,
            "tournament_location": tournament_location,
            "tournament_date": tournament_date,
            "tournament_time_control": tournament_time_control,
            "tournament_description": tournament_description
        }
        return tournament

    def creerJoueur(self):
        player_last_name = input("Nom du joueur : ")
        while player_last_name == "":
            print(f"Le nom du joueur est obligatoire")
            player_last_name = input("Nom du joueur : ")
            
        player_first_name = input("Prénom du joueur : ")
        while player_first_name == "":
            print(f"Le prénom du joueur est obligatoire")
            player_first_name = input("Prénom du joueur : ")

        player_birth_date = input("Date de naissance du joueur au format jj/mm/aaaa : ")
        while (player_birth_date == "" or len(player_birth_date) != 10 and player_birth_date != "jj/mm/aaaa"):
            if player_birth_date == "":
                print(f"La date de naissance du joueur est obligatoire")
            else:
                print(f"La date de naissance du joueur doit être au format jj/mm/aaaa")
            player_birth_date = input("Date de naissance du joueur : ")

        player_sexe = input("Sexe du joueur M ou F : ")
        while player_sexe == "" or not player_sexe == "M" and not player_sexe == "F":
            if player_sexe == "":
                print(f"Le sexe du joueur est obligatoire")
            else:
                print(f"Le sexe du joueur doit être M ou F")
            player_sexe = input("Sexe du joueur : ")
        
        player = {
            "player_last_name": player_last_name,
            "player_first_name": player_first_name,
            "player_birth_date": player_birth_date,
            "player_sexe": player_sexe
        }
        return player


















































































































# import os
# from time import time
# from models.tournaments import Tournament


# class View:
    
#     def __init__(self):
#         """Constructor for View"""
#         print("View")


#     def afficher(self, titre):
#         print("----------------------------------------------------------------------------------")
#         print(f"{titre}")
#         print("----------------------------------------------------------------------------------")

#     def erreur(self, message, function, functionAtive=False):
#         """Affiche un message d'erreur et renvoie la fonction en cours"""
#         os.system("cls")
#         print(f"Erreur : {message}")
#         if functionAtive:
#             return function()
        
        
#     def afficherMenu(self):        
#         print("1. Créer un tournoi")
#         print("2. Créer un joueur")
#         print("3. Selectionne un tournoi")
#         print("4. Rapport")
#         print("5. Quitter")
#         print("")
#         choice = input("Veuillez selectionner le numéro de votre choix : ")
#         return choice

#     def creerTournoi(self, titre):
#         self.afficher(titre)
#         tournament_name = input("Nom du tournoi : ")
#         tournament_location = input("Lieu du tournoi : ")
#         tournament_date = input("Date du tournoi : ")
#         time_control = {
#             "1": "Bullet",
#             "2": "Blitz",
#             "3": "Coup rapide"
#         }
#         print(f"1. Bullet")
#         print(f"2. Blitz")
#         print(f"3. Coup rapide")
#         choice = input("Veuillez selectionner le numéro de votre choix : ")
#         tournament_time_control = time_control[choice]
#         tournament_description = input("Description du tournoi : ")

#         tournament = {
#             "tournament_name": tournament_name,
#             "tournament_location": tournament_location,
#             "tournament_date": tournament_date,
#             "tournament_time_control": tournament_time_control,
#             "tournament_description": tournament_description
#         }
#         print("Le tournoi a bien été créé")
#         return tournament
    
#     def creerUnJoueur(self, titre):
#         self.afficher(titre)
#         nom = input("Nom du joueur : ")
#         prenom = input("Prénom du joueur : ")
#         date = input("Date de naissance : ")
#         sexe = input("Sexe : ")
#         classement = input("Classement : ")
#         joueur = {
#             "nom": nom,
#             "prenom": prenom,
#             "date": date,
#             "sexe": sexe,
#             "classement": classement
#         }
#         if joueur:
#             print("Le joueur a bien été créé")
#         return joueur


#     def selectionnerTournoi(self, tournois, titre):
#         self.afficher(titre)
#         print("Liste des tournois :")
#         for tournoi in tournois:
#             print(f"{tournoi['id']} - {tournoi['nom']}")
#         print("")
#         idTournoi = input("Veuillez saisir l'id du tournoi : ")
#         return idTournoi

#     def afficherTournoi(self, tournoi):
#         self.afficher("Affichage du tournoi")
#         print(f"Nom : {tournoi['nom']}")
#         print(f"Lieu : {tournoi['lieu']}")
#         print(f"Date : {tournoi['date']}")
#         print(f"Nombre de tour : {tournoi['nbTour']}")
#         print(f"matchs : {tournoi['matchs']}")
#         print(f"players : {tournoi['players']}")
#         print(f"Temps de contrôle : {tournoi['temps']}")
#         print(f"Description : {tournoi['description']}")
#         print("")
#         print("1. Ajouter un joueur")
#         print("2. Lancer le tournoi")
#         print("3. Rapport du tournoi")
#         print("4. Retour")
#         print("")
#         return input("Veuillez faire votre choix : ")

#     def ajouterJoueur(self, joueurs):
#         self.afficher("Ajout d'un joueur")
#         print("Liste des joueurs :")
#         for joueur in joueurs:
#             print(f"{joueur['id']} - {joueur['nom']} {joueur['prenom']}")
#         print("")
#         idJoueur = input("Veuillez saisir l'id du joueur : ")
#         return idJoueur

#     def lancerTournoi(self, tournoi):
#         # LANCER 
#         print("Lancement du tournoi")


#     def rapportTournoi(self, tournoi):
#         # RAPPORT
#         print("Rapport du tournoi")
        
#     def rapport(self):
#         # RAPPORT
#         self.afficher("Rapport")
#         print("1. Rapport des joueurs")
#         print("2. Rapport des tournois")
#         print("3. Rapport des matchs")
#         print("4. Retour")
#         print("")
#         return input("Veuillez faire votre choix : ")
    
