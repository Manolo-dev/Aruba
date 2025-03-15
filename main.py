#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controler.Game import Game
from controler.autoplayer.RandomIA import RandomIA
from controler.autoplayer.HeuristIA import HeuristIA
from controler.Menu import Menu
from boundary.MenuView import MenuView

if __name__ == "__main__" :
    game = Game(7)
    randomIA = RandomIA(game)
    heuristIA = HeuristIA(game)
    menu = Menu(game, [randomIA, heuristIA])
    menuview = MenuView(menu)

    menuview.start()

    menuview.end()