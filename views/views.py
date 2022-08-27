# IMPORT

# VARIABLES

# CLASSES
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
    
