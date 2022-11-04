import re

from models.player import Player


class View:
    """ View class """
    def __init__(self):
        pass
    
#TODO: VIEW INTERFACE
    def header(self, message):
        """ Affiche le titre """
        dict_view_header = {}
        try:
            print(f"=" * 160)
            print(f"{message}".center(160))
            print(f"=" * 160)
            dict_view_header["status"] = True
            dict_view_header["message"] = f"{message}"
            dict_view_header["function"] = f"header() : Affiche le titre"
        except Exception as e:
            dict_view_header["status"] = False
            dict_view_header["message"] = f"{message}"
            dict_view_header["function"] = print(f"header() : {e}")
        return dict_view_header

    def footer(self):
        """ Affiche le pied de page """
        dict_view_footer = {}
        try:
            print(f"=" * 160)
            dict_view_footer["status"] = True
            dict_view_footer["function"] = f"footer() : Affiche le pied de page"
        except Exception as e:
            dict_view_footer["status"] = False
            dict_view_footer["function"] = print(f"footer() : {e}")
        return dict_view_footer

    def accueil(self, *message):
        """ Affiche l'accueil """
        dict_view_accueil = {}
        try:
            print(f"1. Gestions des tournois")
            print(f"2. Gestions des joueurs")
            print(f"3. Gestions des rapports")
            print(f"4. Quitter")
            print(f"=" * 160)
            choice = ""
            while choice not in ["1", "2", "3"]:
                choice = input(f"Veuillez choisir une option : ")
            dict_view_accueil["status"] = True
            dict_view_accueil["message"] = f"{message}"
            dict_view_accueil["function"] = f"accueil() : Affiche l'accueil"
            dict_view_accueil["choice"] = int(choice)
        except Exception as e:
            dict_view_accueil["status"] = False
            dict_view_accueil["message"] = f"{message}"
            dict_view_accueil["function"] = print(f"accueil() : {e}")
        return dict_view_accueil

    def retour_accueil(self):
        """ Affiche le message de retour à l'accueil """
        dict_view_retour_accueil = {}
        try:
            print(f"Voulez-vous retourner à l'accueil ?")
            print(f"1. Oui")
            print(f"2. Non")
            choice = ""
            while choice not in ["1", "2"]:
                choice = input(f"Veuillez choisir une option : ")
            if choice == "1":
                dict_view_retour_accueil["status"] = True
                dict_view_retour_accueil["function"] = f"retour_accueil() : Affiche le message de retour à l'accueil"
                dict_view_retour_accueil["choice"] = True
            else:
                dict_view_retour_accueil["status"] = True
                dict_view_retour_accueil["function"] = f"retour_accueil() : Affiche le message de retour à l'accueil"
                dict_view_retour_accueil["choice"] = False
                
            dict_view_retour_accueil["status"] = True
            dict_view_retour_accueil["function"] = f"retour_accueil() : Affiche le message de retour à l'accueil"
        except Exception as e:
            dict_view_retour_accueil["status"] = False
            dict_view_retour_accueil["function"] = print(f"retour_accueil() : {e}")
        return dict_view_retour_accueil

