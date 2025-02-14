#=== boundary/__init__.py

#=== boundary/View.py
from typing import Callable

from controler.Game import Game
from entity.Pawn import Pawn

class View:
    def __init__(self, game:Game, iptWhite: Callable[[], str], iptBlack: Callable[[], str]) :
        """
        Construit une interface utilisateur prenant en entrée un jeu et deux fonctions de saisie de coup.

        Parameters:
        -----------
        game : Game
            Le jeu.
        iptWhite : Callable[[], str]
            La fonction de saisie de coup du joueur blanc.
        iptBlack : Callable[[], str]
            La fonction de saisie de coup du joueur noir.
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

        print("\033[H\033[J" + "\n".join(result)) # Efface l'écran et affiche le plateau de jeu. Rappel : \033[H\033[J efface l'écran (voir README.md)


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
                print("\033[30m●\033[0m") # Affiche un pion noir. Rappel : \033[30m change la couleur du texte en noir, \033[0m réinitialise la couleur (voir README.md)
            case Pawn.WHITE :
                print("\033[37m●\033[0m") # Affiche un pion blanc. Rappel : \033[37m change la couleur du texte en blanc (voir README.md)
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
        tuple[int, int, int, int] : Les coordonnées du coup.
        """

        print("\033[" + str(2*self.game.get_size()+3) + ";0H")

        match self.game.get_current_player() :
            case Pawn.BLACK :
                player = "\033[30m●\033[0m" # Pion noir
                _input = self.iptBlack
            case Pawn.WHITE :
                player = "\033[37m●\033[0m" # Pion blanc
                _input = self.iptWhite
            case Pawn.VOID :
                player = " " # Case vide
        
        while True : # Demande une saisie tant que le coup n'est pas valide

            print("\033[2K" + player + " (x\u2081y\u2081x\u2082y\u2082): ", end="") # Efface la ligne et affiche le joueur courant et la demande de coup. Rappel : \u2081 et \u2082 affichent les indices en exposant (voir README.md)
            
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

            if not self.game.play(x1, y1, x2, y2) : # Si le coup n'est pas valide, on dis caca
                print("caca\n\n", x1, y1, x2, y2)

            winner = self.game.is_finished() # Vérifie si la partie est terminée

            if winner != Pawn.VOID : # Si la partie est terminée, on arrête la boucle
                break

        self._end(winner) # Affiche l'écran de fin de partie

    def _end(self, winner:Pawn) -> None :
        """
        Affiche l'écran de fin de partie.

        Parameters:
        -----------
        winner : Pawn
            Le gagnant de la partie.
        """
        
        print("\033[H\033[J") # Efface l'écran
        print("┌" + "─" * 29 + "┐") # Bordure supérieure
        print("│" + " " * 29 + "│") # Ligne vide

        match winner : # Affiche le gagnant selon sa couleur
            case Pawn.BLACK :
                print("│" + " " * 4 + "Victoire des  noirs !" + " " * 4 + "│") # Rappel : "│" et "─" sont des caractères spéciaux (voir README.md)
            case Pawn.WHITE :
                print("│" + " " * 4 + "Victoire des blancs !" + " " * 4 + "│")
            case Pawn.VOID :
                print("│" + " " * 11 + "Abandon" + " " * 11 + "│")

        print("│" + " " * 29 + "│")  # Ligne vide
        print("└" + "─" * 29 + "┘") # Bordure inférieure
#=== controler/__init__.py

#=== controler/Game.py
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
#=== controler/Menu.py
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
#=== controler/Markdown.py
import re

