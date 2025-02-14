from typing import Callable

from utils.terminal import clear
from controler.Game import Game
from utils.Pawn import Pawn

class View:
    def __init__(self, game:Game, iptBlack:Callable[[], str]=input, iptWhite:Callable[[], str]=input) :
        """
        Construit une interface utilisateur prenant en entrée un jeu et deux fonctions de saisie de coup.

        Parameters:
        -----------
        game : Game
            Le jeu.
        iptBlack : Callable[[], str], optional
            La fonction de saisie de coup du joueur bleu.
        iptWhite : Callable[[], str], optional
            La fonction de saisie de coup du joueur rouge.
        """
        self.game = game
        self.iptWhite = iptWhite
        self.iptBlack = iptBlack

    def _board(self) -> None:
        """
        Affiche un plateau de jeu vide avec des coordonnées (A, B, C... et 1, 2, 3...).
        """

        size = self.game.get_size()
        
        letters = "    " + "   ".join(chr(65 + i) for i in range(size))
        result = []

        result.append("  ┌───" + ("┬───" * (size - 1)) + "┐") # Bordure supérieure
        
        for i in range(size):
            row = f"{i + 1} │ " + " │ ".join(" " for _ in range(size)) + " │" # Ligne vide
            result.append(row)
            
            if i < size - 1:
                result.append("  ├───" + ("┼───" * (size - 1)) + "┤") #  Ligne de séparation
        
        result.append("  └───" + ("┴───" * (size - 1)) + "┘") # Bordure inférieure
        result.append(letters)

        clear() # Efface l'écran
        print("\n".join(result)) # Affiche le plateau de jeu.


    def _pawn(self, x:int, y:int, p:Pawn) -> None:
        """
        Affiche un pion sur le plateau de jeu.

        Parameters:
        -----------
        x : int
            La coordonnée x du pion.
        y : int
            La coordonnée y du pion.
        p : Pawn
            La valeur du pion.
        """

        print("\033[" + str(2*y+2) + ";" + str(4*x+5) + "H", end="") # Se déplace à la position (x, y) du plateau de jeu
        match p :
            case Pawn.BLACK :
                print("\033[34m●\033[0m") # Affiche un pion bleu. Rappel : \033[34m change la couleur du texte en bleu, \033[0m réinitialise la couleur (voir README.md)
            case Pawn.WHITE :
                print("\033[31m●\033[0m") # Affiche un pion rouge. Rappel : \033[31m change la couleur du texte en rouge (voir README.md)
            case Pawn.VOID :
                print(" ") # Affiche une case vide et efface le pion précédent si présent
    
    def _pawns(self) -> None :
        """
        Affiche les pions du plateau de jeu.
        """

        for x, y, p in self.game.get_pawns() :
            self._pawn(x, y, p)
    
    def _erase(self) -> None :
        """
        Efface les cases du plateau de jeu.
        """

        for i in range(self.game.get_size()) :
            for j in range(self.game.get_size()) :
                self._pawn(i, j, Pawn.VOID)
    
    def _input(self) -> tuple[int, int, int, int] :
        """
        Demande à l'utilisateur de saisir un coup.

        Returns:
        --------
        tuple[int, int, int, int]
            Les coordonnées du coup.
        """

        match self.game.get_current_player() :
            case Pawn.BLACK :
                player = "\033[34m●\033[0m" # Pion bleu
                _input = self.iptBlack.input
            case Pawn.WHITE :
                player = "\033[31m●\033[0m" # Pion rouge
                _input = self.iptWhite.input
            case Pawn.VOID :
                player = " " # Case vide
        
        while True : # Demande une saisie tant que le coup n'est pas valide

            print("\033[" + str(2*self.game.get_size()+3) + ";0H") # Se déplace à la dernière ligne du plateau

            print("\033[2K" + player + " ", end="") # Efface la ligne et affiche le joueur courant et la demande de coup. Rappel : \u2081 et \u2082 affichent les indices en exposant (voir README.md)
            
            ipt = _input()

            if len(ipt) == 0 or ipt == "pass" : # Si la saisie est vide ou égale à "pass", le joueur passe son tour
                return (-1, -1, -1, -1)
            
            if ipt == "exit" or ipt == "quit" or ipt == "q" : # Si la saisie est égale à "exit", "quit" ou "q", on arrête la partie
                return (-2, -2, -2, -2)

            if len(ipt) != 4 : # Si la saisie n'est pas de la forme "ABCD", on redemande une saisie
                continue
            
            x1 = ipt[0]
            y1 = ipt[1]
            x2 = ipt[2]
            y2 = ipt[3]

            if not x1.isalpha() or not y1.isdigit() or not x2.isalpha() or not y2.isdigit() : # Si les coordonnées ne sont pas des lettres ou des chiffres, on redemande une saisie
                continue
            
            x1 = ord(x1.upper()) - 65 # Conversion des lettres en nombres (A -> 0, B -> 1, C -> 2, ...)
            y1 = int(y1) - 1
            x2 = ord(x2.upper()) - 65
            y2 = int(y2) - 1

            if (not (0 <= x1 < self.game.get_size()) or
                not (0 <= y1 < self.game.get_size()) or
                not (0 <= x2 < self.game.get_size()) or
                not (0 <= y2 < self.game.get_size())) : # Si les coordonnées ne sont pas dans le plateau de jeu, on redemande une saisie
                continue
            
            return x1, y1, x2, y2

    def play(self) -> None :
        """
        Joue une partie.
        """

        winner = Pawn.VOID

        self._board() # Affiche le plateau de jeu

        while True :
            self._erase() # Efface les pions
            self._pawns() # Affiche les pions

            x1, y1, x2, y2 = self._input() # Demande un coup

            if (x1, y1, x2, y2) == (-2, -2, -2, -2) : # Si le joueur quitte la partie
                break

            if (x1, y1, x2, y2) == (-1, -1, -1, -1) : # Si le joueur passe son tour
                self.game.pass_turn()
                continue

            if self.game.play(x1, y1, x2, y2) : # Si le coup est valide, on le valide auprès du jouer
                match self.game.get_current_player() :
                    case Pawn.BLACK :
                        self.iptBlack.played()
                    case Pawn.WHITE :
                        self.iptWhite.played()

            winner = self.game.is_finished() # Vérifie si la partie est terminée

            if winner != Pawn.VOID : # Si la partie est terminée, on arrête la boucle
                break
        
        return winner