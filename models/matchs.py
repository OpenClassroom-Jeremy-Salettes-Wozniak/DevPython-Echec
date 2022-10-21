from models.players import Player
import tinydb
import os

class Match:

    def __init__(self, id, date, player1, player2, score1, score2, round):
        self.id = id
        self.date = date
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.round = round

    def match_save(self):
        """
        Enregistre un match
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        db = tinydb.TinyDB("data/db.json")
        table = db.table("matches")
        table.insert(
            {
                "id": self.id,
                "date": self.date,
                "player1": self.player1,
                "player2": self.player2,
                "score1": self.score1,
                "score2": self.score2,
                "round": self.round,
            }
        )

    def matches_load(self):
        """
        Charge les matchs
        """
        db = tinydb.TinyDB("data/db.json")
        table = db.table("matches")
        return table.all()
        