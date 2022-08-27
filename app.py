# IMPORT

## CONTROLLERS
from controllers.controllers import Controllers
## MODELS
from models.laps import Laps
from models.match import Match
from models.player import Player
from models.tournament import Tournament
## VIEWS
from views.views import Views

# VARIABLES

# CLASSES
class App:

    def __init__(self):
        self.views = Views()
        self.laps = Laps()
        self.match = Match()
        self.player = Player()
        self.tournament = Tournament()
        self.controllers = Controllers(self.views, self.laps, self.match, self.player, self.tournament)
        pass

    def run(self):
        self.controllers
        pass

# EXECUTION
if __name__ == "__main__":
    app = App()
    app.run()
    
