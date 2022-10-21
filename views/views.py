import prettytable


class View:
    
    def __init__(self):
        pass

    def titre(self, message):
        print("----------------------------------------------------------------------------------")
        print(f"{message}")
        print("----------------------------------------------------------------------------------")

    def accueil(self, message=None):
        if message != None:
            print(message)
        print("1. Créer un nouveau tournoi")
        print("2. Créer un nouveau joueur")
        print("3. Sélectionner un tournoi")
        print("4. Rapport")
        print("5. Quitter")
        print("----------------------------------------------------------------------------------")

    def creerTournoi(self):
        tournament_name = input("Nom du tournoi : ")
        while tournament_name == "":
            print(f"Le nom du tournoi est obligatoire")
            tournament_name = input("Nom du tournoi : ")
            
        tournament_location = input("Lieu du tournoi : ")
        while tournament_location == "":
            print(f"Le lieu du tournoi est obligatoire")
            tournament_location = input("Lieu du tournoi : ")

        tournament_date = input("Date du tournoi au format jj/mm/aaaa : ")
        while (tournament_date == "" or len(tournament_date) != 10 and tournament_date != "jj/mm/aaaa"):
            if tournament_date == "":
                print(f"La date du tournoi est obligatoire")
            else:
                print(f"La date du tournoi doit être au format jj/mm/aaaa")
            tournament_date = input("Date du tournoi : ")
            
        print("Contrôle du temps : " )
        print(" 1. Bullet (1 min + 0 sec)")
        print(" 2. Blitz (3 min + 2 sec)")
        print(" 3. Coup rapide (5 min + 3 sec)")
        tournament_time_control = input("Veuillez selectionner le numéro de votre choix : ")
        while tournament_time_control == "":
            print(f"Le contrôle du temps est obligatoire")
            tournament_time_control = input("Contrôle du temps : ")
        while tournament_time_control != "1" and tournament_time_control != "2" and tournament_time_control != "3":
            tournament_time_control = input("Veuillez saisir un choix valide : ")
        if tournament_time_control == "1":
            tournament_time_control = "Bullet"
        elif tournament_time_control == "2":
            tournament_time_control = "Blitz"
        elif tournament_time_control == "3":
            tournament_time_control = "Coup rapide"

        tournament_description = input("Description du tournoi : ")
        while tournament_description == "":
            print(f"La description du tournoi est obligatoire")
            tournament_description = input("Description du tournoi : ")

        tournament = {
            "tournament_name": tournament_name,
            "tournament_location": tournament_location,
            "tournament_date": tournament_date,
            "tournament_time_control": tournament_time_control,
            "tournament_description": tournament_description
        }
        return tournament

    def creerJoueur(self):
        player_last_name = input("Nom du joueur : ")
        while player_last_name == "":
            print(f"Le nom du joueur est obligatoire")
            player_last_name = input("Nom du joueur : ")
            
        player_first_name = input("Prénom du joueur : ")
        while player_first_name == "":
            print(f"Le prénom du joueur est obligatoire")
            player_first_name = input("Prénom du joueur : ")

        player_birth_date = input("Date de naissance du joueur au format jj/mm/aaaa : ")
        while (player_birth_date == "" or len(player_birth_date) != 10 and player_birth_date != "jj/mm/aaaa"):
            if player_birth_date == "":
                print(f"La date de naissance du joueur est obligatoire")
            else:
                print(f"La date de naissance du joueur doit être au format jj/mm/aaaa")
            player_birth_date = input("Date de naissance du joueur : ")

        player_sexe = input("Sexe du joueur M ou F : ")
        while player_sexe == "" or not player_sexe == "M" and not player_sexe == "F":
            if player_sexe == "":
                print(f"Le sexe du joueur est obligatoire")
            else:
                print(f"Le sexe du joueur doit être M ou F")
            player_sexe = input("Sexe du joueur : ")
        
        player = {
            "player_last_name": player_last_name,
            "player_first_name": player_first_name,
            "player_birth_date": player_birth_date,
            "player_sexe": player_sexe
        }
        return player

    def selectionnerTournoi(self, tournaments):
        print("----------------------------------------------------------------------------------")
        print("Liste des tournois")
        print("----------------------------------------------------------------------------------")
        table = prettytable.PrettyTable()
        table.field_names = [
            "Identifiant",
            "tournament_name",
            "tournament_location",
            "tournament_date",
            "tournament_time_control",
            "tournament_description",
            "tournament_laps",
            "tournament_tournees",
            "tournament_players",
        ]
        for tournament in tournaments:
            tournament_id = tournament.doc_id
            table.add_row(
                [
                    tournament_id,
                    tournament["tournament_name"],
                    tournament["tournament_location"],
                    tournament["tournament_date"],
                    tournament["tournament_time_control"],
                    tournament["tournament_description"],
                    tournament["tournament_laps"],
                    tournament["tournament_tournees"],
                    tournament["tournament_players"],
                ]
            )    
        print(table)
        list_id = []
        for tournament in tournaments:
            list_id.append(str(tournament.doc_id))
        tournament_id = input("Veuillez selectionner l'identifiant du tournoi : ")
        while tournament_id == "" or not tournament_id in list_id:
            tournament_id = input("Veuillez selectionner un identifiant valide : ")
        return int(tournament_id)

        
    def afficherTournoi(self, tournament):
        print("----------------------------------------------------------------------------------")
        print("Détail du tournoi")
        print("----------------------------------------------------------------------------------")
        table = prettytable.PrettyTable()
        table.field_names = [
            "tournament_name",
            "tournament_location",
            "tournament_date",
            "tournament_time_control",
            "tournament_description",
            "tournament_laps",
            "tournament_tournees",
            "tournament_players",
        ]
        table.add_row(
            [
                tournament["tournament_name"],
                tournament["tournament_location"],
                tournament["tournament_date"],
                tournament["tournament_time_control"],
                tournament["tournament_description"],
                tournament["tournament_laps"],
                tournament["tournament_tournees"],
                tournament["tournament_players"],
            ]
        )
        print(table)


    def afficherJoueurs(self, players):
        print("----------------------------------------------------------------------------------")
        print("Liste des joueurs")
        print("----------------------------------------------------------------------------------")
        table = prettytable.PrettyTable()
        table.field_names = [
            "Identifiant",
            "player_last_name",
            "player_first_name",
            "player_birth_date",
            "player_sexe",
        ]
        for player in players:
            player_id = player.doc_id
            table.add_row(
                [
                    player_id,
                    player["player_last_name"],
                    player["player_first_name"],
                    player["player_birth_date"],
                    player["player_sexe"],
                ]
            )
        print(table)
        player_id = input("Veuillez selectionner l'identifiant du joueur : ")
        while player_id == "":
            player_id = input("Veuillez selectionner un identifiant valide : ")
        return int(player_id)

    def lancerTournoi(self, id_tournament):
        print("----------------------------------------------------------------------------------")
        print("Lancement du tournoi")
        print("----------------------------------------------------------------------------------")
        print(f"Le tournoi {id_tournament['tournament_name']} a été lancé")
        # RESULTAT DU TOURNOI DU ROUND 1
        round_one = self.round(1)
        # RESULTAT DU TOURNOI DU ROUND 2
        round_two = self.round(2)
        # RESULTAT DU TOURNOI DU ROUND 3
        round_tree = self.round(3)
        # RESULTAT DU TOURNOI DU ROUND 4
        round_four = self.round(4)

        return round_one, round_two, round_tree, round_four

    
    def round(self, round, matchs):
        print("----------------------------------------------------------------------------------")
        print("Lancement du round")
        print("----------------------------------------------------------------------------------")
        print(f"Le round {round} a été lancé")
        # RESULTAT DU ROUND 1
        # RESULTAT DU ROUND 2
        # RESULTAT DU ROUND 3
        # RESULTAT DU ROUND 4

    def match(self, round, player1, player2):
        print("----------------------------------------------------------------------------------")
        print("Lancement du match")
        print("----------------------------------------------------------------------------------")
        print(f"Le match du round {round} a été lancé")
        player1_score = input(f"Score du joueur {player1['player_last_name']} : ")
        player2_score = input(f"Score du joueur {player2['player_last_name']} : ")
        return player1_score, player2_score