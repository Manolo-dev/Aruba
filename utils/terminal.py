import os

def clear() -> None :
    """
    Efface l'écran selon le système d'exploitation.
    """

    if os.name == "nt":
        os.system("cls")  # Efface l'écran sous Windows
    else:
        os.system("clear")  # Efface l'écran sous Linux

def height() -> int :
    """
    Récupère la hauteur du terminal.
    """
    
    return os.get_terminal_size().lines # Récupère la hauteur du terminal

def width() -> int :
    """
    Récupère la largeur du terminal.
    """
    
    return os.get_terminal_size().columns # Récupère la largeur du terminal

def wrap(lines:list[str], n:int) -> list[str]:
    """
    Fais des sauts de ligne pour que chaque ligne ne dépasse pas n caractères.

    Parameters:
    -----------
    lines : list[str]
        Liste des lignes à découper.
    n : int
        Taille maximale des lignes.

    Returns:
    --------
    list[str]
        Liste des lignes découpées.
    """
    
    wrapped_lines = []
    
    for line in lines:
        while len(line) > n:
            wrapped_lines.append(line[:n])  # Ajoute un morceau de la taille max
            line = line[n:]  # Reste de la ligne
        wrapped_lines.append(line)  # Ajoute le reste de la ligne (même si vide)
    
    return wrapped_lines
