import tinydb
import os
import prettytable

from models.tournament import Tournament
class Controller:
    """ Main class of the application """
    
    def __init__(self, view, match, player, tournament, round):
        self.view = view
        self.match = match
        self.player = player
        self.tournament = tournament
        self.round = round
    
    def run(self):
        """ Run the application """
        dict_controller_run = {}
        try:
            os.system("cls")
            # VIEW
            self.view.header(self, "Bienvenue dans le gestionnaire de tournois d'échecs")
            accueil = self.view.accueil(self)
            self.view.footer(self)
            # CONTROLLER
            if accueil["choice"] == 1:
                self.gestion_tournois()
            elif accueil["choice"] == 2:
                self.gestion_joueur()
                pass
            elif accueil["choice"] == 3:
                #TODO: self.gestion_rapport()
                pass
            elif accueil["choice"] == 4:
                exit()
            # DICTIONNAIRE
            dict_controller_run["status"] = True
            dict_controller_run["function"] = f"run() : Accueilize the application"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_run["status"] = False
            dict_controller_run["function"] = print(f"run() : error{e}")
        return dict_controller_run

# TODO: GESTION
    def gestion_tournois(self, *message):
        """ Gestion des tournois """
        dict_controller_gestion_tournois = {}
        try:
            os.system("cls")
            # VIEWS
            self.view.header(self, "Gestion des tournois")
            if message: 
                message = message[0]
                print("### " + message + " ###")
            gestion_tournois = self.view.gestion_tournois(self)
            self.view.footer(self)
            # CONTROLLER
            tournois = self.tournament.get_table_tournaments(self, tinydb)
            if gestion_tournois["choice"] == 1:
                os.system("cls")
                creer_tournoi = self.creer_tournoi()
                os.system("cls")
                if creer_tournoi["status"] == True:
                    self.gestion_tournois("Le tournoi a bien été créé")
                else:
                    self.gestion_tournois("Le tournoi n'a pas été créé")
            elif gestion_tournois["choice"] == 2:
                os.system("cls")
                pass
            elif gestion_tournois["choice"] == 3:
                self.delete_tournament()
            elif gestion_tournois["choice"] == 4:
                os.system("cls")
                self.view.header(self, "Afficher un tournoi | Liste des tournois")
                afficher_tournois = self.afficher_tous_tournois(tournois)
                self.view.footer(self)
                demande_id_tournoi = self.view.demande_id_tournoi(self, afficher_tournois["list_id_tournament"])
                tournoi = self.tournament.get_table_tournament(self, tinydb, demande_id_tournoi["tournament_id"])
                os.system("cls")
                self.view.header(self, "Afficher un tournoi | Tournoi")
                self.afficher_tournoi(tournoi["tournament"], demande_id_tournoi["tournament_id"])
                self.view.footer(self)
                retour_accueil = self.view.retour_accueil(self)
                if retour_accueil["choice"] == 1:
                        self.run()
                else:
                    exit()               
            elif gestion_tournois["choice"] == 5:
                if tournois:
                    os.system("cls")
                    self.view.header(self, "Liste des tournois")
                    self.afficher_tous_tournois(tournois)
                    self.view.footer(self)
                    retour_accueil = self.view.retour_accueil(self)
                    if retour_accueil["choice"] == 1:
                        self.run()
                else:
                    exit()
            elif gestion_tournois["choice"] == 6:
                #TODO:self.lancer_tournoi()
                pass
            elif gestion_tournois["choice"] == 7:
                self.run()
            # DICTIONNAIRE
            dict_controller_gestion_tournois["status"] = True
            dict_controller_gestion_tournois["function"] = f"gestion_tournois() : Manage tournaments"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_gestion_tournois["status"] = False
            dict_controller_gestion_tournois["function"] = print(f"gestion_tournois() : error{e}")
        return dict_controller_gestion_tournois

    def gestion_joueur(self):
        """ Gestion des joueurs """
        dict_controller_gestion_joueur = {}
        try:
            os.system("cls")
            self.view.header(self, "Gestion des joueurs")
            gestion_joueur = self.view.gestion_joueur(self)
            if gestion_joueur["choice"] == 1:
                os.system("cls")
                self.creer_joueur()
            elif gestion_joueur["choice"] == 2:
                #TODO: self.modifier_joueur()
                pass
            elif gestion_joueur["choice"] == 3:
                #TODO: self.delete_player()
                pass
            elif gestion_joueur["choice"] == 4:
                #TODO: self.afficher_joueur()
                pass
            elif gestion_joueur["choice"] == 5:
                #TODO: self.afficher_tous_joueurs()
                pass
            elif gestion_joueur["choice"] == 6:
                self.run()
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_gestion_joueur["status"] = False
            dict_controller_gestion_joueur["function"] = print(f"gestion_joueur() : error{e}")
        return dict_controller_gestion_joueur

    #TODO: def gestion_rapport(self):
        # """ Gestion des rapports """
        # dict_controller_gestion_rapport = {}
        # try:
        #     print("gestion_rapport")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_gestion_rapport["status"] = False
        #     dict_controller_gestion_rapport["function"] = print(f"gestion_rapport() : error{e}")
        # return dict_controller_gestion_rapport

