#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ╔══════════════════════════════════════════════════════════════╗
# ║                                                              ║
# ║  Atelier 2 : Représentation, Saisie et Tests                 ║
# ║                                                              ║
# ╚══════════════════════════════════════════════════════════════╝

# ╔══════════════════════════════╗
# ║ Message aux correcteurs      ║
# ╚══════════════════════════════╝
# 
# Si vous trouvez qu'il y a trop de commentaires, que le code est trop fouillis, trop long, peu élégant, je tient à m'excuser.
# J'ai essayé de faire le code le plus compréhensible possible.
# 
# L'affichage du plateau se fait via des caractères unicode.
# Il est possible que l'affichage ne soit pas correcte sur certains terminaux,
# notamment avec certaines polices de caractères (particulièrement sur Windows).
# Il est préférable d'utiliser une police à chasse fixe (monospace) pour un affichage correct du plateau.
# 
# L'affichage des pions se fait avec des "Ansi Escape Sequences".
# Il est possible que l'affichage ne soit pas correcte sur certains terminaux notamment dans des éditeurs comme PyCharm.
# Il est préférable d'utiliser un terminal pour un affichage correct des pions (tapez windows+r puis cmd sous windows).
# 
# Toutes les fonctions sont typées pour faciliter la compréhension du code.
# Certains types sont plutôt complexes ou nécessitent la librairie `typing` de la STL de Python, toute la documentation nécessaire est disponible ci-dessous.
# 
# Si le programme ne tourne pas correctement, il se peut que ce soit dû à un problème sur votre machine. Le programme a été testé sur diverses configurations :
# (Certaines versions n'étaient pas demandées, mais ont été testées pour plus de fiabilité)
#   - Ubuntu 22.04            : Python 3.10.12
#   - Ubuntu 22.04            : Python 3.12.7
#   - Windows 10.0.19044.3086 : Python 3.10.0
#   - Windows 10.0.19044.3086 : Python 3.12.9
#   - WSL2 - Ubuntu 20.04     : Python 3.12.9
#   - MacOS 15.3.1            : Python 3.13.2
#   - MacOS 15.3.1            : Python 3.12.9
#   - Debian 12 - KDE         : Python 3.11.2
#   - Debian 12 - XFCE        : Python 3.11.2
#   - Windows 11.0.26100.3476 : Python 3.12.9
#   - Windows 11.0.26100.3476 : Python 3.13.2
#   - GitHub Codespaces       : Python 3.12.9
# 
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠿⠿⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ # Certains émulateurs de terminal, notamment "Invite de commande Windows", ne supportent pas les ansi escape sequences.
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀ # De même, certains shells python, comme Ipython, modifient le comportement et l'affichage des ansi escape sequences.
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⢡⠀⠀⠀⠀⠀⢀⡈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀ # Il est donc conseillé d'utiliser un émulateur de terminal à jour, et de lancer le programme avec python (en tapant `python3.12` dans le terminal par exemple).
#⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢠⣿⠀⠀⠀⠀⠀⢸⣷⡈⢻⣆⠀⠀⠀⠀⠀⠀⠀ # Si l'affichage ne se fait tout de même pas correctement, vous pouvez essayer de remplacer les `\033` par des `\x1b` dans les chaînes de caractères des "Ansi Escape Sequences".
#⠀⠀⠀⠀⠀⠀⢀⣼⠏⢠⣿⣿⡆⠀⠀⠀⠀⣸⣿⣷⡄⠹⣆⠀⠀⠀⠀⠀⠀ # Attention : Sur les machines des salles de TP de l'université, sous Windows, il est possible que l'affichage ne soit pas correct. Il est recommandé d'utiliser linux ou une machine personnelle.
#⠀⠀⠀⠀⠀⢀⣾⠃⣰⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⡄⠹⣷⡀⠀⠀⠀⠀ # Je conseille ces émulateurs de terminal :
#⠀⠀⠀⠀⢠⡿⠁⣰⣿⣿⣿⣿⣿⠀⠀⠀⢠⣿⣿⣿⣿⣿⣆⠘⣷⡀⠀⠀⠀ # - Konsole (linux avec KDE)
#⠀⠀⠀⢠⡿⠁⣼⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣆⠘⢿⡄⠀⠀ # - Gnome Terminal (linux avec Gnome)
#⠀⠀⣠⡟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠈⢿⡄⠀ # - Windows Terminal (windows 10 et 11)
#⠀⢰⡿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣿⡄ # - Terminal (MacOS)
#⠀⢼⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢸⡇ # - Terminal de VSCode (Linux, pas testé sur Windows et MacOS)
#⠀⠘⣷⣄⠙⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⣠⡿⠃⠀ #
#⠀⠀⠈⠉⠛⠓⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠛⠛⠉⠀⠀⠀ #

