# IMPORT

# VARIABLES

# CLASSES
class Controllers:
    def __init__(self, views, laps, matchs, players, tournaments):
        self.views = views
        self.laps = laps
        self.matchs = matchs
        self.players = players
        self.tournaments = tournaments
        pass


    def run(self):
        self.views.run()
        pass