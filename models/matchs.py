class Matchs:

    def __init__(self, player1, player2, player1_score, player2_score, player_again=[]):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.player_again = player_again
        
    def __str__(self):
        message = "Player 1: " + self.player1 + "\n"
        message += "Player 2: " + self.player2 + "\n"
        message += "Player 1 score: " + str(self.player1_score) + "\n"
        message += "Player 2 score: " + str(self.player2_score) + "\n"
        return message

    def __repr__(self):
        return f"{self.player1} {self.player2} {self.player1_score} {self.player2_score}"
        