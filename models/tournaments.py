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

















































































# import os
# import tinydb
# class Tournament: 

#     def __init__(
#         self, 
#         tounament_name, 
#         tournament_location, 
#         tournament_date,
#         tournament_time_control,
#         tournament_description,
#         tournament_laps=4,
#         tournament_players=["no_player"],
#         tournament_tournees=["no_matchs"],
#     ):
#         """ 
#         tournament_name: str
#         tournament_location: str
#         tournament_date: list
#         tournament_time_control: dict
#         tournament_description: str
#         tournament_laps: int
#         tournament_tournees: list
#         tournament_players: list
#         """
#         self.tournament_name = tounament_name
#         self.tournament_location = tournament_location
#         self.tournament_date = tournament_date
#         self.tournament_time_control = tournament_time_control
#         self.tournament_description = tournament_description
#         self.tournament_laps = tournament_laps
#         self.tournament_tournees = tournament_tournees
#         self.tournament_players = tournament_players

        

#     def save_tournament(self):
#         if os.path.isdir("data") == False:
#             os.mkdir("data")
#         db = tinydb.TinyDB('data/db.json')
#         Tournaments = db.table('Tournaments')
#         Tournaments.insert({
#             "tournament_name": self.tournament_name,
#             "tournament_location": self.tournament_location,
#             "tournament_date": self.tournament_date,
#             "tournament_time_control": self.tournament_time_control,
#             "tournament_description": self.tournament_description,
#             "tournament_laps": self.tournament_laps,
#             "tournament_tournees": self.tournament_tournees,
#             "tournament_players": self.tournament_players
#         })



    