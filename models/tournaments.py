import tinydb
import os


class Tournament:

    def __init__(
        self,
        tounament_name, 
        tournament_location, 
        tournament_date,
        tournament_time_control,
        tournament_description,
        tournament_laps=4,
        tournament_players=["no_player"],
        tournament_tournees=["no_matchs"],
    ):
        """ 
        tournament_name: str
        tournament_location: str
        tournament_date: list
        tournament_time_control: dict
        tournament_description: str
        tournament_laps: int
        tournament_tournees: list
        tournament_players: list
        """
        self.tournament_name = tounament_name
        self.tournament_location = tournament_location
        self.tournament_date = tournament_date
        self.tournament_time_control = tournament_time_control
        self.tournament_description = tournament_description
        self.tournament_laps = tournament_laps
        self.tournament_tournees = tournament_tournees
        self.tournament_players = tournament_players

    def tournament_save(self):
        """ 
        Save tournament in database
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        db = tinydb.TinyDB("data/db.json")
        table = db.table("tournaments")
        table.insert(
            {
                "tournament_name": self.tournament_name,
                "tournament_location": self.tournament_location,
                "tournament_date": self.tournament_date,
                "tournament_time_control": self.tournament_time_control,
                "tournament_description": self.tournament_description,
                "tournament_laps": self.tournament_laps,
                "tournament_tournees": self.tournament_tournees,
                "tournament_players": self.tournament_players,
            }
        )

    def tournaments_load(self):
        """ 
        Load tournament from database
        """
        db = tinydb.TinyDB("data/db.json")
        table = db.table("tournaments")
        return table.all()

    def tournament_load(self, id):
        """ 
        Load tournament from database
        """
        db = tinydb.TinyDB("data/db.json")
        table = db.table("tournaments")
        return table.get(doc_id=id)
        
    def tournament_players_add(self, id_player, id_tournament):
        """ 
        Ajouter joueur id_player qui à l'id id_tournament
        """
        # si id_player existe deja dans la liste des joueurs du tournoi tournament_players
        # alors on ne fait rien
        # sinon on ajoute le joueur
        db = tinydb.TinyDB("data/db.json")
        tournoi = self.tournament.tournament_load(self, id_tournament)
        if id_player not in tournoi["tournament_players"]:
            tournoi["tournament_players"].append(id_player)
            table = db.table("tournaments")
            table.update(tournoi, doc_ids=[id_tournament])
            # Supprimer no_player si il est dans la liste des joueurs
            if "no_player" in tournoi["tournament_players"]:
                tournoi["tournament_players"].remove("no_player")
                table = db.table("tournaments")
                table.update(tournoi, doc_ids=[id_tournament])
            return True
        else:
            print("Le joueur est déjà dans la liste des joueurs du tournoi")
            return False