#TODO: VIEW TOURNOI
    def gestion_tournois(self, *message):
        """ Affiche le menu de gestion des tournois """
        dict_view_gestion_tournois = {}
        try:
            print(f"1. Créer un nouveau tournoi")
            print(f"2. modifier un tournoi")
            print(f"3. supprimer un tournoi")
            print(f"4. afficher un tournoi")
            print(f"5. afficher tous les tournois")
            print(f"6. lancez un tournoi")
            print(f"7. retour")
            self.view.footer(self)
            choice = ""
            while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                choice = input(f"Veuillez choisir une option : ")
            dict_view_gestion_tournois["status"] = True
            dict_view_gestion_tournois["message"] = f"{message}"
            dict_view_gestion_tournois["function"] = f"gestion_tournois() : Affiche le menu de gestion des tournois"
            dict_view_gestion_tournois["choice"] = int(choice)
        except Exception as e:
            dict_view_gestion_tournois["status"] = False
            dict_view_gestion_tournois["message"] = f"{message}"
            dict_view_gestion_tournois["function"] = print(f"gestion_tournois() : {e}")
        return dict_view_gestion_tournois

    def creer_tournoi(self):
        """ Affiche le formulaire de création d'un tournoi """
        dict_view_creer_tournoi = {}
        try:
            # NOM DU TOURNOI
            tournament_name = ""
            while tournament_name == "":
                tournament_name = input(f"Nom du tournoi : ")
            # LIEU DU TOURNOI
            tournament_location = ""
            while tournament_location == "":
                tournament_location = input(f"Lieu du tournoi : ")
            # DATE DU TOURNOI
            tournament_date = ""
            while tournament_date == "" or not re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", tournament_date):
                tournament_date = input(f"Date du tournoi(DD/MM/YYYY) : ")
            # DESCRIPTION DU TOURNOI
            tournament_description = ""
            while tournament_description == "":
                tournament_description = input(f"Description du tournoi : ")
            # TIME CONTROL
            print("Contrôle du temps : " )
            print(" 1. Bullet (1 min + 0 sec)")
            print(" 2. Blitz (3 min + 2 sec)")
            print(" 3. Coup rapide (5 min + 3 sec)")
            tournament_time_control = ""
            while tournament_time_control not in ["1", "2", "3"]:
                if tournament_time_control == "1":
                    tournament_time_control = "Bullet"
                elif tournament_time_control == "2":
                    tournament_time_control = "Blitz"
                elif tournament_time_control == "3":
                    tournament_time_control = "Coup rapide"
                tournament_time_control = input(f"Veuillez choisir une option : ")
            # NOMBRE DE TOURS
            tournament_number_round = 4
            # LISTE DES DIFFERENTS TOURS
            tournament_instance_round = []
            # LISTE DES JOUEURS
            tournament_players = []
            # DICIONNAIRE
            dict_view_creer_tournoi["tournament_name"] = tournament_name
            dict_view_creer_tournoi["tournament_location"] = tournament_location
            dict_view_creer_tournoi["tournament_date"] = tournament_date
            dict_view_creer_tournoi["tournament_description"] = tournament_description
            dict_view_creer_tournoi["tournament_time_control"] = tournament_time_control
            dict_view_creer_tournoi["tournament_number_round"] = tournament_number_round
            dict_view_creer_tournoi["tournament_instance_round"] = tournament_instance_round
            dict_view_creer_tournoi["tournament_players"] = tournament_players
            dict_view_creer_tournoi["status"] = True
            dict_view_creer_tournoi["function"] = f"creer_tournoi() : Affiche le formulaire de création d'un tournoi"
        except Exception as e:
            dict_view_creer_tournoi["status"] = False
            dict_view_creer_tournoi["function"] = print(f"creer_tournoi() : {e}")
        return dict_view_creer_tournoi

    def demande_id_tournoi(self, list_id_tournois):
        """ affiche et demande le choix du tournoi à modifier """
        dict_view_modifier_tournoi = {}
        try:
            # Demande le l'identifiant du tournois à modifie
            tournament_id = ""
            while tournament_id == "" or tournament_id not in list_id_tournois:
                tournament_id = input(f"Veuillez saisir l'identifiant du tournoi : ")
            dict_view_modifier_tournoi["tournament_id"] = tournament_id
            dict_view_modifier_tournoi["status"] = True
            dict_view_modifier_tournoi["function"] = f"demande_id() : affiche et demande le choix du tournoi à modifier"

        except Exception as e:
            dict_view_modifier_tournoi["status"] = False
            dict_view_modifier_tournoi["function"] = print(f"demande_id() : {e}")
        return dict_view_modifier_tournoi

    def modifier_tournoi(self, tournoi):
        """ Affiche le formulaire de modification d'un tournoi """
        dict_view_modifier_tournoi = {}
        try:
            # TODO : Affiche le formulaire de modification d'un tournoi
            tournament_name = tournoi["tournament_name"]
            tournament_location = tournoi["tournament_location"]
            tournament_date = tournoi["tournament_date"]
            tournament_description = tournoi["tournament_description"]
            tournament_time_control = tournoi["tournament_control_time"]
            tournament_number_round = tournoi["tournament_number_round"]
            tournament_instance_round = tournoi["tournament_instance_round"]
            tournament_players = tournoi["tournament_players"]

            print(f"Que voulez-vous modifier ?")
            print(f"1. Nom du tournoi")
            print(f"2. Lieu du tournoi")
            print(f"3. Date du tournoi")
            print(f"4. Description du tournoi")
            print(f"5. Contrôle du temps")
            print(f"6. Liste des joueurs")

            choice = ""
            while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                choice = input(f"Veuillez choisir une option : ")
            if choice == "1":
                tournament_name = ""
                while tournament_name == "":
                    tournament_name = input(f"Nom du tournoi : ")
            elif choice == "2":
                tournament_location = ""
                while tournament_location == "":
                    tournament_location = input(f"Lieu du tournoi : ")
            elif choice == "3":
                tournament_date = ""
                while tournament_date == "" or not re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", tournament_date):
                    tournament_date = input(f"Date du tournoi(DD/MM/YYYY) : ")
            elif choice == "4":
                tournament_description = ""
                while tournament_description == "":
                    tournament_description = input(f"Description du tournoi : ")
            elif choice == "5":
                print("Contrôle du temps : " )
                print(" 1. Bullet (1 min + 0 sec)")
                print(" 2. Blitz (3 min + 2 sec)")
                print(" 3. Coup rapide (5 min + 3 sec)")
                tournament_time_control = ""
                while tournament_time_control not in ["1", "2", "3"]:
                    if tournament_time_control == "1":
                        tournament_time_control = "Bullet"
                    elif tournament_time_control == "2":
                        tournament_time_control = "Blitz"
                    elif tournament_time_control == "3":
                        tournament_time_control = "Coup rapide"
                    tournament_time_control = input(f"Veuillez choisir une option : ")
            elif choice == "6":
                # TODO: Créer la fonction pour ajouter un joueur
                pass

            dict_view_modifier_tournoi["tournament"] = {
                "tournament_name": tournament_name,
                "tournament_location": tournament_location,
                "tournament_date": tournament_date,
                "tournament_description": tournament_description,
                "tournament_control_time": tournament_time_control,
                "tournament_number_round": tournament_number_round,
                "tournament_instance_round": tournament_instance_round,
                "tournament_players": tournament_players
            }
            dict_view_modifier_tournoi["status"] = True
            dict_view_modifier_tournoi["function"] = f"modifier_tournoi() : Affiche le formulaire de modification d'un tournoi"
        except Exception as e:
            dict_view_modifier_tournoi["status"] = False
            dict_view_modifier_tournoi["function"] = print(f"modifier_tournoi() : {e}")
        return dict_view_modifier_tournoi

    def menu_tournoi(self, tournoi):
        """ Affiche le menu du tournoi """
        dict_view_menu_tournoi = {}
        try:
            # TODO : Affiche le menu du tournoi
            print(f"1. Ajouter un joueurs au tournoi")
            print(f"2. Supprimer un joueurs du tournoi")
            print(f"3. Lancer le tournoi")
            print(f"4. Retour au menu principal")
            self.view.footer(self)
            choice = ""
            while choice not in ["1", "2", "3", "4"]:
                choice = input(f"Veuillez choisir une option : ")
            dict_view_menu_tournoi["choice"] = choice
            dict_view_menu_tournoi["status"] = True
            dict_view_menu_tournoi["function"] = f"menu_tournoi() : Affiche le menu du tournoi"
        except Exception as e:
            dict_view_menu_tournoi["status"] = False
            dict_view_menu_tournoi["function"] = print(f"menu_tournoi() : {e}")
        return dict_view_menu_tournoi

    def demande_score_match(self, player1, player2):
        """ Affiche le formulaire de demande du score du match """
        dict_view_demande_score_match = {}
        try:
            # TODO : Affiche le formulaire de demande du score du match
            player1_name = player1["player_first_name"] + " " + player1["player_last_name"]
            player2_name = player2["player_first_name"] + " " + player2["player_last_name"]
            print(f"Score du match : {player1_name} vs {player2_name}")
            score_player1 = ""
            # QUI A GAGNÉ ? OU MATCH NUL ?
            print(f"1. {player1_name}")
            print(f"2. {player2_name}")
            print(f"3. Match nul")
            self.view.footer(self)
            while score_player1 not in ["1", "2", "3"]:
                score_player1 = input(f"Veuillez choisir la personne qui a gagné ou match nul si égalité : ")
            if score_player1 == "1":
                score_player1 = 1
                score_player2 = 0
            elif score_player1 == "2":
                score_player1 = 0
                score_player2 = 1
            elif score_player1 == "3":
                score_player1 = 0.5
                score_player2 = 0.5
        
            dict_view_demande_score_match["score_player1"] = score_player1
            dict_view_demande_score_match["score_player2"] = score_player2
            dict_view_demande_score_match["score"] = {
                "player1": player1,
                "player2": player2,
                "score_player1": score_player1,
                "score_player2": score_player2
            }
            dict_view_demande_score_match["status"] = True
            dict_view_demande_score_match["function"] = f"demande_score_match() : Affiche le formulaire de demande du score du match"
        except Exception as e:
            dict_view_demande_score_match["status"] = False
            dict_view_demande_score_match["function"] = print(f"demande_score_match() : {e}")
        return dict_view_demande_score_match
        
