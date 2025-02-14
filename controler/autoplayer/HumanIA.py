from random import choice

from controler.Game import Game
from controler.AutoPlayer import AutoPlayer

class HumanIA(AutoPlayer) :
    def __init__(self, game:Game) :
        """
        Construit un joueur non-automatique prenant en entrée un jeu.

        Parameters:
        -----------
        game : Game
            Le jeu.
        """

        super().__init__(game) # Appel du constructeur de la classe mère
        
        self.name = "HumanIA"

    def input(self) -> str :
        """
        Retourne un coup 

        Returns:
        --------
        str
            Le coup aléatoire.
        """

        itp = input()

        self.last_shot = itp # Enregistre

        return itp