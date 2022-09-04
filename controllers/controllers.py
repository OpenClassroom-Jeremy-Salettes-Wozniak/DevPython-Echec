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

################################
############ ACCUEIL ###########
################################
    def accueilControllers(self):
        # VIEWS
        choice = self.view.accueilViews(self)
        if choice == "1":
            # CONTROLLERS
            self.createTournamentControllers()
        elif choice == "2":
            print("Selectionner un tournoi")
        elif choice == "3":
            print("Rapport de tournoi")
            # self.tournament.continueTournament()
        elif choice == "4":
            print("Créer ou modifier joueur")
            # self.tournament.reportTournament()
        elif choice == "5":
            exit()
        else:
            os.system("clear")
            self.view.erreurInput("Veuillez entrer un nombre entre 1 et 4", self.accueilControllers)


################################
########## TOURNAMENT ##########
################################
    def createTournamentControllers(self):
        value = self.view.createTournamentViews(self)
        if value == False:
            self.accueilControllers()
        else:
            tournament = self.tournament(value["name"], value["location"], value["date"], value["laps"], value["laps_instance"], value["players"], value["control_time"], value["description"])
            tournament.save_tournament()
            print(f"Le tournoi {tournament.name} a bien été créé")
            self.accueilControllers()

#################################
############ PLAYER #############
#################################
    def createPlayerControllers(self):
        value = self.view.createPlayerViews(self)
        if value == False:
            self.accueilControllers()
        else:
            pass