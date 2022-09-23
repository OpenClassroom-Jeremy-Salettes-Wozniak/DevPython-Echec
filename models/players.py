import os
import tinydb

class Player:
    """Player d'echec suisse"""
    def __init__(
        self, 
        player_last_name, 
        player_first_name,
        player_birth_date, 
        player_sexe, 
        player_ranking=int, 
        player_again=[],
        ):
        self.player_last_name = player_last_name
        self.player_first_name = player_first_name
        self.player_birth_date = player_birth_date
        self.player_sexe = player_sexe
        self.player_ranking = player_ranking
        self.player_again = player_again

    def player_save(self):
        """
        Enregistre un joueur
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        db = tinydb.TinyDB("data/db.json")
        table = db.table("players")
        table.insert(
            {
                "player_last_name": self.player_last_name,
                "player_first_name": self.player_first_name,
                "player_birth_date": self.player_birth_date,
                "player_sexe": self.player_sexe,
                "player_ranking": str(self.player_ranking),
                "player_again": self.player_again,
            }
        )
