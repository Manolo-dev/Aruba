from random import choice

from controler.Game import Game
from controler.AutoPlayer import AutoPlayer

class RandomIA(AutoPlayer) :
    def __init__(self, game:Game) :
        """
        Construit un joueur automatique prenant en entrée un jeu.

        Parameters:
        -----------
        game : Game
            Le jeu.
        """
        
        self.game = game
        self.shots = []
        self.name = "RandomIA"

    def input(self) -> str :
        """
        Retourne un coup aléatoire autorisé par le jeu.

        Returns:
        --------
        str : Le coup aléatoire.
        """

        while True : # Continue jusqu'à ce qu'un pion ait un coup possible
            player = self.game.get_current_player() # Récupère le joueur courant

            pawns = [(x, y) for x, y, p in self.game.get_pawns() if p == player] # Récupère les coordonnées des pions du joueur courant
            pawn = choice(pawns) # Sélectionne un pion aléatoire

            moves = self.game.get_possible_moves(*pawn) # Récupère les coups possibles pour le pion sélectionné
            if len(moves) > 0 :
                break

        move = choice(moves) # Sélectionne un coup aléatoire

        move_string = f"{chr(97 + pawn[0])}{pawn[1] + 1}{chr(97 + move[0])}{move[1] + 1}" # Convertit les coordonnées en chaîne de caractères
        self.shots.append(move_string) # Ajoute le coup à la liste des coups joués

        return move_string