# IMPORT

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
        choice = self.view.accueilViews()
        if choice == "1":
            self.tournament.createTournament()

        pass
