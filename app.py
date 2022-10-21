from controllers import controller
from views import view
from models import match
from models import player
from models import tournament
from models import round

class App:
    """ Main class of the application """

    def __init__(self):
        self.view = view.View
        self.match = match.Match
        self.player = player.Player
        self.tournament = tournament.Tournament
        self.round = round.Round
        self.controller = controller.Controller(self.view, self.match, self.player, self.tournament, self.round)

    def run(self):
        """ Run the application """
        self.controller.run()

if __name__ == "__main__":
    app = App()
    app.run()
    