# ╔══════════════════════════════╗
# ║ Documentation                ║
# ╚══════════════════════════════╝
# 
# Caractères unicode utilisés pour l'affichage du plateau de jeu et des pions :
#   - https://www.compart.com/fr/unicode/block/U+2500
#   - https://www.compart.com/fr/unicode/block/U+25A0
# 
# Ansi Escape Sequences :
#   - https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# 
# Typage en python :
#   - https://typing.python.org/
#   - https://docs.python.org/3/library/typing.html#annotating-callable-objects
# 
# get_terminal_size :
#   - https://docs.python.org/3/library/os.html#os.get_terminal_size

from typing import Callable # Permet de typer les fonctions prenant une fonction en paramètre
from os import get_terminal_size # Permet de récupérer la taille du terminal pour être certain que l'affichage soit correct

# ╔══════════════════════════════╗
# ║ Affichage                    ║
# ╚══════════════════════════════╝
# 
# Comme dit précédemment, l'affichage du plateau se fait via des caractères unicode et des ansi escape sequences.
# Cette méthode permet un affichage plus propre et plus élégant, permettant un jeu plus agréable.

def affiche_plateau(taille:int) -> None:
    """
        Affiche un plateau de jeu vide

        Parameters:
        -----------
        taille: int
            La taille du plateau de jeu
    """

    print(f"\033[0;0H\033[K", end="") # Efface la ligne du joueur courant si elle existe.

    ligne_haut   = "┌" + "───┬" * (taille - 1) + "───" + "┐"
    ligne_vide   = "│" + "   │" * (taille - 1) + "   " + "│"
    ligne_milieu = "├" + "───┼" * (taille - 1) + "───" + "┤"
    ligne_bas    = "└" + "───┴" * (taille - 1) + "───" + "┘"

    print("\n  " + ligne_haut) # Bordure du haut du plateau

    for i in range(taille):
        print(chr(i + 65) + " ", end="") # Indice des lignes. `chr(i + 65)` donne la lettre majuscule correspondant à l'indice `i`
        print(ligne_vide) # Ligne de cases
        
        if i < taille - 1:
            print("  " + ligne_milieu) # Séparateurs de lignes
        else :
            print("  " + ligne_bas) # Bordure du bas du plateau

    print(" ", end="")
    for i in range(taille): # Indice des colonnes
        print("   " + str(i + 1), end="")
    
def affiche_case(y:int, x:int, valeur:int) -> None:
    """
        Affiche le contenu d'une case

        Parameters:
        -----------
        y: int
            L'indice de la colonne de la case
        x: int
            L'indice de la ligne de la case
        valeur: int
            La valeur de la case (0 pour vide, 1 pour pion blanc, 2 pour pion noir)
    """

    print(f"\033[{2*y+3};{4*x+5}H", end="") # Positionne le curseur à la case (x, y)

    match valeur: # Affiche le contenu de la case en distinguant les cas "case vide", "pion blanc" et "pion noir"
        case 0: # Case vide
            print(" ", end="")

        case 1: # Pion blanc
            print("○", end="")

        case 2: # Pion noir
            print("●", end="")

