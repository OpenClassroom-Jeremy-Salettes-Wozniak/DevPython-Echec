# IMPORT
import os
from models.tournaments import Tournaments
from views.views import Views

# VARIABLES

# CLASSES

class Controllers:
    def __init__(self, views, laps, match, player, tournament):
        self.view = views
        self.lap = laps
        self.match = match
        self.player = player
        self.tournament = tournament
        self.runControllers()
        pass

    def runControllers(self):
        # AJOUTER DES CONTROLLERS ACTIFS
        self.accueilControllers()
        pass

    def accueilControllers(self):
        # VIEWS
        choice = self.view.accueilViews(self)
        if choice == "1":
            # CONTROLLERS
            self.createTournamentControllers()
        elif choice == "2":
            print("choix 2")
            # self.tournament.continueTournament()
        elif choice == "3":
            print("choix 3")
            # self.tournament.reportTournament()
        elif choice == "4":
            exit()
        else:
            os.system("clear")
            self.view.erreurInput("Veuillez entrer un nombre entre 1 et 4", self.accueilControllers)

    def createTournamentControllers(self):
        value = self.view.createTournamentViews(self)
        if value == False:
            self.accueilControllers()
        else:
            tournament = Tournaments(value["name"], value["location"], value["date"], value["laps"], value["laps_instance"], value["players"], value["control_time"], value["description"])
            tournament.save_tournament()
            print(f"Le tournoi {tournament.name} a bien été créé")
            self.accueilControllers()



        # dans le dictionaire, on va recuperer les valeurs des inputs
        # for key, value in self.view.createTournamentViews(self):
        #     print(value)

        # pass

    