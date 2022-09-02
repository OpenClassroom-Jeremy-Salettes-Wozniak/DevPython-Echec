from json import dumps
import tinydb
players = ["Player_one", "Player_two", "Player_three", "Player_four", "Player_five", "Player_six", 
"Player_seven", "Player_eight"]

class Tournaments:

    def __init__(
        self, 
        name="",                        #views
        location="",                    #views    
        date=[],                        #views 
        laps=4,                         #views 
        tournées=[],                    #matchs
        players=[],                     #players
        time_control={                  #views
            "bullet": "00:00:20", 
            "blitz": "00:00:00", 
            "rapid": "00:00:00", 
            "classical": "00:00:00"},   
        description=""):                #views

        """
        name: str
        location: str
        date: list
        laps: int
        tournées: list
        players: list
        time_control: dict
        description: str
        """

        self.name = name
        self.location = location
        self.date = date
        self.laps = laps
        self.tournées = tournées
        self.players = players
        self.time_control = time_control
        self.description = description

    def save_tournament(self):
        db = tinydb.TinyDB('db.json')
        Tournaments = db.table('Tournaments')
        Tournaments.insert({
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "laps": self.laps,
            "tournées": self.tournées,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description
        })
        
    
    def __str__(self):
        message = "Tournament: " + self.name + "\n" 
        message += "Location: " + self.location + "\n"
        message += "Date: " + str(self.date) + "\n"
        message += "Laps: " + str(self.laps) + "\n"
        message += "Tournées: " + str(self.tournées) + "\n"
        message += "Players: " + str(self.players) + "\n"
        message += "Time control: " + str(self.time_control) + "\n"
        message += "Description: " + self.description + "\n"
        return message

    def __repr__(self):
        return f"{self.name} {self.location} {self.date} {self.laps} {self.tournées} {self.players} {self.time_control} {self.description}"

    def __eq__(self, other):
        pass



if __name__ == "__main__":
    tournois1 = Tournaments(
        name="Tournois1", 
        location="Paris", 
        date=["2022/08/12", "2022/08/13"], 
        laps=4, 
        tournées=[1,2,3], 
        players=players, 
        time_control=["bullet"], 
        description="Description")
    tournois1.save_tournament()

    tournois2 = Tournaments(
        name="Tournois2",
        location="Paris",
        date=["2022/08/12", "2022/08/13"],
        laps=4,
        tournées=[1,2,3],
        players=players,
        time_control=["bullet"],
        description="Description")
    tournois2.save_tournament()

    print(tournois1)