def affiche_cimetiere(pions_blancs:int, pions_noirs:int, taille:int) -> None:
    """
        Affiche les pions pris par chaque joueur

        Parameters:
        -----------
        pions_blancs: int
            Le nombre de pions blancs pris
        pions_noirs: int
            Le nombre de pions noirs pris
        taille: int
            La taille du plateau de jeu, permet de positionner le curseur à droite du plateau
    """

    ligne = 3 # Position de la première ligne des pions pris
    colonne = 6+4*taille # Position de la ligne des pions pris
    
    for i in range(pions_blancs):
        incr_ligne = i%(taille*2-1)
        incr_colonne = 2*(i//(taille*2-1))
        print(f"\033[{ligne+incr_ligne};{colonne+incr_colonne}H", end="") # Positionne le curseur à la position du pion blanc pris
        print("○", end="") # Affiche le pion blanc pris

    colonne += (taille // 2) # Le cimetière blanc ne peut pas être plus grand que la moitié du plateau

    for i in range(pions_noirs):
        incr_ligne = i%(taille*2-1)
        incr_colonne = 2*(i//(taille*2-1))
        print(f"\033[{ligne+incr_ligne};{colonne+2+incr_colonne}H", end="")
        print("●", end="")

def affiche_joueur_courant(joueur:int, taille:int) -> None:
    """
        Affiche le joueur courant

        Parameters:
        -----------
        joueur: int
            Le joueur courant
        taille: int
            La taille du plateau de jeu, permet de positionner le curseur à droite du plateau
    """

    print(f"\033[0;0H", end="") # Positionne le curseur à la position du joueur courant

    match joueur: # Affiche le joueur courant
        case 0:
            print("", end="")
        case 1:
            print("Joueur 1 (○)", end="")

        case 2:
            print("Joueur 2 (●)", end="")

def affiche_grille(configuration:tuple[list[list[int]], int, int, int]) -> None:
    """
        Affiche une configuration de jeu
        
        Parameters:
        -----------
        configuration: tuple[list[list[int]], int, int, int]
            Une configuration de jeu:
            - une matrice (liste de liste) représentant le plateau de jeu
            - un entier représentant le joueur courant
            - un entier représentant le nombre de pions blancs pris
            - un entier représentant le nombre de pions noirs pris
    """

    plateau, joueur_courant, pions_blancs_pris, pions_noirs_pris = configuration

    print("\033[2J\033[H", end="") # Efface le terminal et positionne le curseur en haut
    affiche_plateau(len(plateau)) # Affiche le plateau de jeu

    for i in range(len(plateau)):
        ligne = plateau[i] # Pour chaque ligne

        for j in range(len(ligne)):
            case = ligne[j] # Pour chaque case

            affiche_case(i, j, case) # Affiche le contenu de la case à la position (i, j)
    
    affiche_cimetiere(pions_blancs_pris, pions_noirs_pris, len(plateau)) # Affiche les pions pris
    affiche_joueur_courant(joueur_courant, len(plateau)) # Affiche le joueur

# ╔══════════════════════════════╗
# ║ Saisie                       ║
# ╚══════════════════════════════╝
# 
# Il a été choisi de considérer les coordonnées sur plusieurs caractères, en base 26 pour les lignes et en base 10 pour les colonnes.
# Il aurait été possible de considérer les coordonnées sur seulement deux caractères, mais ça rendrait impossible de jouer sur une grille de plus de 26 et 10 colonnes.
# 
# Exemples:
# ---------
#   - BAX291 représente la case (699, 290)
#   - A1     représente la case (0, 0)
#   - D8     représente la case (3, 7)
#   - G6     représente la case (6, 6)
#
# Il a été choisi que la fonction de saisie des coordonnées prenne une fonction `input` en paramètre.
# Cela permet de tester la fonction de saisie en simulant des saisies de l'utilisateur.
# Cela permet également de passer une fonction de saisie différente pour implémenter une IA par exemple.

def est_au_bon_format(coord:str) -> bool:
    """
        Vérifie si une chaîne de caractères est au bon format

        Parameters:
        -----------
        coord: str
            La chaîne de caractères à vérifier

        Returns:
        --------
        bool
            True si la chaîne de caractères est au bon format, False sinon
    """

    if not coord:  # Vérifie que la chaîne n'est pas vide
        return False

    i = 0
    while i < len(coord) and coord[i].isalpha(): # Récupère la partie lettre
        i += 1

    if i == 0 or i == len(coord): # Il faut au moins une lettre et un chiffre
        return False

    return coord[i:].isdigit() # Vérifie que le reste est un nombre


def est_dans_grille(y:int, x:int, plateau:list[list[int]]) -> bool:
    """
        Vérifie si une case est dans la grille

        Parameters:
        -----------
        y: int
            L'indice de la colonne de la case
        x: int
            L'indice de la ligne de la case
        plateau: list[list[int]]
            Le plateau de jeu

        Returns:
        --------
        bool
            True si la case est dans la grille, False sinon
    """

    if not plateau: # Vérifie si la grille est vide
        return False

    taille = len(plateau)

    if not 0 <= y < taille: # Vérifie si l'indice de la colonne est dans la grille
        return False
    
    if not 0 <= x < taille: # Vérifie si l'indice de la ligne
        return False
    
    return True

def convertir_coordonnees(entry:str) -> tuple[int, int]:
    """
        Convertit des coordonnées en indices de case

        Parameters:
        -----------
        entry: str
            Les coordonnées de la case

        Returns:
        --------
        tuple[int, int]
            Les coordonnées de la case
    """

    entry = entry.upper() # Convertit la chaîne en majuscules
    y = 0
    i = 0

    while i < len(entry) and entry[i].isalpha(): # Récupère la partie lettre en la considérant en base 26
        y *= 26
        y += ord(entry[i]) - 65 # Convertit la lettre en nombre
        i += 1

    x = int(entry[i:]) - 1 # Récupère la partie chiffre

    return y, x

def saisir_coordonnees(plateau:list[list[int]], input:Callable[[str], str]) -> tuple[int, int]:
    """
        Saisie des coordonnées d'une case par une méthode d'entrée.

        Parameters:
        -----------
        plateau: list[list[int]]
            Le plateau de jeu

        input: Callable[[str], str]
            La méthode d'entrée

        Returns:
        --------
        tuple[int, int]
            Les coordonnées de la case
    """

    print("\033[?25h") # Affiche le curseur

    while True: # Continue jusqu'à ce que les coordonnées soient valides
        print(f"\033[{2*len(plateau)+4};1H\033[K > ", end="") # Positionne le curseur en bas du plateau et efface la ligne de saisie
        coord = input()

        if not est_au_bon_format(coord):
            continue # Recommence la boucle si les coordonnées ne sont pas au bon format
        
        y, x = convertir_coordonnees(coord)

        if not est_dans_grille(y, x, plateau):
            continue

        break # Sort de la boucle si les coordonnées sont valides

    print("\033[?25l") # Cache le curseur

    return y, x

# ╔══════════════════════════════╗
# ║ Tests                        ║
# ╚══════════════════════════════╝
# 
# Les tests pour la fonction `convertir_coordonnees` n'étaient pas explicitement demandés,
# mais il est nécessaire de les faire pour tester le bon fonctionnement de la fonction.

def test_est_au_bon_format() -> None:
    """
        Teste la fonction est_au_bon_format
    """

    # Cas général
    assert est_au_bon_format("A1")     , "cas général : Coordonnée A1 = (0, 0)"
    assert est_au_bon_format("b2")     , "cas général : Coordonnée B2 = (1, 1)"
    assert est_au_bon_format("C3")     , "cas général : Coordonnée C3 = (2, 2)"
    assert est_au_bon_format("d8")     , "cas général : Coordonnée D8 = (3, 7)"
    assert est_au_bon_format("H7")     , "cas général : Coordonnée H7 = (7, 6)"

    # Cas particulier
    assert est_au_bon_format("X22")    , "cas particulier :  Coordonnée X22 = (23, 21)"  # Numéro de ligne élevé
    assert est_au_bon_format("BA1")    , "cas particulier :  Coordonnée AB1 = (26, 0)"  # Double lettre pour la colonne

    # Cas d'erreur
    assert not est_au_bon_format("A")  , "cas d'erreur : Il manque la colonne"
    assert not est_au_bon_format("11") , "cas d'erreur : Il manque la ligne"
    assert not est_au_bon_format("1A") , "cas d'erreur : La ligne doit être avant la colonne"
    assert not est_au_bon_format("")   , "cas d'erreur : La chaîne est vide"
    assert not est_au_bon_format("..."), "cas d'erreur : La chaîne contient des caractères non autorisés"

def test_est_dans_grille() -> None:
    """
        Teste la fonction est_dans_grille
    """

    # Cas général
    assert est_dans_grille(0, 0, [[0, 0], [0, 0]])    , "cas général : La case (0, 0) est dans la grille"
    assert est_dans_grille(1, 1, [[0, 0], [0, 0]])    , "cas général : La case (1, 1) est dans la grille"
    assert est_dans_grille(0, 1, [[0, 0], [0, 0]])    , "cas général : La case (0, 1) est dans la grille"
    assert est_dans_grille(1, 0, [[0, 0], [0, 0]])    , "cas général : La case (1, 0) est dans la grille"

    # Cas particulier
    assert est_dans_grille(0, 0, [[0]])               , "cas particulier : La case (0, 0) est dans la grille"

    # Cas d'erreur
    assert not est_dans_grille(0, 0, [])              , "cas d'erreur : La grille est vide"
    assert not est_dans_grille(2, 2, [[0, 0], [0, 0]]), "cas d'erreur : La case (2, 2) n'est pas dans la grille"

def test_convertir_coordonnees() -> None:
    """
        Teste la fonction convertir_coordonnees
    """

    # Cas général
    assert convertir_coordonnees("A1") == (0, 0)     , "cas général : Coordonnée A1 = (0, 0)"
    assert convertir_coordonnees("b2") == (1, 1)     , "cas général : Coordonnée B2 = (1, 1)"
    assert convertir_coordonnees("C3") == (2, 2)     , "cas général : Coordonnée C3 = (2, 2)"
    assert convertir_coordonnees("d8") == (3, 7)     , "cas général : Coordonnée D8 = (3, 7)"

    # Cas particulier
    assert convertir_coordonnees("X22") == (23, 21)  , "cas particulier : Coordonnée X22 = (23, 21)"
    assert convertir_coordonnees("BA1") == (26, 0)   , "cas particulier : Coordonnée AB1 = (26, 0)"
    assert convertir_coordonnees("XX22") == (621, 21), "cas général : Coordonnée XX22 = (621, 21)"

def test() -> None:
    """
        Fonction de test générale
    """

    test_est_au_bon_format()
    test_est_dans_grille()
    test_convertir_coordonnees()

# ╔══════════════════════════════╗
# ║ Configuration de jeu         ║
# ╚══════════════════════════════╝
# 
# Une configuration de jeu est représentée par un tuple de 4 éléments :
#  - une matrice (liste de liste) représentant le plateau de jeu
#  - un entier représentant le joueur courant
#  - un entier représentant le nombre de pions blancs pris
#  - un entier représentant le nombre de pions noirs pris
# 
# À noter qu'il n'est techniquement pas nécessaire de stocker le nombre de pions pris,
# car il est possible de le calculer à partir de la configuration du plateau.
# Cependant, cela permet d'optimiser certaines fonctions en évitant de recalculer ce nombre,
# et surtout, cela permet de simplifier l'écriture de certaines fonctions.
# 
# Les valeurs des cases sont représentées par des entiers :
#  - 0 pour une case vide, représentée par ' '
#  - 1 pour une case contenant un pion blanc, représentée par '○'
#  - 2 pour une case contenant un p, représentée par '●'
#
# Logiquement, le joueur 1 est le joueur blanc et le joueur 2 est le joueur noir.

configuration_depart = ([
    [1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2, 2],
    [1, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 0, 2, 2, 2],
    [1, 1, 1, 2, 2, 2, 2],
    [1, 1, 2, 2, 2, 2, 2],
    [1, 2, 2, 2, 2, 2, 2],
], 1, 0, 0)

configuration_interm = ([
    [1, 1, 0, 1, 1, 1, 2],
    [1, 0, 1, 0, 2, 2, 2],
    [0, 1, 1, 1, 1, 2, 2],
    [1, 0, 0, 0, 0, 2, 2],
    [1, 1, 0, 0, 0, 2, 2],
    [1, 0, 2, 2, 0, 0, 2],
    [1, 2, 2, 2, 2, 2, 2],
], 2, 8, 5)

configuration_finale = ([
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
], 2, 20, 20)

configuration_vide = ([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
], 0, 0, 0)

if __name__ == "__main__": # Permet d'exécuter le code suivant seulement si le fichier est exécuté et pas importé. Permet d'éviter des problèmes de double exécution

    #┌────────────────────────────────┐
    #│ Initialisation                 │
    #└────────────────────────────────┘

    if get_terminal_size().lines < 20 or get_terminal_size().columns < 80:
        print("La taille du terminal est trop petite pour afficher le plateau de jeu correctement.")
        exit(1)

    print("\033[?1049h\033[?25l", end="") # Active le mode "alternate screen" et masque le curseur

    #┌────────────────────────────────┐
    #│ Affiche les configurations     │
    #└────────────────────────────────┘

    affiche_grille(configuration_depart)
    input(f"\033[{2*7+4};1H\033[KPremière configuration. Appuyez sur entrée pour continuer.")
    affiche_grille(configuration_interm)
    input(f"\033[{2*7+4};1H\033[KDeuxième configuration. Appuyez sur entrée pour continuer.")
    affiche_grille(configuration_finale)
    input(f"\033[{2*7+4};1H\033[KTroisième configuration. Appuyez sur entrée pour continuer.")

    #┌────────────────────────────────┐
    #│ Saisie des coordonnées         │
    #└────────────────────────────────┘

    affiche_grille(configuration_vide) # Efface la configuration précédemment affichée. N'est pas nécessaire, mais permet de garder le terminal propre

    y, x = saisir_coordonnees(configuration_depart[0], input) # Demande des coordonnées à l'utilisateur
    input(f"\033[{2*7+4};1H\033[KCoordonnées saisies : ({y}, {x}). Appuyez sur entrée pour continuer.")

    #┌────────────────────────────────┐
    #│ Jeux de tests                  │
    #└────────────────────────────────┘

    test() # Test

    input(f"\033[{2*7+4};1H\033[KTests passés. Appuyez sur entrée pour continuer.")

    #┌────────────────────────────────┐
    #│ Nettoyage                      │
    #└────────────────────────────────┘

    print("\033[?1049l\033[?25h") # Désactive le mode "alternate screen" et réaffiche le curseur