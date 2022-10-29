class Tournament:
    """ Class Tournament """
    def __init__(
        self, 
        tournament_name, 
        tournament_location, 
        tournament_date, 
        tournament_number_round,
        tournament_instance_round,
        tournament_players,
        tournament_control_time,
        tournament_description):
        """ Initialize the tournament """
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_date = tournament_date
        self.tournament_number_round = tournament_number_round
        self.tournament_instance_round = tournament_instance_round
        self.tournament_players = tournament_players
        self.tournament_control_time = tournament_control_time
        self.tournament_description = tournament_description

    def get_tournament(self):
        """ Return the tournament """
        dict_get_tournament = {}
        try:
            dict_get_tournament["tournament_name"] = self.tournament_name
            dict_get_tournament["tournament_location"] = self.tournament_location
            dict_get_tournament["tournament_date"] = self.tournament_date
            dict_get_tournament["tournament_number_round"] = self.tournament_number_round
            dict_get_tournament["tournament_instance_round"] = self.tournament_instance_round
            dict_get_tournament["tournament_players"] = self.tournament_players
            dict_get_tournament["tournament_control_time"] = self.tournament_control_time
            dict_get_tournament["tournament_description"] = self.tournament_description
            dict_get_tournament["status"] = True
            dict_get_tournament["message"] = f"Tournament: {self.tournament_name, self.tournament_location, self.tournament_date, self.tournament_number_round, self.tournament_instance_round, self.tournament_player, self.tournament_control_time, self.tournament_description}"
            dict_get_tournament["function"] = f"get_tournament() : Return the tournament"
        except Exception as e:
            dict_get_tournament["tournament_name"] = self.tournament_name
            dict_get_tournament["tournament_location"] = self.tournament_location
            dict_get_tournament["tournament_date"] = self.tournament_date
            dict_get_tournament["tournament_number_round"] = self.tournament_number_round
            dict_get_tournament["tournament_instance_round"] = self.tournament_instance_round
            dict_get_tournament["tournament_players"] = self.tournament_players
            dict_get_tournament["tournament_control_time"] = self.tournament_control_time
            dict_get_tournament["tournament_description"] = self.tournament_description
            dict_get_tournament["status"] = False
            dict_get_tournament["message"] = f"Tournament: {self.tournament_name, self.tournament_location, self.tournament_date, self.tournament_number_round, self.tournament_instance_round, self.tournament_players, self.tournament_control_time, self.tournament_description}"
            dict_get_tournament["function"] = f"get_tournament() : {e}"
        return dict_get_tournament

    def save_tournament(self, tinydb, os):
        """ Save the tournament in json with tinydb """
        dict_save = {}
        try:
            # Si dans data il y a pas un fichier db.json
            if not os.path.exists("data"):
                os.mkdir("data")
            # Si dans data il y a pas un fichier db.json
            elif not os.path.exists("data/db.json"):
                # Créer un fichier db.json
                open("data/db.json", "w").close()
            else:
                # Créer une instance de TinyDB
                db = tinydb.TinyDB("data/db.json")
                # Créer une instance de la table Tournament
                table_tournament = db.table("Tournament")
                # Ajouter le tournoi dans la table Tournament
                table_tournament.insert({
                    "tournament_name": self.tournament_name,
                    "tournament_location": self.tournament_location,
                    "tournament_date": self.tournament_date,
                    "tournament_number_round": self.tournament_number_round,
                    "tournament_instance_round": self.tournament_instance_round,
                    "tournament_players": self.tournament_players,
                    "tournament_control_time": self.tournament_control_time,
                    "tournament_description": self.tournament_description
                })
                dict_save["status"] = True
                dict_save["message"] = f"Save the tournament in json with tinydb"
                dict_save["function"] = f"save() : Save the tournament in json with tinydb"
        except Exception as e:
            dict_save["status"] = False
            dict_save["message"] = f"Save the tournament in json with tinydb"
            dict_save["function"] = f"save() : {e}"
        return dict_save

    def get_table_tournaments(self, tinydb):
        """ Return all tournament """
        dict_get_all_tournament = {}
        try:
            # Créer une instance de TinyDB
            db = tinydb.TinyDB("data/db.json")
            # Créer une instance de la table Tournament
            table = db.table("Tournament")
            # Récupérer tous les tournois
            all_tournaments = table.all()
            if all_tournaments == []:
                dict_get_all_tournament["status"] = False
                dict_get_all_tournament["message"] = "No tournament"
                dict_get_all_tournament["function"] = "get_table_tournaments() : Return all tournament"
            dict_get_all_tournament["status"] = True
            dict_get_all_tournament["function"] = f"get_all_tournaments() : Return all tournament"
            dict_get_all_tournament["tournaments"] = all_tournaments
        except Exception as e:
            dict_get_all_tournament["status"] = False
            dict_get_all_tournament["tournaments"] = all_tournaments
            dict_get_all_tournament["function"] = print(f"get_all_tournament() : {e}")
        return dict_get_all_tournament

    def get_table_tournament(self, tinydb, tournament_id):
        """ Return a tournament """
        dict_get_tournament = {}
        try:
            # Créer une instance de TinyDB
            db = tinydb.TinyDB("data/db.json")
            # Créer une instance de la table Tournament
            table = db.table("Tournament")
            # Récupérer le tournoi
            tournament = table.get(doc_id=tournament_id)
            dict_get_tournament["status"] = True
            dict_get_tournament["function"] = f"get_tournament() : Return a tournament"
            dict_get_tournament["tournament"] = tournament
        except Exception as e:
            dict_get_tournament["status"] = False
            dict_get_tournament["tournament"] = tournament
            dict_get_tournament["function"] = print(f"get_tournament() : {e}")
        return dict_get_tournament

    def delete_tournament(self, tinydb, id):
        """ Delete the tournament """
        dict_delete_tournament = {}
        try:
            # Créer une instance de TinyDB
            db = tinydb.TinyDB("data/db.json")
            # Créer une instance de la table Tournament
            table = db.table("Tournament")
            # selectionner le tournoi
            table.remove(doc_ids=[int(id)])
            dict_delete_tournament["status"] = True
            dict_delete_tournament["function"] = f"delete_tournament() : Delete the tournament"
        except Exception as e:
            dict_delete_tournament["status"] = False
            dict_delete_tournament["function"] = print(f"delete_tournament() : {e}")
        return dict_delete_tournament

    def modify_tournament(self, tournament, tinydb, id):
        """ Modify the tournament """
        dict_modify_tournament = {}
        try:
            db = tinydb.TinyDB("data/db.json")
            table = db.table("Tournament")
            table.update(tournament, doc_ids=[int(id)])
            dict_modify_tournament["status"] = True
            dict_modify_tournament["function"] = f"modify_tournament() : Modify the tournament"
        except Exception as e:
            dict_modify_tournament["status"] = False
            dict_modify_tournament["function"] = print(f"modify_tournament() : {e}")
        return dict_modify_tournament
        
    def add_player_tournament(self, tinydb, id, tournament):
        """ Add a player in the tournament """
        dict_add_player_tournament = {}
        try:
            db = tinydb.TinyDB("data/db.json")
            table = db.table("Tournament")
            # Ajouter le joueur dans le tournoi
            table.update(tournament, doc_ids=[int(id)])
            dict_add_player_tournament["status"] = True
            dict_add_player_tournament["function"] = f"add_player_tournament() : Add a player in the tournament"
        except Exception as e:
            dict_add_player_tournament["status"] = False
            dict_add_player_tournament["function"] = print(f"add_player_tournament() : {e}")
        return dict_add_player_tournament