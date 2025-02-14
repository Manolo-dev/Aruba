from math import sqrt

from utils.Pawn import Pawn
from utils.Move import Move

class Board :
    def __init__(self, size:int, config:list[tuple[int, int, Pawn]]=None) :
        """
        Initialise un nouveau plateau de jeu de la taille spécifiée, avec une configuration initiale optionnelle.

        Le plateau est une grille carrée de `size x size` remplie selon le schéma suivant :
        - La moitié supérieure gauche (excluant la diagonale centrale) est remplie de pions bleus (`Pawn.BLACK`).
        - La moitié inférieure droite (excluant la diagonale centrale) est remplie de pions rouges (`Pawn.WHITE`).
        - La diagonale centrale est divisée en deux parties :
            - Une partie avec des pions rouges (`Pawn.WHITE`).
            - Une autre partie avec des pions bleus (`Pawn.BLACK`).
            - Une ou deux cases peuvent rester vides (`Pawn.VOID`), selon que `size` est pair ou impair.

        Parameters:
        -----------
        size : int
            La taille du plateau. Automatiquement compris entre 3 et 9.
        config : list[list[Pawn]], optional
            La configuration initiale du plateau de jeu. Par défaut, le plateau est initialisé avec une configuration standard.
            Configuration : liste de tuples contenant les coordonnées et la valeur des pions.
        """

        # Si la taille n'est pas comprise entre 3 et 9, on l'ajuste
        if size <= 1 :
            size = 3
        if size >= 10 :
            size = 9

        board = [[Pawn.VOID for i in range(size)] for j in range(size)] # Crée un plateau de jeu vide grâce à une liste en compréhension (voir README.md)

        if config is not None : # Si une configuration est spécifiée, on place les pions selon cette configuration
            for x, y, p in config :
                board[y][x] = p

        else : # Sinon, on initialise le plateau avec une configuration standard (voir README.md)
            for i in range(size) :
                if i < (size-2)/2 :
                    board[-i-1][i] = Pawn.BLACK
                    board[i][-i-1] = Pawn.WHITE
                for j in range(size) :
                    if j < i :
                        board[-i-1][j] = Pawn.BLACK
                        board[i][-j-1] = Pawn.WHITE
        
        self.board = board
        self.size = size
    
    def get(self, x:int, y:int) -> Pawn :
        """
        Retourne la valeur du pion à la position spécifiée.

        Parameters:
        -----------
        x : int
            Coordonnée en abscisse (colonne) du pion.
        y : int
            Coordonnée en ordonnée (ligne) du pion.
        
        Returns:
        --------
        Pawn
            La valeur du pion à la position spécifiée.
        """

        return self.board[y][x]
    
    def get_pawns(self) -> list[tuple[int, int, Pawn]] :
        """
        Retourne les pions du plateau de jeu. Chaque pion est représenté par un tuple contenant ses coordonnées et sa valeur.
        
        Returns:
        --------
        list[tuple[int, int, Pawn]]
            Les pions du plateau de jeu.
        """

        # NOTE: On pourrait utiliser le yield pour optimiser la mémoire et avoir un code plus propre, mais cela empièterait sur la lisibilité

        result = []

        for i in range(self.size) : # On parcourt chaque case du plateau
            for j in range(self.size) :
                if self.board[i][j] != Pawn.VOID :
                    result.append((j, i, self.board[i][j]))  # On ajoute le pion à la liste

        return result

    def set(self, x:int, y:int, value:Pawn) -> None :
        """
        Modifie la valeur du pion à la position spécifiée.

        Parameters:
        -----------
        x : int
            Coordonnée en abscisse (colonne) du pion.
        y : int
            Coordonnée en ordonnée (ligne) du pion.
        value : Pawn
            La nouvelle valeur du pion.
        """

        self.board[y][x] = value
    
    def get_size(self) -> int :
        """
        Retourne la taille du plateau de jeu.

        Returns:
        --------
        int
            La taille du plateau de jeu.
        """

        return self.size

    def move_type(self, x1:int, y1:int, x2:int, y2:int) -> Move :
        """
        Vérifie si un déplacement est valide.

        Un pion peut se déplacer de deux façons :
        1. Déplacement simple : Le pion peut aller sur une case adjacente (horizontale, verticale ou diagonale) si celle-ci est vide (`Pawn.VOID`).
        2. Saut avec prise : Un pion peut sauter par-dessus un pion adverse si :
            - L'adversaire est adjacent (horizontale, verticale ou diagonale).
            - La case située immédiatement après (dans l'alignement) est vide (`Pawn.VOID`).
            - Le pion sauté est de couleur opposée.

        Parameters:
        -----------
        x1 : int
            Coordonnée en abscisse (colonne) de la position initiale.
        y1 : int
            Coordonnée en ordonnée (ligne) de la position initiale.
        x2 : int
            Coordonnée en abscisse (colonne) de la position de destination.
        y2 : int
            Coordonnée en ordonnée (ligne) de la position de destination.

        Returns:
        --------
        bool
            `True` si le déplacement est valide, sinon `False`.
        """

        if (not (0 <= x1 < self.size) or
            not (0 <= y1 < self.size) or
            not (0 <= x2 < self.size) or
            not (0 <= y2 < self.size)) : # Si les coordonnées ne sont pas dans le plateau de jeu
            return Move.INVALID

        # Récupère le pion et la destination
        p1 = self.get(x1, y1)
        p2 = self.get(x2, y2)
        d = sqrt((x2-x1)**2 + (y2-y1)**2) # Calcule la distance entre les deux positions

        if p1 == Pawn.VOID : # On essaie de déplacer un pion d'une case vide
            return Move.INVALID
        
        if d == 0 : # Le surplace est invalide
            return Move.INVALID
        
        if d == 1 or d == sqrt(2) : # Déplacement simple
            if p2 == Pawn.VOID :
                return Move.SIMPLE
        
        if d == 2 or d == sqrt(8) : # Saut avec prise
            p3 = self.get((x1+x2)//2, (y1+y2)//2) # Récupère le pion sauté

            if p2 == Pawn.VOID and p3 != Pawn.VOID and p3 != p1 : # Prise d'un pion adverse et arrivée sur une case vide
                return Move.TAKE

        return Move.INVALID # Déplacement invalide (par défaut, ne devrait pas être atteint)s

    def move(self, x1:int, y1:int, x2:int, y2:int) -> None :
        """
        Déplace un pion sur le plateau de jeu.

        Parameters:
        -----------
        x1 : int
            Coordonnée en abscisse (colonne) de la position initiale.
        y1 : int
            Coordonnée en ordonnée (ligne) de la position initiale.
        x2 : int
            Coordonnée en abscisse (colonne) de la position de destination.
        y2 : int
            Coordonnée en ordonnée (ligne) de la position de destination.
        """

        self.set(x2, y2, self.get(x1, y1))
        self.set(x1, y1, Pawn.VOID)
    
    def take(self, x1:int, y1:int, x2:int, y2:int) -> None :
        """
        Retire le pion adverse lors d'un saut et déplace le pion courant à sa nouvelle position.

        Parameters:
        -----------
        x1 : int
            Coordonnée en abscisse (colonne) de la position initiale.
        y1 : int
            Coordonnée en ordonnée (ligne) de la position initiale.
        x2 : int
            Coordonnée en abscisse (colonne) de la position de destination.
        y2 : int
            Coordonnée en ordonnée (ligne) de la position de destination.
        """

        self.set(x2, y2, self.get(x1, y1))
        self.set(x1, y1, Pawn.VOID)
        self.set((x1+x2)//2, (y1+y2)//2, Pawn.VOID) # Retire le pion adverse