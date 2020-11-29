import pyxel
from classes.target import *
from classes.objects import *
from classes.input import Input
from classes.level import *
from classes.fallingObject import *
from classes.laser import *
from classes.background import *
from classes.score import *

GAME_OVER = 0
GAME_PLAY = 1
GAME_DONE = 2
GAME_END  = 3 

class Game:
    def __init__(self):
        self.keyboard = Input()
        self.background = Background()
        self.score = Score()
        self.levels = [lvl1,lvl2,lvl3]
        self.state = GAME_PLAY
        self.hp = 10
        self.lvl = 0
        self.load_level(self.lvl)
        
    def init_level(self):
        self.fo_list = []
        self.expl_list = []
        self.point_list = []
        self.laser_list = []
        self.target_list = []
        self.target = None       
        self.load_level_timer = 0
        
    def load_level(self,n):
        if n<len(self.levels):
            self.init_level()
            self.level = Level(self.levels[n])
    
    def update(self):
        if self.state == GAME_END:
            self.game_over_timer += 1
            if self.game_over_timer >= 20 and self.keyboard.get_input_list():
                self.state = GAME_DONE
            return
        if self.hp == 0:
            self.set_state(GAME_OVER)
            self.game_over_timer = 0
            self.hp = -1
        if self.state == GAME_OVER:
            self.game_over_timer +=1
            self.background.update()
            if self.game_over_timer >= 20 and self.keyboard.get_input_list():
                self.state = GAME_DONE
            return
        self.check_inputs()
        self.update_level()
        if self.level.done():
            self.lvl += 1
            if self.lvl == len(self.levels):
                self.state = GAME_END
                self.game_over_timer = 0
            else:
                self.load_level(self.lvl)
        self.update_fo()
        self.update_target()
        self.update_explosion()
        self.update_laser()
        self.update_point()
        self.background.update()
        
        
    def draw(self):
        self.background.draw()
        self.score.draw()
        self.level.draw()
        
        for obj in self.fo_list:
            obj.draw()
        for tgt in self.target_list:
            tgt.draw()
        for e in self.expl_list:
            e.draw()
        for l in self.laser_list:
            l.draw()
        for p in self.point_list:
            p.draw()

        if self.state == GAME_OVER:
            pyxel.text(110,128,"game over", pyxel.frame_count %16)
        if self.state == GAME_END:
            pyxel.text(90,128,"congratulations", pyxel.frame_count %16)
            pyxel.text(90,136,"you saved earth", pyxel.frame_count %16)
            pyxel.text(80,152,"thank you for playing", pyxel.frame_count %16)
        if 5<= self.load_level_timer < 60:
            pyxel.text(110,128,"level "+str(self.lvl+1), pyxel.frame_count %16)
            
    def next_target(self):
        if self.target != None:
            if self.target.get_state() != FO_FALLING:
                self.target = None
                self.target_list = []
                
        if self.target == None:
            for obj in self.fo_list:
                for key in self.inputs:
                    if obj.active_char() == key:
                        self.target = obj
                        return 

    def check_inputs(self):
        self.inputs = self.keyboard.get_input_list()
        if self.inputs:
            self.next_target()
            if self.target == None:
                self.miss()
            else:
                if self.target.active_char() in self.inputs:
                    self.hit()
                else:
                    self.miss()

    def set_state(self,state):
        self.state = state

    def get_state(self):
        return self.state
    
    def hit(self):
        self.target.hit()
        x,y = self.target.get_target()
        self.laser_list.append(LaserHit(x,y))
        self.score.hit_char()
        self.point_list.append(Point(x-4*len(str(self.score.point))//2,y-10,self.score.point))

    def miss(self):
        self.score.miss()
        if self.target == None:
            pass
        else:
            self.target.miss()
            self.target = None
        self.laser_list.append(LaserMiss(0,0))

    def fail(self,loss):
        self.hp = max(0, self.hp -loss)
        self.background.hit()
        self.background.set_hp(self.hp)

    def update_level(self):
        self.load_level_timer += 1
        self.level.update()
        while self.level.fo_list:
            self.fo_list.append(self.level.fo_list.pop(0))
            
    def update_fo(self):
        i=0
        destructions = []
        while i < len(self.fo_list):
            fo = self.fo_list[i]
            if fo.rock.y + fo.rock.sprite.h > 250:
                fo.set_state(FO_FAIL)
                if fo.rock.sprite.w <=8:
                    loss = 1
                elif fo.rock.sprite.w <=16:
                    loss = 2
                elif fo.rock.sprite.w <=32:
                    loss = 3
                elif fo.rock.sprite.w <=48:
                    loss = 4
                else:
                    loss = 10
                self.fail(loss)
                
            if fo.get_state() == FO_DESTROYED or\
               fo.get_state() == FO_FAIL:
                destructions.append(fo.destroy())  
                self.fo_list.pop(i)
            else:
                fo.update()
                i+=1
        for d in destructions:
            for e in d.explosions:
                self.expl_list.append(e)
            for fo in d.fos:
                self.fo_list.append(fo)

    def update_target(self):
        self.target_list = []
        if (self.target != None):
            if (self.target.get_state()!=FO_FALLING):
                self.target = None
                self.target_list = []
            else:
                x,y = self.target.get_target()
                w = min(16,self.target.rock.sprite.w)
                if w <=8:
                    sprite = small_target
                    x-=4
                    y-=4
                else:
                    sprite = target
                    x-=8
                    y-=8
                self.target_list = [Target(x, y,*sprite)]
        if self.target == None:
            ac= []
            self.fo_list=sorted(self.fo_list,key=lambda fo: -fo.y)
            for obj in self.fo_list:
                char = obj.active_char()
                if char!= None and ( not (char in ac) ):
                    ac.append(char)
                    x,y = obj.get_target()
                    w = min(16,obj.rock.sprite.w)
                    if w <=8:
                        sprite = small_target
                        x-=4
                        y-=4
                    else:
                        sprite = target
                        x-=8
                        y-=8
                    self.target_list.append(Target(x, y,*sprite))


                
    def update_explosion(self):
        i=0
        while i<len(self.expl_list):
            e = self.expl_list[i]
            if e.done():
                self.expl_list.pop(i)
            else:
                e.update()
                i+=1

    def update_laser(self):
        i=0
        while i<len(self.laser_list):
            l = self.laser_list[i]
            if l.done():
                self.laser_list.pop(i)
            else:
                l.update()
                i+=1
    def update_point(self):
        i=0
        while i<len(self.point_list):
            p = self.point_list[i]
            if p.done():
                self.point_list.pop(i)
            else:
                p.update()
                i+=1
       
    

        
            
