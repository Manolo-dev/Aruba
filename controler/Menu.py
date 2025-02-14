import os

from controler.AutoPlayer import AutoPlayer
from controler.Game import Game

class Menu :
    def __init__(self, game:Game, autoplayers:list[AutoPlayer]=[]) :
        """
        Initialise un menu de jeu avec les règles et une liste de joueurs automatiques.

        Parameters:
        -----------
        game : Game
            Le jeu.
        autoplayers : list, optional
            La liste des joueurs automatiques.
        """

        self.rulesfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "../sources/rules.md"))
        self.game = game
        self.autoplayers = autoplayers
    
    def get_rules(self) -> str :
        """
        Retourne les règles du jeu.

        Returns:
        --------
        str
            Les règles du jeu.
        """

        with open(self.rulesfile, "r") as f :
            return f.read()
    
    def get_autoplayers(self) -> list[AutoPlayer] :
        """
        Retourne la liste des joueurs automatiques.

        Returns:
        --------
        list[AutoPlayer]
            La liste des joueurs automatiques.
        """

        return self.autoplayers

    def add_autoplayer(self, autoplayer:AutoPlayer) :
        """
        Ajoute un joueur automatique.

        Parameters:
        -----------
        autoplayer : AutoPlayer
            Le joueur automatique à ajouter.
        """

        self.autoplayers.append(autoplayer)
    
    def get_game(self) -> Game :
        """
        Retourne le jeu.

        Returns:
        --------
        Game
            Le jeu.
        """

        return self.game