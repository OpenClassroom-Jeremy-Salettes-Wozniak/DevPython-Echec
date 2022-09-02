class Rapports:
    
    def __init__(self, actor=[], player=[], tournament=[], match=[]):
        self.actor = actor
        self.player = player
        self.tournament = tournament
        self.match = match
        self.rapport_id = 1

    def increment_rapport_id(self):
        self.rapport_id += 1
        return self.rapport_id

    def __str__(self):
        message = "Actor: " + self.actor 
        message += "Player: " + self.player + "\n"
        message += "Tournament: " + self.tournament + "\n"
        message += "Match: " + self.match + "\n"

        return message

    def __repr__(self):
        return f"{self.actor} {self.player} {self.tournament} {self.match}"
    
if __name__ == "__main__":
    print("Rapports")