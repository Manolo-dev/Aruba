from abc import ABC, abstractmethod
from controler.Game import Game

class AutoPlayer(ABC):
    def __init__(self, game:Game):
        """
        Construit un joueur automatique prenant en entrée un jeu.

        Parameters:
        -----------
        game : Game
            Le jeu.
        """
        self.game = game
        self.temp_shot = ""
        self.shots = []
        self.name = ""

    @abstractmethod
    def input(self) -> str:
        """
        Méthode pour générer le coup du joueur automatique.

        Returns:
        --------
        str
            Le coup choisi par le joueur.
        """
        pass

    def get_name(self) -> str :
        """
        Retourne le nom du joueur automatique.

        Returns:
        --------
        str
            Le nom du joueur automatique.
        """

        return self.name

    def played(self) -> None :
        """
        Valide le dernier coup.
        """

        self.shots.append(self.temp_shot) # Ajoute le coup
        self.temp_shot = ""
