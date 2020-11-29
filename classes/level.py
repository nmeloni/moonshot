import pyxel
from copy import deepcopy

from classes.strophe import *
from classes.objects import *
from classes.sprite import *
from classes.animation import *
from classes.rock import *
from classes.word import *
from classes.explosion import *
from classes.fallingObject import *

class Level:
    def __init__(self,data):
        self.load_data(data)
        self.fo_list = []
        self.strophe = None
        self.previous_strophe = None
        self.next_strophe()

    def load_data(self,data):
        self.poem = deepcopy(data["poem"])
        self.events = deepcopy(data["events"])

    def done(self):
        if self.poem == []:
            return self.strophe.done()
        return False
        
    def next_strophe(self):
        self.strophe = Strophe(48,24,self.poem.pop(0))
        self.objects = self.events.pop(0)
        self.timer = 0

    def next_event(self):
        pass
    
    def update(self):
        self.timer += 1
        if self.previous_strophe != None:
            if self.previous_strophe.done():
                self.previous_strophe = None
            else:
                self.previous_strophe.update()
        if self.strophe.get_state() == STR_COMPLETED:
            self.previous_strophe = self.strophe
            if self.poem:
                self.next_strophe()
            else:
                return
        self.strophe.update()
        if not self.objects:
            return
        if self.strophe.is_empty():
            return
        if self.timer >= self.objects[0][0]:
            self.timer = 0
            obj = self.objects.pop(0)
            if obj[1] == SIMPLE  \
               or obj[1]==MIRROR \
               or obj[1]==RANDOM \
               or obj[1]==SPLITS \
               or obj[1]==BONUS:
                w = self.strophe.pop_word()
                self.fo_list.append(make_SimpleFO(obj,w))
            elif obj[1]==METEOR:
                w = [self.strophe.pop_word() for i in range(3)]
                self.fo_list.append(make_MeteorFO(obj,w))

                
    def draw(self):
        if self.previous_strophe:
            self.previous_strophe.draw()
        self.strophe.draw()
