# IMPORT

# VARIABLES

# CLASSES
import os


class Views: 

    def __init__(self):
        pass

################################
############ ACCUEIL ###########
################################
    def accueilViews(self):
        """ 
        Affiche la page d'accueil
        """
        print("############## MENU PRINCIPAL ##############")
        print("")
        print("1 - Créer un nouveau tournoi")
        print("2 - Selectionner un tournoi")
        print("3 - Rapport de tournoi")
        print("4 - Créer un nouveau joueur")
        print("5 - Quitter")
        print("")
        return input("Veuillez entrer un nombre entre 1 et 5 : ")

#################################
######## GESTION ERREUR #########    
#################################
    def erreurInput(self, message, fonction=False):
        """
        Affiche un message d'erreur
        """
        print("################## ERREUR ##################")
        print("")
        print(message)
        print("")
        if fonction != False:
            fonction()
        else:
            return False

#################################
############ TOURNAMENT #########
#################################
    def createTournamentViews(self):
        """
        Affiche un formulaire pour créer un nouveau tournoi
        """
        name = input("Veuillez entrer le nom du tournoi : ")
        location = input("Veuillez entrer le lieu du tournoi : ")
        date = input("Veuillez entrer la date du tournoi : ")
        laps = input("Veuillez entrer le nombre de tours du tournoi : ")
        laps_instance = input("Veuillez entrer le nombre de match par tour : ")
        players = input("Veuillez entrer le nom des joueurs séparés par une virgule : ")
        control_time = input("Veuillez entrer le temps de contrôle : ")
        description = input("Veuillez entrer une description du tournoi : ")

        # On vérifie que les inputs sont corrects
        return {
                "name": name,
                "location": location,
                "date": date,
                "laps": laps,
                "laps_instance": laps_instance,
                "players": players,
                "control_time": control_time,
                "description": description
        }

#################################
############ PLAYER #############
#################################
    def createPlayerViews(self):
        """
        Affiche un formulaire pour créer un nouveau joueur
        """
        name = input("Veuillez entrer le nom du joueur : ")

if __name__ == "__main__":
    Views().createTournamentViews()