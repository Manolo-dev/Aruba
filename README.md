# Aruba

Ce projet est un jeu de plateau simple, inspiré du jeu de dames, développé en Python. Il a été réalisé *à tort* dans le cadre du cours de info1.projet à l'Université de Toulouse (anciennement Université Toulouse III - Paul Sabatier).

## Structure du projet

Le projet est organisé selon le modèle ECB (Entity-Control-Boundary). L'architecture du projet est la suivante :

```
Aruba/
├── main.py
├── entity/
│   └── Board.py
├── controler/
│   ├── Game.py
│   ├── Menu.py
│   ├── AutoPlayer.py
│   ├── autoplayer/
│   │   ├── RandomIA.py
│   │   ├── HumanIA.py
│   │   └── HeuristIA.py
│   └── Markdown.py
├── boundary/
│   ├── MenuView.py
│   ├── View.py
│   └── Keyboard.py
├── utils/
│   ├── terminal.py
│   ├── Pawn.py
│   └── Move.py
└── sources/
    └── rules.md
```

**Entity (E) :** Définit les éléments du jeu (plateau, pions, déplacements).

**Control (C) :** Gère la logique du jeu.

**Boundary (B) :** Gère l'affichage et l'interaction avec l'utilisateur.

**Utils :** Contient des classes utilitaires, principalement des enums.

**Sources :** Contient les fichiers non exécutables du projet.

## Fonctionnalités

- Jeu au tour par tour entre deux joueurs.
- Affichage d'un menu de jeu interactif.
- Affichage du plateau avec des bordures et des coordonnées.
- Déplacement des pions sur le plateau.
- Prise de pions adverses.
- Configuration standard du jeu.
- Affichage des règles du jeu en Markdown dans le terminal.
- Possibilité de jouer contre différentes IA :
  - **HumanIA**  : N'est pas une IA, mais une interface pour un joueur humain.
  - **RandomIA** : Joue un coup aléatoire.
  - **HeuristIA** : Joue un coup en fonction d'une heuristique.

## Configuration du jeu

Le plateau est une grille carrée de $n\times n$ remplie selon le schéma suivant :
- La moitié supérieure gauche (excluant la diagonale centrale) est remplie de pions bleus.
- La moitié inférieure droite (excluant la diagonale centrale) est remplie de pions rouges.
- La diagonale centrale est divisée en deux parties :
    - Une partie avec des pions rouges.
    - Une autre partie avec des pions bleus.
    - Une ou deux cases peuvent rester vides, selon que $n$ est pair ou impair.

## HeuristIA

Basé sur un algorithme Minimax, et une heuristique simple. L'heuristique est basée sur les critères suivants :

- Prioriser les captures
- Maximiser les captures enchaînées
- Minimiser les options adverses

Pour évaluer un coup, on va le simuler et évaluer le plateau obtenu. On va alors attribuer un score au coup en fonction de l'heuristique.

### Prioriser les captures

Si après simulation d'une prise c'est toujours au tour de l'IA, on ajoute $10$ point au score.

### Maximiser les captures enchaînées

Si après simulation d'une prise c'est toujours au tour de l'IA, on ajouter au score le score de la capture enchaînée.

Les scores ainsi obtenus sont conséquents, par effet cumulatif de la récursivité.

### Minimiser les options adverses

Après simulation d'un coup, on enlève $3$ points par prise possible par l'adversaire et $1$ point par déplacement possible.

## Menu

Le menu est interactif et permet de choisir entre les différentes options suivantes :

- **Jouer** : Permet de jouer une partie contre une IA ou un autre joueur.
- **Règles** : Affiche les règles du jeu.
- **Quitter** : Permet de quitter le jeu.

### Jouer

Le sous-menu de jeu permet de choisir entre les différentes options suivantes :

- **Jouer à deux** : Permet de jouer une partie contre un autre joueur.
- **IA** : La liste des IA disponibles est affichée, et l'utilisateur peut en choisir une pour jouer contre.

## Installation et exécution

Assurez-vous d'avoir Python `>3.9` installé sur votre machine.

Seuls Linux et Microsoft Windows sont supportés. Possiblement MacOS mais non testé.

un terminal compatible avec les séquences d'échappement ANSI est nécessaire pour un affichage correct (ex: Gnome Terminal, Konsole, Windows Terminal).

Pour installer le projet, il suffit de cloner le dépôt git.

```bash
git clone https://github.com/Manolo-dev/Aruba/
cd Aruba
```

Pour lancer le jeu, il suffit de lancer le fichier main.py depuis la racine.

```bash
python main.py
```

ou

```bash
python3 main.py
```

## Documentation

- Utilisation des **séquences d'échappement ANSI** pour le rendu visuel :
  - [Documentation ANSI](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)
- Utilisation des **caractères spéciaux Unicode** pour l'affichage :
  - [Liste des caractères du plateau](https://www.compart.com/fr/unicode/block/U+2500)
  - [Liste des caractères d'indices](https://www.compart.com/fr/unicode/block/U+2070)
  - [Caractère de pion](https://www.compart.com/fr/unicode/U+25CF)
- [Liste par compréhension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [ternary operator](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

## Auteurs

- [Manolo SARDÓ](https://github.com/Manolo-dev) : Chef de projet
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Direction artistique
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Responsable documentation
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Responsable test
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Développeur