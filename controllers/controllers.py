import os


from models.tournaments import Tournament

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

    def selectionnerTournoi(self):
        os.system("cls")
        self.view.titre(self, "Selectionner un tournoi")
        tournois = self.tournament.tournaments_load(self)
        id = self.view.selectionnerTournoi(self, tournois)
        self.affichageTournoi(id)

    def affichageTournoi(self, id):
        os.system("cls")
        self.view.titre(self, "Affichage du tournoi")
        tournoi = self.tournament.tournament_load(self, id)
        self.view.afficherTournoi(self, tournoi)
        print("1 - Ajouter un joueur")
        print("2 - Lancer le tournoi")
        print("3 - Retour")
        choix = input(f"Veuillez selectionner le numéro de votre choix : ")
        if choix == "1":
            self.ajouterJoueur(id)
        elif choix == "2":
            self.lancerTournoi(id)
        elif choix == "3":
            self.accueil()