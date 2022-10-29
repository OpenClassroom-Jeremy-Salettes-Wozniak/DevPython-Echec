import time
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
                tournois = self.modifier_tournoi(tournois)
                os.system("cls")
                if tournois["status"] == True:
                    self.gestion_tournois("Le tournoi a bien été modifié")
                else:
                    self.gestion_tournois("Le tournoi n'a pas été modifié")
            elif gestion_tournois["choice"] == 3:
                self.delete_tournament(tournois)
                self.gestion_tournois(f"Le tournoi a bien été supprimé")
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
                self.lancer_tournoi()
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

    def gestion_joueur(self, *message):
        """ Gestion des joueurs """
        dict_controller_gestion_joueur = {}
        try:
            os.system("cls")
            db_player = self.player.get_table_players(self, tinydb)
            self.view.header(self, "Gestion des joueurs")
            if message:
                message = message[0]
                print("### " + message + " ###")
            gestion_joueur = self.view.gestion_joueur(self)
            if gestion_joueur["choice"] == 1:
                os.system("cls")
                self.creer_joueur()
                self.gestion_joueur("Le joueur a bien été créé")
            elif gestion_joueur["choice"] == 2:
                self.modifier_joueur()
            elif gestion_joueur["choice"] == 3:
                self.delete_joueur(db_player)
                self.gestion_joueur(f"Le joueur a bien été supprimé")
            elif gestion_joueur["choice"] == 4:
                os.system("cls")
                self.view.header(self, "Afficher un joueur | Liste des joueurs")
                afficher_tous_joueurs = self.afficher_tous_joueurs(db_player["players"])
                self.view.footer(self)
                demande_id_joueur = self.view.demande_id_joueur(self, afficher_tous_joueurs["tableau_id"])
                joueur = self.player.get_table_player(self, tinydb, demande_id_joueur["joueur_id"])
                os.system("cls")
                self.view.header(self, "Afficher un joueur | Joueur")
                self.afficher_joueur(joueur["players"], demande_id_joueur["joueur_id"])
                self.view.footer(self)
                retour_accueil = self.view.retour_accueil(self)
                if retour_accueil["choice"] == 1:
                        self.run()
                else:
                    exit()
            elif gestion_joueur["choice"] == 5:
                self.afficher_tous_joueurs(db_player["players"])
                accueil = self.view.retour_accueil(self)
                if accueil["choice"] == 1:
                    self.run()
                else:
                    exit()
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

    def modifier_tournoi(self, tournaments):
        """ Modifier un tournoi """
        dict_controller_modifier_tournoi = {}
        try:
            self.view.header(self, "Modifier un tournoi")
            # VIEW
            afficher_tournois = self.afficher_tous_tournois(tournaments)
            self.view.footer(self)
            demande_id_tournoi = self.view.demande_id_tournoi(self, afficher_tournois["list_id_tournament"])
            tournoi = self.tournament.get_table_tournament(self, tinydb, demande_id_tournoi["tournament_id"])
            self.view.header(self, "Afficher un tournoi | Tournoi")
            self.afficher_tournoi(tournoi["tournament"], demande_id_tournoi["tournament_id"])
            self.view.footer(self)
            nouveau_tournoi = self.view.modifier_tournoi(self, tournoi["tournament"])
            self.tournament.modify_tournament(self, nouveau_tournoi["tournament"], tinydb, demande_id_tournoi["tournament_id"])
            # DICTIONNAIRE
            dict_controller_modifier_tournoi["status"] = True
            dict_controller_modifier_tournoi["function"] = f"modifier_tournoi() : Modify a tournament"
            # DICTIONNAIRE
            dict_controller_modifier_tournoi["status"] = True
            dict_controller_modifier_tournoi["function"] = f"modifier_tournoi() : Modify a tournament"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_modifier_tournoi["status"] = False
            dict_controller_modifier_tournoi["function"] = print(f"modifier_tournoi() : error{e}")
        return dict_controller_modifier_tournoi
        
    def delete_tournament(self, db_player):
        """ Delete a tournament """
        dict_controller_delete_tournament = {}
        try:
            print("db_player", db_player)
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

    def lancer_tournoi(self):
        """ Start a tournament """
        dict_controller_lancer_tournoi = {}
        try:
            # SELECTION DU TOURNOI
            os.system("cls")
            self.view.header(self, "Lancement du tournois | Sélection du tournoi")
            afficher_tournois = self.afficher_tous_tournois(self.tournament.get_table_tournaments(self, tinydb))
            self.view.footer(self)
            if afficher_tournois["list_id_tournament"] == []:
                print("Aucun tournoi à lancer")
                input("Appuyer sur une touche pour continuer")
                self.gestion_tournois()
            demande_id_tournoi = self.view.demande_id_tournoi(self, afficher_tournois["list_id_tournament"])
            # AFFICHAGE DU TOURNOI
            os.system("cls")
            self.view.header(self, f"Lancement du tournois | Tournoi sélectionné : {demande_id_tournoi['tournament_id']}")
            tournoi = self.tournament.get_table_tournament(self, tinydb, demande_id_tournoi["tournament_id"])
            self.afficher_tournoi(tournoi["tournament"], demande_id_tournoi["tournament_id"])
            self.view.footer(self)
            #AFFICHAGE DU MENU DU TOURNOI
            os.system("cls")
            self.view.header(self, f"Lancement du tournois | Menu du tournoi")
            choice_menu_tournoi = self.view.menu_tournoi(self, demande_id_tournoi["tournament_id"])

            if choice_menu_tournoi["choice"] == "1":
                # LANCER LE TOURNOI
                print(tournoi)
                self.ajouter_joueurs_tournoi(tournoi["tournament"])
            elif choice_menu_tournoi["choice"] == "2":
                self.supprimer_joueurs_tournoi(tournoi["tournament"])
            elif choice_menu_tournoi["choice"] == "3":
                # SI LE NOMBRE DE JOUEURS EST INFERIEUR A 8
                if len(tournoi["tournament"]["tournament_players"]) < 8:
                    print("Il faut au minimum 8 joueurs pour lancer le tournoi")
                    # Attendre 3 secondes
                    time.sleep(3)
                    self.lancer_tournoi()
                else:
                    self.tournoi_lancer()
            elif choice_menu_tournoi["choice"] == "4":
                self.gestion_tournois()
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_lancer_tournoi["status"] = False
            dict_controller_lancer_tournoi["function"] = print(f"lancer_tournoi() : error{e}")
        return dict_controller_lancer_tournoi

    def ajouter_joueurs_tournoi(self, tournament):
        """ Add players to a tournament """
        dict_controller_ajouter_joueurs_tournoi = {}
        try:
            # SELECTION DU TOURNOI
            os.system("cls")
            self.view.header(self, "Lancement du tournois | Ajouter un joueurs")
            db_player = self.player.get_table_players(self, tinydb)
            afficher_joueurs = self.afficher_tous_joueurs(db_player["players"])
            self.view.footer(self)
            demande_id_joueur = self.view.demande_id_joueur(self, afficher_joueurs["tableau_id"])
            # Recupere la liste des joueurs du tournoi
            list_players_tournament = tournament["tournament_players"]
            # Ajoute le joueur selectionné à la liste des joueurs du tournoi
            if demande_id_joueur["joueur_id"] not in list_players_tournament:
                list_players_tournament.append(demande_id_joueur["joueur_id"])
            else:
                print("Ce joueur est déjà dans le tournoi")
                input("Appuyer sur une touche pour continuer")
                self.gestion_tournois()
            tournoi = {
                "tournament_name": tournament["tournament_name"],
                "tournament_location": tournament["tournament_location"],
                "tournament_date": tournament["tournament_date"],
                "tournament_number_round": tournament["tournament_number_round"],
                "tournament_instance_round": tournament["tournament_instance_round"],
                "tournament_players" : list_players_tournament,
                "tournament_control_time": tournament["tournament_control_time"],
                "tournament_description": tournament["tournament_description"],
            }
            self.tournament.add_player_tournament(self, tinydb, tournament.doc_id, tournoi)
            dict_controller_ajouter_joueurs_tournoi["status"] = True
            dict_controller_ajouter_joueurs_tournoi["function"] = f"ajouter_joueurs_tournoi() : Add players to a tournament"

        except Exception as e:
            # DICTIONNAIRE
            dict_controller_ajouter_joueurs_tournoi["status"] = False
            dict_controller_ajouter_joueurs_tournoi["function"] = print(f"ajouter_joueurs_tournoi() : error{e}")

    def supprimer_joueurs_tournoi(self, tournament):
        """ Delete players to a tournament """
        dict_controller_supprimer_joueurs_tournoi = {}
        try:
            os.system("cls")
            self.view.header(self, "Lancement du tournois | Supprimer un joueurs")
            # Recupere la liste des joueurs du tournoi
            list_players_tournament = tournament["tournament_players"]
            print(list_players_tournament)
            # Supprime le joueur selectionné à la liste des joueurs du tournoi
            if list_players_tournament != []:
                demande_id_joueur = self.view.demande_id_joueur(self, list_players_tournament)
                list_players_tournament.remove(demande_id_joueur["joueur_id"])
            else:
                print("Il n'y a pas de joueurs dans ce tournoi")
                input("Appuyer sur une touche pour continuer")
                self.gestion_tournois()
            tournoi = {
                "tournament_name": tournament["tournament_name"],
                "tournament_location": tournament["tournament_location"],
                "tournament_date": tournament["tournament_date"],
                "tournament_number_round": tournament["tournament_number_round"],
                "tournament_instance_round": tournament["tournament_instance_round"],
                "tournament_players" : list_players_tournament,
                "tournament_control_time": tournament["tournament_control_time"],
                "tournament_description": tournament["tournament_description"],
            }
            self.tournament.add_player_tournament(self, tinydb, tournament.doc_id, tournoi)
            dict_controller_supprimer_joueurs_tournoi["status"] = True
            dict_controller_supprimer_joueurs_tournoi["function"] = f"supprimer_joueurs_tournoi() : Delete players to a tournament"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_supprimer_joueurs_tournoi["status"] = False
            dict_controller_supprimer_joueurs_tournoi["function"] = print(f"supprimer_joueurs_tournoi() : error{e}")

    #TODO: def tournoi_lancer(self):
        # pass

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

    def modifier_joueur(self):
        """ Modify a player """
        dict_controller_modifier_joueur = {}
        try:
            db_player = self.player.get_table_players(self, tinydb)
            self.view.header(self, "Modifier un joueur | Liste des joueurs")
            afficher_joueurs = self.afficher_tous_joueurs(db_player["players"])
            self.view.footer(self)
            demande_id_joueur = self.view.demande_id_joueur(self, afficher_joueurs["tableau_id"])
            joueur = self.player.get_table_player(self, tinydb, demande_id_joueur["joueur_id"])
            self.view.header(self, "Modifier un joueur | Joueur")
            self.afficher_joueur(joueur["players"], demande_id_joueur["joueur_id"])
            self.view.footer(self)
            nouveau_joueur = self.view.modifier_joueur(self, joueur["players"])
            self.player.modify_player(self, nouveau_joueur["player"], tinydb, demande_id_joueur["joueur_id"])
            self.gestion_joueur("Le joueur a été modifié")
            dict_controller_modifier_joueur["status"] = True
            dict_controller_modifier_joueur["function"] = f"modifier_joueur() : Modify a player"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_modifier_joueur["status"] = False
            dict_controller_modifier_joueur["function"] = print(f"modifier_joueur() : error{e}")
        return dict_controller_modifier_joueur

    def delete_joueur(self , db_player):
        """ Delete a player """
        dict_controller_delete_joueur = {}
        try:
            self.view.header(self, "Supprimer un joueur")
            list_id = self.afficher_tous_joueurs(db_player["players"])
            self.view.footer(self)
            demande_id_joueur = self.view.demande_id_joueur(self, list_id["tableau_id"])
            print("demande_id_joueur", demande_id_joueur)
            self.player.delete_player(self, tinydb, demande_id_joueur["joueur_id"])
            dict_controller_delete_joueur["status"] = True
            dict_controller_delete_joueur["function"] = f"delete_joueur() : Delete a player"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_delete_joueur["status"] = False
            dict_controller_delete_joueur["function"] = print(f"delete_joueur() : error{e}")
        return dict_controller_delete_joueur

    def afficher_tous_joueurs(self, players):
        """ 
        Get all players 
        """
        dict_controller_all_players = {}
        try:
            all_players = players
            prettytable_players = prettytable.PrettyTable()
            prettytable_players.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]
            tableau_id = []
            for player in all_players:
                player_id = player.doc_id
                tableau_id.append(str(player_id))
                prettytable_players.add_row([
                    player_id,
                    player["player_last_name"],
                    player["player_first_name"],
                    player["date_of_birth"],
                    player["sexe"],
                    player["ranking"]
                ])
            print(prettytable_players)
            # DICTIONNAIRE
            dict_controller_all_players["tableau_id"] = tableau_id
            dict_controller_all_players["status"] = True
            dict_controller_all_players["function"] = f"all_players() : Get all players"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_all_players["status"] = False
            dict_controller_all_players["function"] = print(f"all_players() : error{e}")
        return dict_controller_all_players

    def afficher_joueur(self, player, id):
        """ Get all player """
        dict_controller_all_player = {}
        try:
            prettytable_player = prettytable.PrettyTable()
            prettytable_player.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Sexe", "Classement"]
            prettytable_player.add_row([
                id,
                player["player_last_name"],
                player["player_first_name"],
                player["date_of_birth"],
                player["sexe"],
                player["ranking"]
            ])
            print(prettytable_player)
            # DICTIONNAIRE
            dict_controller_all_player["status"] = True
            dict_controller_all_player["function"] = f"all_player() : Get all player"
        except Exception as e:
            # DICTIONNAIRE
            dict_controller_all_player["status"] = False
            dict_controller_all_player["function"] = print(f"all_player() : error{e}")


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