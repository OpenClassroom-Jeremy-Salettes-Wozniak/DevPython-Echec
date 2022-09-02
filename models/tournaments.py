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