#TODO: VIEWS JOUEURS
    def gestion_joueur(self, *message):
        """ Affiche le menu de gestion des joueurs """
        dict_view_gestion_joueur = {}
        try:
            print(f"1. Créer un joueur")
            print(f"2. Modifier un joueur")
            print(f"3. Supprimer un joueur")
            print(f"4. Afficher un joueur")
            print(f"5. Afficher tous les joueurs")
            print(f"6. Retour au menu principal")
            self.view.footer(self)
            choice = ""
            while choice not in ["1", "2", "3", "4", "5", "6"]:
                choice = input(f"Veuillez choisir une option : ")
            if choice == "1":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "creer_joueur()"
            elif choice == "2":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "modifier_joueur()"
            elif choice == "3":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "supprimer_joueur()"
            elif choice == "4":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "afficher_joueur()"
            elif choice == "5":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "afficher_tous_les_joueurs()"
            elif choice == "6":
                dict_view_gestion_joueur["status"] = True
                dict_view_gestion_joueur["function"] = "menu_principal()"
            dict_view_gestion_joueur["function"] = f"gestion_joueur() : Affiche le menu de gestion des joueurs"
            dict_view_gestion_joueur["choice"] = int(choice)
        except Exception as e:
            dict_view_gestion_joueur["status"] = False
            dict_view_gestion_joueur["function"] = print(f"gestion_joueur() : {e}")
        return dict_view_gestion_joueur
    
    def creer_joueur(self):
        """ Affiche le formulaire de création d'un joueur """
        dict_view_creer_joueur = {}
        try:
            nom = input(f"Veuillez saisir le nom du joueur : ")
            while nom == "":
                nom = input(f"Veuillez saisir le nom du joueur : ")
            prenom = input(f"Veuillez saisir le prénom du joueur : ")
            while prenom == "":
                prenom = input(f"Veuillez saisir le prénom du joueur : ")
            date_de_naissance = input(f"Veuillez saisir la date de naissance du joueur (jj/mm/aaaa) : ")
            while date_de_naissance == "" or len(date_de_naissance) != 10:
                date_de_naissance = input(f"Veuillez saisir la date de naissance du joueur (jj/mm/aaaa) : ")
            sexe = input(f"Veuillez saisir le sexe du joueur (M ou F) : ")
            while sexe == "" or sexe not in ["M", "F"]:
                sexe = input(f"Veuillez saisir le sexe du joueur (M ou F)")
            dict_view_creer_joueur["status"] = True
            dict_view_creer_joueur["function"] = f"creer_joueur() : Affiche le formulaire de création d'un joueur"
            dict_view_creer_joueur["player_first_name"] = nom
            dict_view_creer_joueur["player_last_name"] = prenom
            dict_view_creer_joueur["date_of_birth"] = date_de_naissance
            dict_view_creer_joueur["sexe"] = sexe
        except Exception as e:
            dict_view_creer_joueur["status"] = False
            dict_view_creer_joueur["function"] = print(f"creer_joueur() : {e}")
        return dict_view_creer_joueur

    def demande_id_joueur(self, list_id_joueur):
        """ Demande à l'utilisateur de saisir l'id d'un joueur """
        dict_view_demande_id_joueur = {}
        try:
            id_joueur = ""
            while id_joueur not in list_id_joueur:
                id_joueur = input(f"Veuillez saisir l'id du joueur : ")
            dict_view_demande_id_joueur["status"] = True
            dict_view_demande_id_joueur["function"] = f"demande_id_joueur() : Demande l'id du joueur"
            dict_view_demande_id_joueur["joueur_id"] = id_joueur
        except Exception as e:
            dict_view_demande_id_joueur["status"] = False
            dict_view_demande_id_joueur["function"] = print(f"demande_id_joueur() : {e}")
        return dict_view_demande_id_joueur

    def modifier_joueur(self, player):
        """ Affiche le formulaire de modification d'un joueur """
        dict_view_modifier_joueur = {}
        try:
            player_name = player["player_first_name"]
            player_last_name = player["player_last_name"]
            player_date_of_birth = player["date_of_birth"]
            player_sexe = player["sexe"]
            ranking = player["ranking"]

            choice = ""
            while choice not in ["1", "2", "3", "4", "5", "6"]:
                print(f"1. Modifier le nom du joueur : {player_name}")
                print(f"2. Modifier le prénom du joueur : {player_last_name}")
                print(f"3. Modifier la date de naissance du joueur : {player_date_of_birth}")
                print(f"4. Modifier le sexe du joueur : {player_sexe}")
                print(f"5. Modifier le classement du joueur : {ranking}")
                print(f"6. Retour au menu précédent")
                self.view.footer(self)
                choice = input(f"Veuillez choisir une option : ")

            if choice == "1":
                player_name = input(f"Veuillez saisir le nom du joueur : ")
                while player_name == "":
                    player_name = input(f"Veuillez saisir le nom du joueur : ")
            elif choice == "2":
                player_last_name = input(f"Veuillez saisir le prénom du joueur : ")
                while player_last_name == "":
                    player_last_name = input(f"Veuillez saisir le prénom du joueur : ")
            elif choice == "3":
                player_date_of_birth = input(f"Veuillez saisir la date de naissance du joueur (jj/mm/aaaa) : ")
                while player_date_of_birth == "" or not re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([0-9]{4})$", player_date_of_birth):
                    player_date_of_birth = input(f"Veuillez saisir la date de naissance du joueur (jj/mm/aaaa) : ")
            elif choice == "4":
                player_sexe = input(f"Veuillez saisir le sexe du joueur (M ou F) : ")
                while player_sexe == "" or player_sexe not in ["M", "F"]:
                    player_sexe = input(f"Veuillez saisir le sexe du joueur (M ou F)")
            dict_view_modifier_joueur["status"] = True
            dict_view_modifier_joueur["function"] = f"modifier_joueur() : Affiche le formulaire de modification d'un joueur"
            dict_view_modifier_joueur["choice"] = int(choice)
            dict_view_modifier_joueur["player"] = {
                "player_first_name": player_name,
                "player_last_name": player_last_name,
                "date_of_birth": player_date_of_birth,
                "sexe": player_sexe,
                "ranking": ranking
            }
        except Exception as e:
            dict_view_modifier_joueur["status"] = False
            dict_view_modifier_joueur["function"] = print(f"modifier_joueur() : {e}")
        return dict_view_modifier_joueur

