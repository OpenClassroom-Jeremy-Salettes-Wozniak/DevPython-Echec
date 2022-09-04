# IMPORT
import os

## CONTROLLERS
from controllers.controllers import Controllers
## MODELS
from models.laps import Laps
from models.matchs import Matchs
from models.players import Players
from models.tournaments import Tournaments
## VIEWS
from views.views import Views

# VARIABLES

# CLASSES
class App:

    def __init__(self, controllers, views, laps, match, player, tournament):
        self.views = views
        self.laps = laps
        self.match = match
        self.player = player
        self.tournament = tournament
        self.controllers = controllers(self.views, self.laps, self.match, self.player, self.tournament)
        

# EXECUTION
if __name__ == "__main__":
    App(Controllers, Views, Laps, Matchs, Players, Tournaments)