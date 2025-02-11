import os

from controler.Game import Game

class Menu :
    def __init__(self, game:Game) :
        """
        Initialise un menu de jeu.

        Parameters:
        -----------
        game : Game
            Le jeu.
        """

        self.rulesfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../sources/rules.md"))
        self.game = game
    
    def get_rules(self) :
        """
        Retourne les règles du jeu.

        Returns:
        --------
        str : Les règles du jeu.
        """

        with open(self.rulesfile, "r") as f :
            return f.read()