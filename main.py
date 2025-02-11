from controler.Game import Game
from entity.Pawn import Pawn
from boundary.View import View
from controler.AutoPlayer import AutoPlayer

if __name__ == "__main__" :
    game = Game(5, [(0, 0, Pawn.BLACK), (1, 1, Pawn.WHITE)])
    auto = AutoPlayer(game)
    view = View(game, auto.input, input)
    view.play()
