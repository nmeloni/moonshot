################################################################################################  
#  _______                 __  __        _          _   _            __  __                   
# |__   __|               |  \/  |      | |        | | | |          |  \/  |                  
#    | |_   _ _ __   ___  | \  / | ___  | |_ ___   | |_| |__   ___  | \  / | ___   ___  _ __  
#    | | | | | '_ \ / _ \ | |\/| |/ _ \ | __/ _ \  | __| '_ \ / _ \ | |\/| |/ _ \ / _ \| '_ \ 
#    | | |_| | |_) |  __/ | |  | |  __/ | || (_) | | |_| | | |  __/ | |  | | (_) | (_) | | | |
#    |_|\__, | .__/ \___| |_|  |_|\___|  \__\___/   \__|_| |_|\___| |_|  |_|\___/ \___/|_| |_|
#        __/ | |                                                                              
#       |___/|_|                                                                               
#
################################################################################################ 

################################################################
#                                                              
# tmttm.py
# -----------
#
# date:   november 2020
# author: Nicolas Méloni
#         Toulon, France
# source: https://github.com/nmeloni
#                                                              
################################################################

################################################################
# 
# Type Me To The Moon is a typing shmup developed for the
# Github/itch.io game jam of november 2020 and a
# first attempt at game programming.
#
# Theme : MOONSHOT
# Pitch : The moon is collapsing and threatens the earth.
#         Use your more poetic instincts to type your way
#         through the meteors and save humanity !
################################################################

import pyxel
from classes.word import *
from classes.animation import *
from classes.rock import *
from classes.title import *
from classes.sprite import *
from classes.fallingObject import *
from classes.game import *
from classes.explosion import *
from classes.intro import *

SCREEN_WIDTH  = 256
SCREEN_HEIGHT = 256

APP_INTRO        = 0
APP_TITLE_SCREEN = 1
APP_GAME         = 2

class App():
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, caption="--- TYPE-ME-TO-THE-MOON ---")
        pyxel.load("assets/tmttm.pyxres")
        self.state = APP_INTRO
        self.intro = Intro()
        self.title = TitleScreen()
        self.game = Game()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.state == APP_INTRO:
            self.intro.update()
            if self.intro.state == DONE:
                self.state = APP_TITLE_SCREEN
                self.title.__init__()
        elif self.state == APP_TITLE_SCREEN:
            self.title.update()
            if self.title.state == PLAY:
                self.game.__init__()
                self.state = APP_GAME
        elif self.state == APP_GAME:
            self.game.update()
            if self.game.state == GAME_DONE:
                self.state = APP_INTRO
                self.intro.__init__()

    def draw(self):
        pyxel.cls(0)
        if self.state == APP_INTRO:
            self.intro.draw()
        elif self.state == APP_TITLE_SCREEN:
            self.title.draw()
        elif self.state == APP_GAME:
            self.game.draw()

        
        
        
if __name__=="__main__":
    App()
