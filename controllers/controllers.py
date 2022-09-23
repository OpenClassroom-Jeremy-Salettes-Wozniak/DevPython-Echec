import os
from pydoc import plain

class Controller:

    def __init__(self, view, tournament, player):
        self.view = view
        self.tournament = tournament
        self.player = player
        self.accueil()

    def accueil(self, message=None):
        titre = "Bienvenue dans le gestionnaire de tournoi d'échec"
        os.system("cls")
        if message != None:
            self.view.titre(self, titre)
            self.view.accueil(self, message)
        else:
            self.view.titre(self, titre)
            self.view.accueil(self)

        choix = input(f"Veuillez selectionner le numéro de votre choix : ")

        if choix == "1":
            self.creerTournoi()
        elif choix == "2":
            self.creerJoueur()	
        elif choix == "3":
            self.selectionnerTournoi()
        elif choix == "4":
            self.rapport()
        elif choix == "5":
            exit()
        else:
            os.system("cls")
            self.accueil("---- Veuillez selectionner un choix valide ----")


    os.system("tv fichier.csv")
    def creerTournoi(self):
        try: 
            os.system("cls")
            self.view.titre(self, "Créer un tournoi")
            tournoi = self.view.creerTournoi(self)
            new_tournois = self.tournament(
                tournoi["tournament_name"], 
                tournoi["tournament_location"], 
                tournoi["tournament_date"], 
                tournoi["tournament_time_control"], 
                tournoi["tournament_description"],
                )
            new_tournois.tournament_save()
            self.accueil("---- Le tournoi a été créé avec succès ----")

        except:
            os.system("cls")
            self.creerTournoi()

    def creerJoueur(self):
        try:
            self.view.titre(self, "Créer un joueur")
            joueur = self.view.creerJoueur(self)
            print(joueur)
            new_joueur = self.player(
                joueur["player_last_name"], 
                joueur["player_first_name"],
                joueur["player_birth_date"],
                joueur["player_sexe"],
            )
            new_joueur.player_save()
            self.accueil("---- Le joueur a été créé avec succès ----")
        except Exception as e:
            print(e)







































































# import os
# from secrets import choice
# from statistics import mode


# class Controller:

#     def __init__(self, view, tournament):
#         self.view = view()
#         self.tournament = tournament
#         self.accueil()
    
#     def accueil(self):
#         """Affiche le menu principal"""
#         os.system("cls")
#         self.view.afficher(self.view, "Bienvenue dans le gestionnaire de tournoi d'échec")
#         choice = self.view.afficherMenu()
#         if choice == "1":
#             self.creerTournoi()
#         elif choice == "2":
#             self.creerUnJoueur()
#         elif choice == "3":
#             self.selectionnerTournoi()
#         elif choice == "4":
#             self.rapport()
#         elif choice == "5":
#             exit()
#         else:
#             os.system("cls")
#             self.view.erreur("Veuillez selectionner un numéro valide", self.accueil())

#     def creerTournoi(self):
#         """Créer un tournoi"""
#         os.system("cls")
#         self.view.afficher("Créer un tournoi")
#         tournament = self.view.creerTournoi()
#         self.tournament.createTournament(tournament)
#         self.accueil()
        