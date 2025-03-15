# Règles du Jeu

## Objectif

L'objectif du jeu est de capturer tous les pions adverses.

## Matériel

- Un plateau de jeu de taille $n\cdot n$ (par default $7\cdot 7$).
- Deux ensembles de pions : bleus et rouges (Pour les distinguer facilement dans le terminal).
- Un joueur automate ou un autre joueur.

## Disposition des Pions

Le plateau est une grille carrée de $n\cdot n$ remplie selon le schéma suivant :
- La moitié supérieure gauche (excluant la diagonale centrale) est remplie de pions bleus.
- La moitié inférieure droite (excluant la diagonale centrale) est remplie de pions rouges.
- La diagonale centrale est divisée en deux parties :
    - Une partie avec des pions rouges.
    - Une autre partie avec des pions bleus.
    - Une ou deux cases peuvent rester vides, selon que $n$ est pair ou impair.

### Exemple de Disposition

Dans un plateau $7\cdot 7$ (les pions bleus sont représentés par `●` et les pions rouges par `○`):

```
  ┌───┬───┬───┬───┬───┬───┬───┐
1 │ ● │ ● │ ● │ ● │ ● │ ● │ ● │
  ├───┼───┼───┼───┼───┼───┼───┤
2 │ ● │ ● │ ● │ ● │ ● │ ● │ ○ │
  ├───┼───┼───┼───┼───┼───┼───┤
3 │ ● │ ● │ ● │ ● │ ● │ ○ │ ○ │
  ├───┼───┼───┼───┼───┼───┼───┤
4 │ ● │ ● │ ● │   │ ○ │ ○ │ ○ │
  ├───┼───┼───┼───┼───┼───┼───┤
5 │ ● │ ● │ ● │ ○ │ ○ │ ○ │ ○ │
  ├───┼───┼───┼───┼───┼───┼───┤
6 │ ● │ ● │ ○ │ ○ │ ○ │ ○ │ ○ │
  ├───┼───┼───┼───┼───┼───┼───┤
7 │ ● │ ○ │ ○ │ ○ │ ○ │ ○ │ ○ │
  └───┴───┴───┴───┴───┴───┴───┘
    A   B   C   D   E   F   G
```

## Déroulement du Jeu

1. Chaque joueur joue à tour de rôle.
2. Un joueur peut déplacer un de ses pions selon les **règles de mouvement**.
4. Un joueur peut passer son tour en entrant `pass`, ou en appuyant sur `Enter`.
5. Un joueur peut quitter la partie en entrant `exit`, `quit` ou `q`. Un match nul est déclaré.

## Règles de Mouvement

- Les pions se déplacent sur des cases adjacentes.
- Les pions peuvent capturer les pions adverses en sautant par-dessus eux sur la case vide suivante.
- La capture n'est pas possible si la case suivante n'est pas vide, c'est un  **cas particulier** de superposition.
- Si un pion vient de capturer un pion adverse, il peut continuer à capturer d'autres pions.
- Les mouvements doivent être saisis sous la forme $x_1y_1x_2y_2$, où $x_1y_1$ est la position initiale et $x_2y_2$ la destination.
- Les lettres désignent les colonnes (A, B, C, ...), et les chiffres désignent les lignes (1, 2, 3, ...).

## Conditions de Victoire

- Un joueur gagne s'il capture tous les pions adverses.
- La partie peut se terminer par un match nul si un joueur quitte la partie. Personne ne gagne mais le joueur qui a quitté gagne le titre de "lâche".

## Cas Particuliers

- Si un joueur saisit une commande incorrecte, il doit recommencer.
- Les coups doivent respecter les limites du plateau.
- Les pions ne peuvent pas se superposer.
- Les pions ne peuvent pas sauter par-dessus un pion de la même couleur.