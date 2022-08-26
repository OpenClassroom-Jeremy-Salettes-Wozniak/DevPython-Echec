# IMPORT

# VARIABLES

# CLASSES
class Matchs:

    def __init__(self, players):
        self.players = players
        self.matchs = []
        self.matchs.append(self.creer_un_match(self.players))
        print(self.matchs)
        pass

    def creer_un_match(self, joueur1, joueur2, score_joueur1, score_joueur2):
        match = {
            "joueur1": joueur1,
            "joueur2": joueur2,
            "score_joueur1": score_joueur1,
            "score_joueur2": score_joueur2
        }
        return match
    