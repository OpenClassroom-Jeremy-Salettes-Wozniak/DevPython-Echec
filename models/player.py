class Player:
    """ Player class """
    def __init__(self, player_first_name, player_last_name, date_of_birth, sexe, ranking=0):
        """ Initialize the player """
        self.player_first_name = player_first_name
        self.player_last_name = player_last_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.ranking = ranking

    def get_player(self):
        """ Return the player """
        dict_get_player = {}
        try:
            dict_get_player["player_first_name"] = self.player_first_name
            dict_get_player["player_last_name"] = self.player_last_name
            dict_get_player["date_of_birth"] = self.date_of_birth
            dict_get_player["sexe"] = self.sexe
            dict_get_player["ranking"] = self.ranking
            dict_get_player["status"] = True
            dict_get_player["message"] = f"Player: {self.player_first_name, self.player_last_name, self.date_of_birth, self.sexe, self.ranking}"
            dict_get_player["function"] = f"get_player() : Return the player"
        except Exception as e:
            dict_get_player["player_first_name"] = self.player_first_name
            dict_get_player["player_last_name"] = self.player_last_name
            dict_get_player["date_of_birth"] = self.date_of_birth
            dict_get_player["sexe"] = self.sexe
            dict_get_player["ranking"] = self.ranking
            dict_get_player["status"] = False
            dict_get_player["message"] = f"Player: {self.player_first_name, self.player_last_name, self.date_of_birth, self.sexe, self.ranking}"
            dict_get_player["function"] = f"get_player() : {e}"
        return dict_get_player

    def save_player(self, tinydb, os):
        """ Save the player in the database """
        dict_save_player = {}
        try:
            if not os.path.exists("data"):
                os.makedirs("data")
            elif not os.path.exists("data/db.json"):
                open("data/db.json", "w").close()
            else:
                db = tinydb.TinyDB("data/db.json")
                table = db.table("players")
                table.insert({
                    "player_first_name": self.player_first_name, 
                    "player_last_name": self.player_last_name, 
                    "date_of_birth": self.date_of_birth, 
                    "sexe": self.sexe, 
                    "ranking": self.ranking
                    })
                db.close()
                dict_save_player["status"] = True
                dict_save_player["message"] = f"Player: {self.player_first_name, self.player_last_name, self.date_of_birth, self.sexe, self.ranking}"
                dict_save_player["function"] = f"save_player() : Save the player in the database"
        except Exception as e:
            dict_save_player["status"] = False
            dict_save_player["message"] = f"Player: {self.player_first_name, self.player_last_name, self.date_of_birth, self.sexe, self.ranking} not saved"
            dict_save_player["function"] = f"save_player() : {e}"
        return dict_save_player

    def get_table_players(self, tinydb):
        """ Return all players """
        dict_get_all_players = {}
        try:
            # Créer une instance de TinyDB
            db = tinydb.TinyDB("data/db.json")
            # Créer une instance de la table Tournament
            table = db.table("players")
            # Récupérer tous les tournois
            all_players = table.all()
            dict_get_all_players["status"] = True
            dict_get_all_players["function"] = f"get_all_tournaments() : Return all tournament"
            dict_get_all_players["players"] = all_players
        except Exception as e:
            dict_get_all_players["status"] = False
            dict_get_all_players["players"] = all_players
            dict_get_all_players["function"] = print(f"get_all_tournament() : {e}")
        return dict_get_all_players

    def get_table_player(self, tinydb, id_player):
        """ Return all players """
        dict_get_all_players = {}
        try:
            # Créer une instance de TinyDB
            db = tinydb.TinyDB("data/db.json")
            # Créer une instance de la table Tournament
            table = db.table("players")
            # Récupérer tous les tournois
            table_player = table.get(doc_id=id_player)  
            dict_get_all_players["status"] = True
            dict_get_all_players["function"] = f"get_all_tournaments() : Return all tournament"
            dict_get_all_players["players"] = table_player
        except Exception as e:
            dict_get_all_players["status"] = False
            dict_get_all_players["players"] = table_player
            dict_get_all_players["function"] = print(f"get_all_tournament() : {e}")
        return dict_get_all_players