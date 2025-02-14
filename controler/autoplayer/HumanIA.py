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
        
        self.game = game
        self.shots = []
        self.name = "HumanIA"

    def input(self) -> str :
        """
        Retourne un coup 

        Returns:
        --------
        str : Le coup aléatoire.
        """

        itp = input()

        self.shots.append(itp)

        return itp