class Markdown:
    @staticmethod
    def superscript(match:re.Match) -> str:
        """
        Convertit un texte en exposant en texte avec des codes ANSI.

        Parameters:
        -----------
        match : re.Match
            Texte à convertir.

        Returns:
        --------
        str
            Texte converti.
        """

        text = match.group(1)

        ansis = { # Liste des codes ANSI pour les exposants
            "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ⁱ", "j": "ʲ", "k": "ᵏ", "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ", "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ", "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᶲ", "K": "ᶪ", "L": "ᴸ", "M": "ᴹ", "N": "ᴺ", "O": "ᴼ", "P": "ᵽ", "R": "ʳ", "S": "ᵿ", "T": "ᵀ", "U": "ᴿ", "V": "ᵿ", "W": "ʷ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", " ": " ",
        }

        return "".join(ansis.get(char, char) for char in text)  # Remplace les caractères par leurs équivalents en exposants

    @staticmethod
    def subscript(match:re.Match) -> str:
        """
        Convertit un texte en indice en texte avec des codes ANSI.

        Parameters:
        -----------
        match : re.Match
            Texte à convertir.

        Returns:
        --------
        str
            Texte converti.
        """

        text = match.group(1)

        ansis = { # Liste des codes ANSI pour les indices
            "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎", "a": "ₐ", "e": "ₑ", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "r": "ᵣ", "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "x": "ₓ", " ": " ",
        }

        return "".join(ansis.get(char, char) for char in text) # Remplace les caractères par leurs équivalents en indices
    
    @staticmethod
    def latex(math:re.Match) -> str:
        """
        Convertit une formule LaTeX en formule ASCII.

        Parameters:
        -----------
        math : re.Match
            Formule LaTeX à convertir.
        
        Returns:
        --------
        str
            Formule convertie en ASCII.
        """

        math = math.group(1)
        
        replacements = [
            (r"\\frac\b\s*\{(.*?)\}\{(.*?)\}", r"\1 / \2"),  # Fraction
            (r"\\sqrt\b\s*\{(.*?)\}", r"√(\1)"),             # Racine carrée
            (r"\\times\b\s*", "×"),                          # Multiplication
            (r"\\cdot\b\s*", "·"),                           # Produit scalaire
            (r"\\pm\b\s*", "±"),                             # Plus ou moins
            (r"\\mp\b\s*", "∓"),                             # Moins ou plus
            (r"\\div\b\s*", "÷"),                            # Division
            (r"\\leq\b\s*", "≤"),                            # Inférieur ou égal
            (r"\\geq\b\s*", "≥"),                            # Supérieur ou égal
            (r"\\neq\b\s*", "≠"),                            # Différent
            (r"\\approx\b\s*", "≈"),                         # Approximativement
            (r"\\equiv\b\s*", "≡"),                          # Équivalent
            (r"\\infty\b\s*", "∞"),                          # Infini
            (r"\\forall\b\s*", "∀"),                         # Pour tout
            (r"\\exists\b\s*", "∃"),                         # Il existe
            (r"\\nexists\b\s*", "∄"),                        # Il n'existe pas
            (r"\\in\b\s*", "∈"),                             # Appartient
            (r"\\notin\b\s*", "∉"),                          # N'appartient pas
            (r"\\subset\b\s*", "⊂"),                         # Inclus
            (r"\\subseteq\b\s*", "⊆"),                       # Inclus ou égal
            (r"\\cup\b\s*", "∪"),                            # Union
            (r"\\cap\b\s*", "∩"),                            # Intersection
            (r"\\emptyset\b\s*", "∅"),                       # Ensemble vide
            (r"\\mathbb\b\s*\{R\}", "ℝ"),                    # Ensemble des réels
            (r"\\mathbb\b\s*\{N\}", "ℕ"),                    # Ensemble des naturels
            (r"\\mathbb\b\s*\{Z\}", "ℤ"),                    # Ensemble des entiers
            (r"\\mathbb\b\s*\{Q\}", "ℚ"),                    # Ensemble des rationnels
            (r"\\mathbb\b\s*\{C\}", "ℂ"),                    # Ensemble des complexes
            (r"\\mathbb\b\s*\{P\}", "ℙ"),                    # Ensemble des premiers
            (r"\\mathbb\b\s*\{H\}", "ℍ"),                    # Quaternions
            (r"\\alpha\b\s*", "α"),                          # Alpha
            (r"\\beta\b\s*", "β"),                           # Bêta
            (r"\\gamma\b\s*", "γ"),                          # Gamma
            (r"\\delta\b\s*", "δ"),                          # Delta
            (r"\\epsilon\b\s*", "ε"),                        # Epsilon
            (r"\\zeta\b\s*", "ζ"),                           # Zêta
            (r"\\eta\b\s*", "η"),                            # Êta
            (r"\\theta\b\s*", "θ"),                          # Thêta
            (r"\\iota\b\s*", "ι"),                           # Iota
            (r"\\kappa\b\s*", "κ"),                          # Kappa
            (r"\\lambda\b\s*", "λ"),                         # Lambda
            (r"\\mu\b\s*", "μ"),                             # Mu
            (r"\\nu\b\s*", "ν"),                             # Nu
            (r"\\xi\b\s*", "ξ"),                             # Xi
            (r"\\omicron\b\s*", "ο"),                        # Omicron
            (r"\\pi\b\s*", "π"),                             # Pi
            (r"\\rho\b\s*", "ρ"),                            # Rho
            (r"\\sigma\b\s*", "σ"),                          # Sigma
            (r"\\tau\b\s*", "τ"),                            # Tau
            (r"\\upsilon\b\s*", "υ"),                        # Upsilon
            (r"\\phi\b\s*", "φ"),                            # Phi
            (r"\\chi\b\s*", "χ"),                            # Chi
            (r"\\psi\b\s*", "ψ"),                            # Psi
            (r"\\omega\b\s*", "ω"),                          # Oméga
            (r"\\Alpha\b\s*", "Α"),                          # Alpha majuscule
            (r"\\Beta\b\s*", "Β"),                           # Bêta majuscule
            (r"\\Gamma\b\s*", "Γ"),                          # Gamma majuscule
            (r"\\Delta\b\s*", "Δ"),                          # Delta majuscule
            (r"\\Epsilon\b\s*", "Ε"),                        # Epsilon majuscule
            (r"\\Zeta\b\s*", "Ζ"),                           # Zêta majuscule
            (r"\\Eta\b\s*", "Η"),                            # Êta majuscule
            (r"\\Theta\b\s*", "Θ"),                          # Thêta majuscule
            (r"\\Iota\b\s*", "Ι"),                           # Iota majuscule
            (r"\\Kappa\b\s*", "Κ"),                          # Kappa majuscule
            (r"\\Lambda\b\s*", "Λ"),                         # Lambda majuscule
            (r"\\Mu\b\s*", "Μ"),                             # Mu majuscule
            (r"\\Nu\b\s*", "Ν"),                             # Nu majuscule
            (r"\\Xi\b\s*", "Ξ"),                             # Xi majuscule
            (r"\\Omicron\b\s*", "Ο"),                        # Omicron majuscule
            (r"\\Pi\b\s*", "Π"),                             # Pi majuscule
            (r"\\Rho\b\s*", "Ρ"),                            # Rho majuscule
            (r"\\Sigma\b\s*", "Σ"),                          # Sigma majuscule
            (r"\\Tau\b\s*", "Τ"),                            # Tau majuscule
            (r"\\Upsilon\b\s*", "Υ"),                        # Upsilon majuscule
            (r"\\Phi\b\s*", "Φ"),                            # Phi majuscule
            (r"\^\{(.*)\}", Markdown.superscript),           # Exposants
            (r"\^(.)", Markdown.superscript),                # Exposants
            (r"_\{(.*)\}", Markdown.subscript),              # Indices
            (r"_(.)", Markdown.subscript),                   # Indices
        ]
        
        for pattern, replacement in replacements:  # Applique les remplacements LaTeX -> ASCII
            math = re.sub(pattern, replacement, math)

        return "\033[3m" + math + "\033[0m"  # Met la formule en italique
    
    @staticmethod
    def generate(md_text: str) -> str:
        """
        Convertit un texte Markdown en texte avec ANSI escapes et ASCII pour la mise en forme.

        Parameters:
        -----------
        md_text : str
            Le texte en Markdown.
        
        Returns:
        --------
        str
            Le texte en ASCII avec les codes ANSI.
        """
        
        lines = md_text.split("\n")
        output = []

        for line in lines:
            if match := re.match(r"^(#{1,6}) (.*)$", line):  # Vérifie si la ligne est un titre
                level = len(match.group(1))  # Niveau du titre
                title = match.group(2)  # Texte du titre
                
                match level:
                    case 1:
                        formatted = "╔" + "═" * (len(title) + 2) + "╗\n" + "║ " + "\033[1m" + title + "\033[0m" + " ║\n" + "╚" + "═" * (len(title) + 2) + "╝"
                    case 2:
                        formatted = "┌" + "─" * (len(title) + 2) + "┐\n" + "│ " + "\033[1m" + title + "\033[0m" + " │\n" + "╘" + "═" * (len(title) + 2) + "╛"
                    case 3:
                        formatted = "┌" + "─" * (len(title) + 2) + "┐\n" + "│ " + "\033[1m" + title + "\033[0m" + " │\n" + "└" + "─" * (len(title) + 2) + "┘"
                    case 4:
                        formatted = " " + "\033[1m" + title + "\033[0m" + " \n" + "═" * (len(title) + 2)
                    case 5:
                        formatted = " " + "\033[1m" + title + "\033[0m" + " \n" + "╍" * (len(title) + 2)
                    case 6:
                        formatted = " " + "\033[1m" + title + "\033[0m" + " \n" + "─" * (len(title) + 2)
                
                output.append(formatted)
            else:  # Si la ligne n'est pas un titre
                replacements = [
                    (r"\*\*(.*?)\*\*", r"\033[1m\1\033[0m"),                               # Gras
                    (r"__(.*?)__", r"\033[1m\1\033[0m"),                                   # Gras
                    (r"\*(.*?)\*", r"\033[3m\1\033[0m"),                                   # Italique
                    (r"_(.*?)_", r"\033[3m\1\033[0m"),                                     # Italique
                    (r"\~\~(.*?)\~\~", r"\033[9m\1\033[0m"),                               # Barré
                    (r"\`(.*?)\`", r"\033[2m\1\033[0m"),                                   # Code
                    (r"(?<!\033)\[(.*?)\]\((.*?)\)", r"\033]8;;\2\033\\\1\033]8;;\033\\"), # Lien
                    (r"\$(.*?)\$", Markdown.latex),                                # LaTeX
                ]
                
                for pattern, replacement in replacements : # Applique les remplacements markdown -> ANSI
                    line = re.sub(pattern, replacement, line)

                output.append(line)
        
        return "\n".join(output)  # Retourne le texte formaté
