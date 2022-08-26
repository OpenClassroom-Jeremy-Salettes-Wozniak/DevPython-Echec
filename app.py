# IMPORT

## CONTROLLERS
from controllers.controllers import Controllers
## MODELS
from models.joueurs import Joueurs
from models.matchs import Matchs
from models.tournois import Tournois
from models.tours import Tours
## VIEWS
from views.views import Views

# VARIABLES

# CLASSES
class App:

    def __init__(self):
        self.views = Views()
        self.joueurs = Joueurs()
        self.matchs = Matchs()
        self.tournois = Tournois()
        self.tours = Tours()
        self.controllers = Controllers(self.views, self.joueurs, self.matchs, self.tournois, self.tours)

    def run(self):
        self.controllers.run()
        pass

# EXECUTION
if __name__ == "__main__":
    app = App()
    app.run()
    
