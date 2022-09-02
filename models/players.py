class Players:

    def __init__(self, last_name="", first_name="", date_of_birth="", sexe="", classement=int, player_again=[]):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classement = classement
        self.player_again = player_again
        self.player_id = 1
    
    def increment_player_id(self):
        self.player_id += 1
        return self.player_id
    
    def __str__(self):
        message = "Player: " + self.last_name + " " + self.first_name + "\n"
        message += "Date of birth: " + str(self.date_of_birth) + "\n"
        message += "Sexe: " + self.sexe + "\n"
        message += "Classement: " + str(self.classement) + "\n"
        return message

    def __repr__(self):
        return f"{self.last_name} {self.first_name} {self.date_of_birth} {self.sexe} {self.classement}"

    def __eq__(self, other):
        pass

if __name__ == "__main__":
    player1 = Players(last_name="Dupont", first_name="Jean", date_of_birth="2022/08/12", sexe="M", classement=1, player_again=[])
    print(player1)