#=== controler/AutoPlayer.py
from random import choice

from controler.Game import Game

class AutoPlayer:
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

    def input(self) -> str :
        """
        Retourne un coup aléatoire autorisé par le jeu.

        Returns:
        --------
        str : Le coup aléatoire.
        """

        player = self.game.get_current_player() # Récupère le joueur courant

        pawns = [(x, y) for x, y, p in self.game.get_pawns() if p == player] # Récupère les coordonnées des pions du joueur courant
        pawn = choice(pawns) # Sélectionne un pion aléatoire

        moves = self.game.get_possible_moves(*pawn) # Récupère les coups possibles pour le pion sélectionné
        move = choice(moves) # Sélectionne un coup aléatoire

        move_string = f"{chr(97 + pawn[0])}{pawn[1] + 1}{chr(97 + move[0])}{move[1] + 1}" # Convertit les coordonnées en chaîne de caractères
        self.shots.append(move_string) # Ajoute le coup à la liste des coups joués

        return move_string
#=== entity/Pawn.py
from enum import Enum

class Pawn(Enum) :
    WHITE = "○"
    BLACK = "●"
    VOID =  " "
#=== entity/Move.py
from enum import Enum

class Move(Enum):
    SIMPLE = 1
    TAKE = 2
    INVALID = 3
#=== temp.py