# TODO: TOURNOI
    def creer_tournoi(self):
        """ Créer un tournoi """
        dict_controller_creer_tournoi = {}
        try:
            os.system("cls")
            # VIEW
            self.view.header(self, "Créer un tournoi")
            creer_tournoi = self.view.creer_tournoi(self)
            self.view.footer(self)
            # CONTROLLER
            if creer_tournoi["status"] == True:
                tournament = self.tournament(
                    creer_tournoi["tournament_name"], 
                    creer_tournoi["tournament_location"], 
                    creer_tournoi["tournament_date"], 
                    creer_tournoi["tournament_number_round"],
                    creer_tournoi["tournament_instance_round"],
                    creer_tournoi["tournament_players"],
                    creer_tournoi["tournament_time_control"],
                    creer_tournoi["tournament_description"]
                )
                tournament.save_tournament(tinydb, os)
            # DICTIONNAIRE
            dict_controller_creer_tournoi["status"] = True
            dict_controller_creer_tournoi["function"] = f"creer_tournoi() : Create a tournament"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_creer_tournoi["status"] = False
            dict_controller_creer_tournoi["function"] = print(f"creer_tournoi() : error{e}")
        return dict_controller_creer_tournoi

    def afficher_tous_tournois(self, tournaments):
        """ Afficher tous les tournois """
        dict_controller_afficher_tous_tournois = {}
        try:
            list_id_tournament = []
            all_tournaments = tournaments["tournaments"]
            tables = prettytable.PrettyTable()
            tables.field_names = ["id","Nom", "Lieu", "Date", "Nombre de tours", "Tour en cours", "Joueurs", "Contrôle du temps", "Description"]
            for tournament in all_tournaments:
                list_id_tournament.append(str(tournament.doc_id))
                tables.add_row(
                    [
                        tournament.doc_id,
                        tournament["tournament_name"],
                        tournament["tournament_location"],
                        tournament["tournament_date"],
                        tournament["tournament_number_round"],
                        tournament["tournament_instance_round"],
                        tournament["tournament_players"],
                        tournament["tournament_control_time"],
                        tournament["tournament_description"]
                    ]
                )
            print(tables)             
            # DICTIONNAIRE
            dict_controller_afficher_tous_tournois["list_id_tournament"] = list_id_tournament
            dict_controller_afficher_tous_tournois["status"] = True
            dict_controller_afficher_tous_tournois["function"] = f"afficher_tous_tournois() : Display all tournaments"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_afficher_tous_tournois["status"] = False
            dict_controller_afficher_tous_tournois["function"] = print(f"afficher_tous_tournois() : error{e}")
        return dict_controller_afficher_tous_tournois

    def afficher_tournoi(self, tournament, id):
        """ Get tournament """
        dict_controller_all_tournament = {}
        try:
            prettytable_tournament = prettytable.PrettyTable()
            prettytable_tournament.field_names = ["id", "Nom", "Lieu", "Date", "Nombre de tours", "Tour en cours", "Joueurs", "Contrôle du temps", "Description"]
            prettytable_tournament.add_row([
                id,
                tournament["tournament_name"],
                tournament["tournament_location"],
                tournament["tournament_date"],
                tournament["tournament_number_round"],
                tournament["tournament_instance_round"],
                tournament["tournament_players"],
                tournament["tournament_control_time"],
                tournament["tournament_description"]
            ])
            print(prettytable_tournament)
            # DICTIONNAIRE
            dict_controller_all_tournament["status"] = True
            dict_controller_all_tournament["function"] = f"all_tournament() : Get all tournament"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_all_tournament["status"] = False
            dict_controller_all_tournament["function"] = print(f"all_tournament() : error{e}")
        return dict_controller_all_tournament

    #TODO: def modifier_tournoi(self):
        # """ Modifier un tournoi """
        # dict_controller_modifier_tournoi = {}
        # try:
        #     self.view.header(self, "Modifier un tournoi")
        #     self.all_table_tournaments = self.tournament.all_table_tournaments(tinydb, os)
            
        #     id_tournoi = self.view.demande_id(self)
        #     modifier_tournoi = self.view.modifier_tournoi(self, id_tournoi)

        #     # DICTIONNAIRE
        #     dict_controller_modifier_tournoi["status"] = True
        #     dict_controller_modifier_tournoi["function"] = f"modifier_tournoi() : Modify a tournament"
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_modifier_tournoi["status"] = False
        #     dict_controller_modifier_tournoi["function"] = print(f"modifier_tournoi() : error{e}")
        # return dict_controller_modifier_tournoi
        
    def delete_tournament(self):
        """ Delete a tournament """
        dict_controller_delete_tournament = {}
        try:
            self.view.header(self, "Supprimer un tournoi")
            afficher_tournois = self.afficher_tous_tournois(self.tournament.get_table_tournaments(self, tinydb))
            self.view.footer(self)
            demande_id_tournoi = self.view.demande_id_tournoi(self, afficher_tournois["list_id_tournament"])
            self.tournament.delete_tournament(self, tinydb, demande_id_tournoi["tournament_id"])
            dict_controller_delete_tournament["status"] = True
            dict_controller_delete_tournament["function"] = f"delete_tournament() : Delete a tournament"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_delete_tournament["status"] = False
            dict_controller_delete_tournament["function"] = print(f"delete_tournament() : error{e}")
        return dict_controller_delete_tournament

    #TODO:def lancer_tournoi(self):
        # """ Start a tournament """
        # dict_controller_lancer_tournoi = {}
        # try:
        #     print("lancer_tournoi")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_lancer_tournoi["status"] = False
        #     dict_controller_lancer_tournoi["function"] = print(f"lancer_tournoi() : error{e}")
        # return dict_controller_lancer_tournoi
    
    # def all_table_tournaments(self, tournaments):
    #     """ Get all tournaments """
    #     dict_controller_all_tournaments = {}
    #     try:
    #         all_tournaments = tournaments["tournaments"]
    #         prettytable_tournaments = prettytable.PrettyTable()
    #         prettytable_tournaments.field_names = ["ID", "Nom", "Lieu", "Date", "Nombre de tours", "Tour en cours", "Joueurs", "Contrôle du temps", "Description"]
    #         tableau_id = []
    #         for tournament in all_tournaments:
    #             tournament_id = tournament.doc_id
    #             tableau_id.append(tournament_id)
    #             prettytable_tournaments.add_row([
    #                 tournament_id,
    #                 tournament["tournament_name"],
    #                 tournament["tournament_location"],
    #                 tournament["tournament_date"],
    #                 tournament["tournament_number_round"],
    #                 tournament["tournament_instance_round"],
    #                 tournament["tournament_players"],
    #                 tournament["tournament_control_time"],  
    #                 tournament["tournament_description"]
    #             ])
    #         print(prettytable_tournaments)
    #         # DICTIONNAIRE
    #         dict_controller_all_tournaments["tableau_id"] = tableau_id
    #         dict_controller_all_tournaments["status"] = True
    #         dict_controller_all_tournaments["function"] = f"all_tournaments() : Get all tournaments"
    #     except Exception as e:
    #         # DICTIONNAIRE
    #         dict_controller_all_tournaments["status"] = False
    #         dict_controller_all_tournaments["function"] = print(f"all_tournaments() : error{e}")
    #     return dict_controller_all_tournaments

