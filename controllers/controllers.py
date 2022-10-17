from ast import If
from operator import le
import os
from turtle import pen


from models.tournaments import Tournament

class Controller:

    def __init__(self, view, tournament, player):
        self.view = view
        self.tournament = tournament
        self.player = player
        self.accueil()

    def accueil(self, message=None):
        titre = "Bienvenue dans le gestionnaire de tournoi d'échec"
        os.system("cls")
        if message != None:
            self.view.titre(self, titre)
            self.view.accueil(self, message)
        else:
            self.view.titre(self, titre)
            self.view.accueil(self)

        choix = input(f"Veuillez selectionner le numéro de votre choix : ")

        if choix == "1":
            self.creerTournoi()
        elif choix == "2":
            self.creerJoueur()	
        elif choix == "3":
            self.selectionnerTournoi()
        elif choix == "4":
            self.rapport()
        elif choix == "5":
            exit()
        else:
            os.system("cls")
            self.accueil("---- Veuillez selectionner un choix valide ----")

    def creerTournoi(self):
        try: 
            os.system("cls")
            self.view.titre(self, "Créer un tournoi")
            tournoi = self.view.creerTournoi(self)
            new_tournois = self.tournament(
                tournoi["tournament_name"], 
                tournoi["tournament_location"], 
                tournoi["tournament_date"], 
                tournoi["tournament_time_control"], 
                tournoi["tournament_description"],
                )
            new_tournois.tournament_save()
            self.accueil("---- Le tournoi a été créé avec succès ----")

        except:
            os.system("cls")
            self.creerTournoi()

    def creerJoueur(self):
        try:
            self.view.titre(self, "Créer un joueur")
            joueur = self.view.creerJoueur(self)
            print(joueur)
            new_joueur = self.player(
                joueur["player_last_name"], 
                joueur["player_first_name"],
                joueur["player_birth_date"],
                joueur["player_sexe"],
            )
            new_joueur.player_save()
            self.accueil("---- Le joueur a été créé avec succès ----")
        except Exception as e:
            print(e)

    def selectionnerTournoi(self):
        os.system("cls")
        self.view.titre(self, "Selectionner un tournoi")
        tournois = self.tournament.tournaments_load(self)
        id = self.view.selectionnerTournoi(self, tournois)
        self.affichageTournoi(id)

    def affichageTournoi(self, id, message=None):
        os.system("cls")
        self.view.titre(self, "Affichage du tournoi")
        id_tournoi = self.tournament.tournament_load(self, id)
        self.view.afficherTournoi(self, id_tournoi)
        if message != None:
            print(message)
        print("1 - Ajouter un joueur")
        print("2 - Lancer le tournoi")
        print("3 - Retour")
        choix = input(f"Veuillez selectionner le numéro de votre choix : ")
        if choix == "1":
            add_player = self.ajouterJoueur(id_tournoi)
            if add_player == True:
                message = "---- Le joueur a été ajouté avec succès ----"
                self.affichageTournoi(id, message)
            elif add_player == False:
                message = "---- Le joueur est déjà dans le tournoi ----"
                self.affichageTournoi(id, message)
            else:
                print("---- Erreur ----")
        elif choix == "2":
            self.lancerTournoi(id_tournoi)
        elif choix == "3":
            self.accueil()

    def ajouterJoueur(self, id_tournoi):
        os.system("cls")
        self.view.titre(self, "Ajouter un joueur")
        joueurs = self.player.players_load(self)
        id_player = self.view.afficherJoueurs(self, joueurs)
        add_player = self.tournament.tournament_players_add(self, id_player, id_tournoi.doc_id)
        if add_player == True:
            return True
        else:
            return False

    def lancerTournoi(self, id_tournoi):
        """ Lance le tournoi """
        os.system("cls")
        dict_lancerTournoi = {}
        try:    
            nb_joueurs = len(id_tournoi["tournament_players"])
            list_joueurs = id_tournoi["tournament_players"]
            while nb_joueurs != 8:
                os.system("cls")
                self.view.titre(self, "Lancer le tournoi")
                print("---- Il faut 8 joueurs pour lancer le tournoi ----")
                print("1 - Ajouter un joueur")
                print("2 - Retour")
                choix = input(f"Veuillez selectionner le numéro de votre choix : ")
                if choix == "1":
                    add_player = self.ajouterJoueur(id_tournoi)
                    if add_player == True:
                        message = "---- Le joueur a été ajouté avec succès ----"
                        self.affichageTournoi(id_tournoi.doc_id, message)
                    elif add_player == False:
                        message = "---- Le joueur est déjà dans le tournoi ----"
                        self.affichageTournoi(id_tournoi.doc_id, message)
                    else:
                        print("---- Erreur ----")
                elif choix == "2":
                    print("---- Retour ----")
            print("---- Le tournoi peut commencer ----")
            result_one = self.round(1, list_joueurs)
            if result_one == True:
                result_two = self.round(2, list_joueurs)
                if result_two == True:
                    result_tree = self.round(3, list_joueurs)
                    if result_tree == True:
                        result_four= self.round(4, list_joueurs)
                    else:
                        print("---- Erreur ----")
                else:
                    print("---- Erreur ----")
            else:
                print("---- Erreur ----")
        except Exception as e:
            print(e)
            dict_lancerTournoi["error"] = f"---- Erreur lors de la récupération des joueurs du tournoi ----" + str(e)
        return dict_lancerTournoi

    def round(self, round, list_joueurs):
        """ Lance un round """
        os.system("cls")
        self.view.titre(self, "Lancer un round")
        print(f"---- Round {round} ----")
        if round == 1:
            # On divisie la liste des joueurs en 2
            list_joueurs_1 = list_joueurs[0:4]
            list_joueurs_2 = list_joueurs[4:8]
            list_matchs = {}
            # Le joueur 1 du groupe 1 joue contre le joueur 1 du groupe 2
            match_1 = self.match(list_joueurs_1[0], list_joueurs_2[0])
            list_matchs["match_1"] = match_1
            # Le joueur 2 du groupe 1 joue contre le joueur 2 du groupe 2
            match_2 = self.match(list_joueurs_1[1], list_joueurs_2[1])
            list_matchs["match_2"] = match_2
            # Le joueur 3 du groupe 1 joue contre le joueur 3 du groupe 2
            match_3 = self.match(list_joueurs_1[2], list_joueurs_2[2])
            list_matchs["match_3"] = match_3
            # Le joueur 4 du groupe 1 joue contre le joueur 4 du groupe 2
            match_4 = self.match(list_joueurs_1[3], list_joueurs_2[3])
            list_matchs["match_4"] = match_4
            
        elif round == 2:
            # liste_TRIER = []
            # list_TRIER.sort(reverse=True)
            # match_1 = self.match(list_joueurs[0], list_joueurs[1])
            pass

    def match(self, player_1, player_2):
        """ Lance un match """
        dict_match = {}
        os.system("cls")
        player_one = self.player.player_load(self, player_1)
        player_two = self.player.player_load(self, player_2)
        print(player_1)
        print(player_2)
        
        self.view.titre(self, "Lancer un match")
        print(f"---- Match entre {player_one} et {player_two} ----")
        print("1 - Victoire du joueur 1")
        print("2 - Victoire du joueur 2")
        print("3 - Match nul")
            
        choix = input(f"Veuillez selectionner le numéro de votre choix : ")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input(f"Veuillez selectionner le numéro de votre choix : ")

        if choix == "1":
            print("---- Player 1 gagne ----")
            self.player.player_modify_score(self, player_1, 1)
            self.player.player_modify_score(self, player_2, 0)
        elif choix == "2":
            print("---- Player 2 gagne ----")
            self.player.player_modify_score(self, player_1, 0)
            self.player.player_modify_score(self, player_2, 1)
        elif choix == "3":
            print("---- Match nul ----")
            self.player.player_modify_score(self, player_1, 0.5)
            self.player.player_modify_score(self, player_2, 0.5)
        else:
            print("---- Erreur ----")
        # ROUND 1
        # VERIFIER LE NOMBRE DE JOUEURS ON DIVISE LE NOMBRE DE JOUEURS PAR 2 LIST A ET LIST B ON PREMIER ELEMENT DE LA LIST A ON ATAQUE LE PREMIER ELEMENT DE LA LIST B
        # ON AFFICHE LA VUE DES RESULTATS DU PREMIER ROUND 

        # ROUND 2
        # CLASSEMENT PAR NOMBRE DE POINT TRIE PAR SCORE LE PREMIER JOUEUR 1 AFFRONTE LE JOUEUR 2 ET LES JOUEURS NE DOIVENT PAS SE REAFFRONTER
        # BOUCLE D'AFFRONTATION DES JOUEURS 

        # SAUVGARDE DES RESULTATS DU TOURNOI A CHAQUE ROUNDS