# IMPORT

# VARIABLES

# CLASSES
class Tournois:
    
    def __init__(self, nom, lieu, date, tournees, joueurs, controle_temps, description, nb_tours=4):
        """
        """
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours
        self.tournees = tournees
        self.joueurs = joueurs
        self.controle_temps = controle_temps
        self.description = description
