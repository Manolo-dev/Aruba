# Aruba

Ce projet est un jeu de plateau simple, inspiré du jeu de dames, développé en Python. Il a été réalisé dans le cadre du cours de info1.projet à l'Université de Toulouse (anciennement Université Toulouse III - Paul Sabatier).

## Structure du projet

Le projet est organisé selon le modèle ECB (Entity-Control-Boundary). L'architecture du projet est la suivante :

```
Aruba/
├── main.py
├── entity/
│   ├── Board.py
│   ├── Pawn.py
│   └── Move.py
├── controler/
│   ├── Markdown.py
│   ├── AutoPlayer.py
│   ├── autoplayer/
│   │   ├── RandomIA.py
│   │   └── HeuristIA.py
│   └── Game.py
└── boundary/
    └── View.py
```

**Entity (E) :** Définit les éléments du jeu (plateau, pions, déplacements).

**Control (C) :** Gère la logique du jeu.

**Boundary (B) :** Gère l'affichage et l'interaction avec l'utilisateur.

## Fonctionnalités

- Jeu au tour par tour entre deux joueurs.
- Affichage du plateau en ASCII avec des bordures et des coordonnées.
- Déplacement des pions sur le plateau.
- Prise de pions adverses.
- Configuration standard du jeu
- Affichage des règles du jeu en Markdown dans le terminal.
- Possibilité de jouer contre différentes IA :
  - **RandomIA** : Joue un coup aléatoire.
  - **HeuristIA** : Joue un coup en fonction d'une heuristique.

## Configuration du jeu

Le plateau est une grille carrée de $n\times n$ remplie selon le schéma suivant :
- La moitié supérieure gauche (excluant la diagonale centrale) est remplie de pions noirs.
- La moitié inférieure droite (excluant la diagonale centrale) est remplie de pions blancs.
- La diagonale centrale est divisée en deux parties :
    - Une partie avec des pions blancs.
    - Une autre partie avec des pions noirs.
    - Une ou deux cases peuvent rester vides, selon que $n$ est pair ou impair.

## Installation et exécution

Assurez-vous d'avoir Python installé sur votre machine.

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
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Dorection artistique
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Responsable documentation
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Responsable test
- [Manolo SARDÓ](https://github.com/Manolo-dev) : Développeur