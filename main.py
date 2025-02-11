from controler.Game import Game
from entity.Pawn import Pawn
from boundary.View import View
from controler.AutoPlayer import AutoPlayer
from controler.Menu import Menu
from controler.Markdown import Markdown

if __name__ == "__main__" :
    Menu = Menu(Game(5))
    print(Markdown.generate(Menu.get_rules()))