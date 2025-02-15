from typing import Optional

from controler.Game import Game
from controler.AutoPlayer import AutoPlayer
from utils.Move import Move
from utils.Pawn import Pawn
from copy import deepcopy
from boundary.Keyboard import Keyboard
from utils.terminal import clear

class HeuristIA(AutoPlayer) :
    def __init__(self, game:Game, validation:bool=True) :
        """
        Construit un joueur automatique basé sur une heuristique simple.

        - Prioriser les captures
        - Maximiser les captures enchaînées
        - Minimiser les options adverses

        Parameters:
        -----------
        game : Game
            Le jeu.
        validation : bool, optional
            Si True, attend une validation pour jouer le coup.
        """

        super().__init__(game)
        self.name = "HeuristIA"
        self.validation = validation

    def input(self) -> str :
        """
        Retourne un coup basé sur une heuristique.

        Returns:
        --------
        str
            Le coup sélectionné.
        """

        player = self.game.get_current_player()

        best_move = self._get_best(self.game, player)

        if best_move is None :
            return "pass"

        pawn, move = best_move
        move_string = f"{chr(97 + pawn[0])}{pawn[1] + 1}{chr(97 + move[0])}{move[1] + 1}"
        
        self.last_shot = move_string

        while self.validation : # Attend une validation
            ch = Keyboard.getch()
            if ch == Keyboard.NL :
                break

        return move_string
    
    @staticmethod
    def _get_best(game:Game, player:Pawn) -> Optional[tuple[tuple[int, int], tuple[int, int, Move]]] :
        """
        Retourne le meilleur coup pour un joueur donné.

        Parameters:
        -----------
        game : Game
            Le jeu.
        player : Pawn
            Le joueur.

        Returns:
        --------
        Optional[tuple[tuple[int, int], tuple[int, int, Move]]]
            Le meilleur coup. Les coordonnées sont (x1, y1, x2, y2) avec (x1, y1) la position du pion et (x2, y2) la destination.
        """

        possibles = HeuristIA._get_possibles(game, player)

        if len(possibles) == 0 :
            return None

        best_move = HeuristIA._get_best_move(game, player, possibles)

        return best_move
    
    @staticmethod
    def _get_best_move(game:Game, player:Pawn, possibles:list[tuple[tuple[int, int], tuple[int, int, Move]]]) -> Optional[tuple[tuple[int, int], tuple[int, int, Move]]] :
        """
        Retourne les coups possibles pour un pion donné en fonction des coups possibles.

        Parameters:
        -----------
        game : Game
            Le jeu.
        player : Pawn
            Le joueur.
        possibles : list[tuple[tuple[int, int], tuple[int, int, Move]]]
            Les coups possibles.

        Returns:
        --------
        tuple[tuple[int, int], tuple[int, int, Move]]
            Le meilleur coup.
        """

        best_move = None
        best_score = -float("inf")

        for pawn, move in possibles : # Parcourir tous les coups
            score = HeuristIA._evaluate_move(game, player, pawn, move)

            if score > best_score : # Garder le meilleur coup
                best_score = score
                best_move = (pawn, move)

        return best_move

    @staticmethod
    def _get_possibles(game:Game, player:Pawn) -> list[tuple[tuple[int, int], tuple[int, int, Move]]] :
        """
        Retourne les coups possibles pour un joueur donné.

        Parameters:
        -----------
        game : Game
            Le jeu.
        player : Pawn
            Le joueur.

        Returns:
        --------
        list[tuple[tuple[int, int], tuple[int, int, Move]]]
            La liste des coups possibles.
        """

        return [
            ((x1, y1), (x2, y2, m))
            for x1, y1, p in game.get_pawns() if p == player # Pour chaque pion du joueur
            for x2, y2, m in game.get_possible_moves(x1, y1) # Pour chaque coup possible du pion
        ]

    @staticmethod
    def _evaluate_move(game:Game, player:Pawn, pawn:tuple[int, int], move:Optional[tuple[int, int, Move]]) -> int :
        """
        Évalue un coup en fonction d'une heuristique simple.

        Parameters:
        -----------
        game : Game
            Le jeu réel ou simulé.
        player : Pawn
            Le joueur courant.
        pawn : tuple[int, int]
            La position du pion actuel.
        move : Optional[tuple[int, int, Move]]
            La position de destination.

        Returns:
        --------
        int
            Un score représentant l'intérêt du coup.
        """

        x1, y1 = pawn
        x2, y2, mov = move
        score = 0

        if mov == Move.TAKE : # Vérifier si le mouvement capture un pion adverse
            score += 10  # Bonus pour une capture
        
        if mov == None : # Vérifier si le mouvement existe
            return -float("inf")

        game_copy = deepcopy(game) # Crée une simulation du jeu

        if not game_copy.play(x1, y1, x2, y2) : # Joue le coup sur la simulation
            return -float("inf")
    
        if player == game_copy.get_current_player() : # Vérifie si le joueur peut rejouer dans la simulation
            score += 10
            best_move = HeuristIA._get_best_move(game_copy, player, [((x2, y2), (x, y, m)) for x, y, m in game_copy.get_possible_moves(x2, y2)])
            if best_move is not None :
                score += HeuristIA._evaluate_move(game_copy, player, best_move[0], best_move[1]) # Évalue la meilleure prise suivante dans la simulation

        opp = Pawn.BLACK if player == Pawn.WHITE else Pawn.WHITE
        opp_moves = HeuristIA._get_possibles(game_copy, opp)
        opp_takes = [move for move in opp_moves if move[1][2] == Move.TAKE]
        
        score += len(opp_takes) * -3 # Malus pour les captures adverses
        score += len(opp_moves) * -1 # Malus pour les options adverses
        
        return score