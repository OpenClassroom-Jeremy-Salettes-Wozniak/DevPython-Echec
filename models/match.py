class Match:
    def __init__(self, date, time, location, player1, player2, score1, score2, round):
        """ Initialize the match """
        self.date = date
        self.time = time
        self.location = location
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.round = round
    
    def get_match(self):
        """ Return the match """
        dict_get_match = {}
        try:
            dict_get_match ["date"] = self.date
            dict_get_match ["time"] = self.time
            dict_get_match["location"] = self.location
            dict_get_match["player1"] = self.player1
            dict_get_match["player2"] = self.player2
            dict_get_match["score1"] = self.score1
            dict_get_match["score2"] = self.score2
            dict_get_match["round"] = self.round
            dict_get_match["status"] = True
            dict_get_match["message"] = f"Match: {self.date, self.time, self.location, self.player1, self.player2, self.score1, self.score2, self.round}"
            dict_get_match["function"] = f"get_match() : Return the match"
        except Exception as e:
            dict_get_match["date"] = self.date
            dict_get_match["time"] = self.time
            dict_get_match["location"] = self.location
            dict_get_match["player1"] = self.player1
            dict_get_match["player2"] = self.player2
            dict_get_match["score1"] = self.score1
            dict_get_match["score2"] = self.score2
            dict_get_match["round"] = self.round
            dict_get_match["status"] = False
            dict_get_match["message"] = f"Match: {self.date, self.time, self.location, self.player1, self.player2, self.score1, self.score2, self.round}"
            dict_get_match["function"] = f"get_match() : {e}"
        return dict_get_match
