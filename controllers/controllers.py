# IMPORT
import os

# VARIABLES

# CLASSES

class Controllers:
    def __init__(self, views, laps, match, player, tournament):
        self.view = views
        self.lap = laps
        self.match = match
        self.player = player
        self.tournament = tournament
        self.accueilControllers()
        pass

    def accueilControllers(self):
        # VIEWS
        choice = self.view.accueilViews()
        if choice == "1":
            # CONTROLLERS
            self.createTournamentControllers()
        elif choice == "2":
            self.tournament.continueTournament()
        elif choice == "3":
            self.tournament.reportTournament()
        elif choice == "4":
            exit()
        else:
            os.system("clear")
            self.view.erreurInput("Veuillez entrer un nombre entre 1 et 4", self.accueilControllers)

    def createTournamentControllers(self):
        # VIEWS
        New_tournament = self.view.createTournamentViews()
        print(New_tournament)
        # IL FAUT CREER LE MODEL

    