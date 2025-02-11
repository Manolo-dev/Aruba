from entity.Board import Board
from entity.Pawn import Pawn
from entity.Move import Move

class Game :
    def __init__(self, size:int, config:list[tuple[int, int, Pawn]] = None) :
        """
        Initialise une nouvelle partie de jeu de taille spécifiée, avec une configuration initiale optionnelle.

        Parameters :
        ----------
        size : int
            La taille du plateau de jeu. Automatiquement compris entre 3 et 9.
        config : list[list[Pawn]], optional
            La configuration initiale du plateau de jeu. Par défaut, le plateau est initialisé avec une configuration standard.
        """

        self.board = Board(size, config) # Plateau de jeu
        self.current_player = Pawn.BLACK # Joueur courant. L'énoncé ne précise pas qui commence, donc je choisis le joueur noir par souci de respect des minorités et de la diversité.
        self.possible_moves = [] # Liste des coups autorisés. Si vide alors le joueur n'a aucune restriction de mouvement.
    
    def get_current_player(self) -> Pawn :
        """
        Retourne le joueur courant.

        Returns:
        --------
        Pawn : Le joueur courant.
        """

        return self.current_player
    
    def get_pawns(self) -> list[tuple[int, int, Pawn]] :
        """
        Retourne les pions du plateau de jeu.

        Returns:
        --------
        list[list[int]] : Le plateau de jeu.
        """

        return self.board.get_pawns()
    
    def get_size(self) -> int :
        """
        Retourne la taille du plateau de jeu.

        Returns:
        --------
        int : La taille du plateau de jeu.
        """

        return self.board.get_size()

    def play(self, x1:int, y1:int, x2:int, y2:int) -> bool:
        """
        Joue un coup sur le plateau de jeu.

        Le coup est effectué par le joueur courant. Les coordonnées du coup sont spécifiées par les paramètres `x1`, `y1`, `x2` et `y2`.

        Parameters:
        -----------
        x1 : int
            La coordonnée x de la case de départ du coup.
        y1 : int
            La coordonnée y de la case de départ du coup.
        x2 : int
            La coordonnée x de la case d'arrivée du coup.
        y2 : int
            La coordonnée y de la case d'arrivée du coup.

        Returns:
        --------
        bool : True si le coup a été joué avec succès, False sinon.
        """

        if self.possible_moves != [] and (x1, y1, x2, y2) not in self.possible_moves : #  Le joueur doit prendre un pion et qu'il ne le fait pas
            return False
        
        move = self.board.move_type(x1, y1, x2, y2)

        if self.board.get(x1, y1) != self.current_player : # Le joueur ne joue pas un de ses pions
            return False
        
        if move == Move.INVALID : # Coup invalide
            return False

        match move :
            case Move.SIMPLE : # Déplacement simple
                self.board.move(x1, y1, x2, y2)
                self.pass_turn()
                
                return True
            case Move.TAKE : # Prise
                self.board.take(x1, y1, x2, y2) # Prend le pion

                possible_takes = [(i, j) for i, j, mve in self.get_possible_moves(x2, y2) if mve == Move.TAKE] # Vérifie si le joueur peut prendre un autre pion

                self.possible_moves = [(x2, y2, i, j) for i, j, mve in self.get_possible_moves(x2, y2) if mve == Move.TAKE] # Liste les prises possibles

                if len(possible_takes) == 0 : # Si le joueur ne peut pas prendre un autre pion
                    self.pass_turn() # Passe le tour du joueur

                return True
            
    def pass_turn(self) -> None :
        """
        Passe le tour du joueur courant.
        """

        self.current_player = Pawn.WHITE if self.current_player == Pawn.BLACK else Pawn.BLACK # Change le joueur courant, utilisation de l'opérateur ternaire (voir README.md)
        self.possible_moves = [] # Réinitialise les coups possibles, rappel: si vide alors le joueur n'a aucune restriction de mouvement.

    
    def is_finished(self) -> Pawn :
        """
        Vérifie si la partie est terminée.

        Returns:
        --------
        bool : True si la partie est terminée, False sinon.
        """

        winner = Pawn.VOID # Initialise un gagnant non défini
        for i in range(self.board.size) : # Parcours le plateau de jeu
            for j in range(self.board.size) :
                if self.board.get(i, j) != Pawn.VOID :
                    if winner == Pawn.VOID :
                        winner = self.board.get(i, j) # Définit le gagnant si non défini
                    elif winner != self.board.get(i, j) : # Il reste des pions adverses
                        return Pawn.VOID
        
        return winner

    def __str__(self) -> str :
        """
        Représentation textuelle de la partie.

        Returns:
        --------
        str : Représentation textuelle de la partie.
        """

        return str(self.board)

    def get_possible_moves(self, x:int, y:int) -> list[tuple[int, int, Move]] :
        """
        Retourne les coups possibles pour un pion.

        Parameters:
        -----------
        x : int
            La coordonnée x du pion.
        y : int
            La coordonnée y du pion.

        Returns:
        --------
        list[tuple[int, int, Move]] : Les coups possibles pour le pion.
        """

        result = []

        for i in range(-1, 2) :
            for j in range(-1, 2) :
                for k in range(1, 3) : # Parcours les cases à une distance de 1 ou 2 autour du pion
                    move = self.board.move_type(x, y, x+i*k, y+j*k)

                    if move != Move.INVALID :
                        result.append((x+i*k, y+j*k, move)) # Ajoute le déplacement valide à la liste des coups possibles
        
        return result