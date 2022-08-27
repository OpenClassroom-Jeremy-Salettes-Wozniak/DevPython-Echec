# IMPORT

# VARIABLES

# CLASSES
import os
from random import choices


class Views: 

    def __init__(self):
        pass

    def accueilViews(self):
        """ 
        Affiche la page d'accueil
        """
        print("############## MENU PRINCIPAL ##############")
        print("")
        print("1 - Créer un nouveau tournoi")
        print("2 - Continuer un tournoi")
        print("3 - Rapport d'un tournoi")
        print("4 - Quitter")
        print("")
        return input("Veuillez entrer un nombre entre 1 et 4 : ")
    
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

    def createTournamentViews(self):
        """
        Affiche un formulaire
        """
        print("############## CREATION DE TOURNOI ##############")
        print("")
        print("Nom du tournoi : ")
        name = str(input())
        print("Lieux du tournoi : ")
        location = str(input())
        print("Date du tournoi au format YYYY-MM-DD : ")
        date = str(input())
        print("Nombre de tours : ")
        nb_laps = str(input())
        print("Tournées (liste des instances rondes): ")
        Tournées = str(input())
        print("players (liste des instances joueurs): ")
        players = str(input())
        print("Controle de temps (liste des instances controle de temps): ")
        print("1 - bullet")
        print("2 - blitz")
        print("3 - rapid")
        controle_de_temps = str(input())
        while controle_de_temps != "1" and controle_de_temps != "2" and controle_de_temps != "3":
            print("Veuillez entrer un nombre entre 1 et 3 :")
            controle_de_temps = str(input())
        # if controle_de_temps == "1":
        #     controle_de_temps = "bullet"
        # elif controle_de_temps == "2":
        #     controle_de_temps = "blitz"
        # elif controle_de_temps == "3":
        #     controle_de_temps = "rapid"
        # else:
        #     self.erreurInput("Veuillez entrer un nombre entre 1 et 3")
        #     controle_de_temps = str(input())
        print("Description du tournoi : ")
        description = str(input())
        print("")
        print("############## TOURNOI CREE ##############")
        print("")
        print("Nom du tournoi : " + name)
        print("Lieux du tournoi : " + location)
        print("Date du tournoi : " + date)
        print("Nombre de tours : " + nb_laps)
        print("Tournées (liste des instances rondes): " + Tournées)
        print("players (liste des instances joueurs): " + players)
        print("Controle de temps (liste des instances controle de temps): " + controle_de_temps)
        print("Description du tournoi : " + description)
        print("")
        return name, location, date, nb_laps, Tournées, players, controle_de_temps, description


        

