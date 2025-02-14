from utils.terminal import clear, width, height, wrap
from controler.Menu import Menu
from controler.Markdown import Markdown
from boundary.View import View
from boundary.Keyboard import Keyboard
from controler.AutoPlayer import AutoPlayer
from controler.autoplayer.HumanIA import HumanIA

class MenuView :
    def __init__(self, menu:Menu) :
        """
        Initialise une vue de menu de jeu.

        Parameters:
        -----------
        menu : Menu
            Le menu de jeu.
        """

        self.menu = menu
    
    def _choice(self, buttons:list[tuple[str, int, bool]]) -> int :
        """
        Demande de choisir un bouton.

        Parameters:
        -----------
        buttons : list[tuple[str, int, bool]]
            Les boutons disponibles.

        Returns:
        --------
        int
            L'indice du bouton choisi.
        """

        for b in buttons : # Affiche les boutons
            self._print_button(b[0], b[1], b[2])

        ch = ""
        n = 0
        while True : # Attend une saisie
            ch = Keyboard.getch() # Récupère un caractère
            match ch :
                case Keyboard.TOP : # Déplace le curseur
                    self._print_button(buttons[n][0], buttons[n][1])
                    n = max(0, n-1)
                    self._print_button(buttons[n][0], buttons[n][1], True)
                case Keyboard.DOWN :
                    self._print_button(buttons[n][0], buttons[n][1])
                    n = min(len(buttons)-1, n+1)
                    self._print_button(buttons[n][0], buttons[n][1], True)
                case Keyboard.NL : # Valide le choix
                    break
        
        return n
    
    def start(self) -> None:
        """
        Affiche le menu de jeu.
        """

        clear() # Efface l'écran
        print("\033[?25l", end="", flush=True) # Cache le curseur

        print("\033[1m" # Gras
              "╔══════╦══════╦══╗\n"
              "║╔═╗   ╚╗  ╔══╬╗╔╣\n"
              "╠╝╔╝╔═══╩══╩═╗╚╬╝║\n"
              "║ ╠═╣ Arbuba ╠╗╚═╣\n"
              "║╔╝╔╩═╦══════╝╚╗ ║\n"
              "╠╣ ║  ╚══╗  ╔══╝ ║\n"
              "╚╩═╩═════╩══╩════╝\n"
              "\033[0m", # Normal
              end="")
        
        buttons = [
            ("Jouer"  ,  9,  True), # Texte et hauteur des boutons
            ("Règles" , 12, False),
            ("Quitter", 15, False),
        ]

        n = self._choice(buttons) # Demande de choisir un bouton
        
        match n : # Exécute l'action correspondante
            case 0 :
                autoplayer = self._choice_player()
                view = View(self.menu.get_game(), autoplayer, HumanIA(self.menu.get_game()))
                view.play()
                while True :
                    ch = Keyboard.getch()
                    if ch == Keyboard.NL :
                        break
            case 1 :
                self._rules()
            case 2 :
                return
    
    def end(self) -> None :
        """
        Remet l'écran en état initial.
        """

        clear()
        print("\033[?25h", end="", flush=True) # Remet le curseur
    
    def _print_button(self, label:str, line:int=None, focus:bool=False) -> None:
        """
        Affiche un bouton.

        Parameters:
        -----------
        label : str
            Le texte du bouton.
        line : int, optional
            Hauteur du bouton.
        focus : bool
            Si le bouton est sélectionné.
        """

        label = label.center(14)

        print((f"\033[{line};1H" if line else "") + # Se déplace à la ligne
                "\033[1m" +                         # Gras
               ("\033[31m" if focus else "") +      # Rouge si focus
                "┌────────────────┐\n"
               f"│ {   label    } │\n"
                "└────────────────┘\n"
                "\033[0m",
                end="")

    def _choice_player(self) -> AutoPlayer :
        """
        Demande de choisir un joueur automatique (ou un humain).

        Returns:
        --------
        AutoPlayer : Le joueur automatique choisi.
        """

        autoplayers = [HumanIA(self.menu.get_game())] + self.menu.get_autoplayers()

        clear()
        
        buttons = [(autoplayers[i].get_name(), 3+i*3, False) for i in range(len(autoplayers))]
        buttons[0] = ("Jouer à deux", buttons[0][1], True)

        n = self._choice(buttons) # Demande de choisir un bouton

        return autoplayers[n]
         
    def _rules(self) -> None:
        """
        Affiche les règles du jeu.
        """

        rules = self.menu.get_rules() # Récupère les règles du jeu
        markdown = Markdown.generate(rules) # Génère le markdown en ASCII et ANSI

        markdown = markdown.split("\n")
        n = 0

        while True : # Attend une saisie
            clear() # Efface l'écran
            h = height()
            slide = wrap(markdown, width())[n:n+h]
            print(*slide, sep="\n", end="")
            
            ch = Keyboard.getch() # Récupère un caractère
            match ch :
                case Keyboard.NL :
                    break
                case Keyboard.TOP :
                    n = max(0, n-2)
                case Keyboard.DOWN :
                    n = min(len(markdown), n+2)

        self.start()