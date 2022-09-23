import os

from models.tournaments import Tournament
from models.players import Player
from controllers.controllers import Controller
from views.views import View   


class App:

    def __init__(self, view, controller, tournament, player):
        self.view = view
        self.controller = controller
        self.tournament = tournament
        self.player = player

    def run(self):
        self.controller(self.view, self.tournament, self.player)
        
if __name__ == "__main__":
    os.system("cls")
    app = App(View, Controller, Tournament, Player)
    app.run()
    