# TODO: VIEWS RAPPORTS

    #TODO:def afficher_rapport_tournoi(self):
        # """ Affiche le rapport d'un tournoi """
        # dict_view_afficher_rapport_tournoi = {}
        # try:
        #     dict_view_afficher_rapport_tournoi["status"] = True
        #     dict_view_afficher_rapport_tournoi["function"] = f"afficher_rapport_tournoi() : Affiche le rapport d'un tournoi"
        # except Exception as e:
        #     dict_view_afficher_rapport_tournoi["status"] = False
        #     dict_view_afficher_rapport_tournoi["function"] = print(f"afficher_rapport_tournoi() : {e}")
        # return dict_view_afficher_rapport_tournoi

    #TODO:def afficher_rapport_joueur(self):
        # """ Affiche le rapport d'un joueur """
        # dict_view_afficher_rapport_joueur = {}
        # try:
        #     dict_view_afficher_rapport_joueur["status"] = True
        #     dict_view_afficher_rapport_joueur["function"] = f"afficher_rapport_joueur() : Affiche le rapport d'un joueur"
        # except Exception as e:
        #     dict_view_afficher_rapport_joueur["status"] = False
        #     dict_view_afficher_rapport_joueur["function"] = print(f"afficher_rapport_joueur() : {e}")
        # return dict_view_afficher_rapport_joueur