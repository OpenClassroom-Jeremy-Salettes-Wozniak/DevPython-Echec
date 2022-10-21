class Round:
    """ Round class """
    def __init__(self, number, matches):
        """ Initialize the round """
        self.number = number
        self.matches = matches

    def get_round(self):
        """ Return the round """
        dict_get_round = {}
        try:
            dict_get_round["number"] = self.number
            dict_get_round["matches"] = self.matches
            dict_get_round["status"] = True
            dict_get_round["message"] = f"Round: {self.number, self.matches}"
            dict_get_round["function"] = f"get_round() : Return the round"
        except Exception as e:
            dict_get_round["number"] = self.number
            dict_get_round["matches"] = self.matches
            dict_get_round["status"] = False
            dict_get_round["message"] = f"Round: {self.number, self.matches}"
            dict_get_round["function"] = f"get_round() : {e}"
        return dict_get_round
        
