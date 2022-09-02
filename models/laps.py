class Laps:

    def __init__(self, laps=[]):
        self.laps = laps
        self.laps_id = 1

    def increment_laps_id(self):
        self.laps_id += 1
        return self.laps_id

    def __str__(self):
        message = "Laps: " + self.laps + "\n"
        return message

    def __repr__(self):
        return f"{self.laps}"

    def __eq__(self, other):
        pass
    

