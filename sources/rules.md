# Règles du Jeu

## Objectif

L'objectif du jeu est de capturer les pions adverses.

## Matériel

- Un plateau de jeu de taille $n\cdot n$ définie.
- Deux ensembles de pions (Noirs et Blancs).
- Un joueur automate.

## Déroulement du Jeu

1. Chaque joueur joue à tour de rôle.
2. Un joueur peut déplacer un de ses pions selon les règles de mouvement.
3. Si un pion atteint une position spécifique, il peut être promu.
4. Un joueur peut passer son tour en entrant `pass`.
5. Un joueur peut quitter la partie en entrant `exit`, `quit` ou `q`.

## Règles de Mouvement

- Les pions se déplacent sur des cases adjacentes.
- Certains pions peuvent capturer les pions adverses.
- Les mouvements doivent être saisis sous la forme `x1y1x2y2`, où `x1y1` est la position initiale et `x2y2` la destination.
- Les lettres désignent les colonnes (A, B, C, ...), et les chiffres désignent les lignes (1, 2, 3, ...).

## Conditions de Victoire

- Un joueur gagne s'il capture tous les pions adverses.
- Un joueur gagne s'il atteint une position spécifique sur le plateau avec un pion désigné.
- La partie peut se terminer par un match nul si aucun joueur ne peut jouer.

## Cas Particuliers

- Si un joueur saisit une commande incorrecte, il doit recommencer.
- Les coups doivent respecter les limites du plateau.
- Les pions ne peuvent pas se superposer.