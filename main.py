from controler.Game import Game
from controler.autoplayer.RandomIA import RandomIA
from controler.Menu import Menu
from boundary.MenuView import MenuView

if __name__ == "__main__" :
    game = Game(7)
    randomIA = RandomIA(game)
    menu = Menu(game, [randomIA])
    menuview = MenuView(menu)

    menuview.start()

    menuview.end()