# TODO: JOUEURS
    def creer_joueur(self):
        """ Create a player """
        dict_controller_creer_joueur = {}
        try:
            os.system("cls")
            self.view.header(self, "Créer un joueur")
            creer_joueur = self.view.creer_joueur(self)
            player = self.player(
                creer_joueur["player_first_name"], 
                creer_joueur["player_last_name"], 
                creer_joueur["date_of_birth"], 
                creer_joueur["sexe"]
            )
            player.save_player(tinydb, os)
            self.view.footer(self)
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_creer_joueur["status"] = False
            dict_controller_creer_joueur["function"] = print(f"creer_joueur() : error{e}")
        return dict_controller_creer_joueur 
    def passa(self):
        pass
    #TODO:def modifier_joueur(self):
        # """ Modify a player """
        # dict_controller_modifier_joueur = {}
        # try:
        #     print("modifier_joueur")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_modifier_joueur["status"] = False
        #     dict_controller_modifier_joueur["function"] = print(f"modifier_joueur() : error{e}")
        # return dict_controller_modifier_joueur

    #TODO:def delete_joueur(self):
        # """ Delete a player """
        # dict_controller_delete_joueur = {}
        # try:
        #     print("delete_joueur")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_delete_joueur["status"] = False
        #     dict_controller_delete_joueur["function"] = print(f"delete_joueur() : error{e}")
        # return dict_controller_delete_joueur

    #TODO:def afficher_joueur(self):
        # """ Display a player """
        # dict_controller_afficher_joueur = {}
        # try:
        #     print("afficher_joueur")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_afficher_joueur["status"] = False
        #     dict_controller_afficher_joueur["function"] = print(f"afficher_joueur() : error{e}")
        # return dict_controller_afficher_joueur

    #TODO:def afficher_tous_joueurs(self):
        # """ Display all players """
        # dict_controller_afficher_tous_joueurs = {}
        # try:
        #     print("afficher_tous_joueurs")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_afficher_tous_joueurs["status"] = False
        #     dict_controller_afficher_tous_joueurs["function"] = print(f"afficher_tous_joueurs() : error{e}")
        # return dict_controller_afficher_tous_joueurs
    
    #TODO:def all_table_players(self, players):
        # """ 
        # Get all players 
        # """
        # dict_controller_all_players = {}
        # try:
        #     all_players = players["players"]
        #     prettytable_players = prettytable.PrettyTable()
        #     prettytable_players.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]
        #     tableau_id = []
        #     for player in all_players:
        #         player_id = player.doc_id
        #         tableau_id.append(player_id)
        #         prettytable_players.add_row([
        #             player_id,
        #             player["player_last_name"],
        #             player["player_first_name"],
        #             player["date_of_birth"],
        #             player["sexe"],
        #             player["ranking"]
        #         ])
        #     print(prettytable_players)
        #     # DICTIONNAIRE
        #     dict_controller_all_players["tableau_id"] = tableau_id
        #     dict_controller_all_players["status"] = True
        #     dict_controller_all_players["function"] = f"all_players() : Get all players"
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_all_players["status"] = False
        #     dict_controller_all_players["function"] = print(f"all_players() : error{e}")
        # return dict_controller_all_players

    #TODO:def table_player(self, player, id):
        # """ Get all player """
        # dict_controller_all_player = {}
        # try:
        #     prettytable_player = prettytable.PrettyTable()
        #     prettytable_player.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]
        #     prettytable_player.add_row([
        #         id,
        #         player["player_last_name"],
        #         player["player_first_name"],
        #         player["date_of_birth"],
        #         player["sexe"],
        #         player["ranking"]
        #     ])
        #     print(prettytable_player)
        #     # DICTIONNAIRE
        #     dict_controller_all_player["status"] = True
        #     dict_controller_all_player["function"] = f"all_player() : Get all player"
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_all_player["status"] = False
        #     dict_controller_all_player["function"] = print(f"all_player() : error{e}")

# TODO: RAPPORTS
    #TODO:def rapport_tournoi(self):
        # """ Report a tournament """
        # dict_controller_rapport_tournoi = {}
        # try:
        #     print("rapport_tournoi")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_rapport_tournoi["status"] = False
        #     dict_controller_rapport_tournoi["function"] = print(f"rapport_tournoi() : error{e}")
        # return dict_controller_rapport_tournoi

    #TODO:def rapport_joueur(self):
        # """ Report a player """
        # dict_controller_rapport_joueur = {}
        # try:
        #     print("rapport_joueur")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_rapport_joueur["status"] = False
        #     dict_controller_rapport_joueur["function"] = print(f"rapport_joueur() : error{e}")
        # return dict_controller_rapport_joueur

    #TODO:def rapport_match(self):
        # """ Report a match """
        # dict_controller_rapport_match = {}
        # try:
        #     print("rapport_match")
        # except Exception as e:
        #     # DICTIONNAIRE
        #     dict_controller_rapport_match["status"] = False
        #     dict_controller_rapport_match["function"] = print(f"rapport_match() : error{e}")
        # return dict_controller_rapport_match