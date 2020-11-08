################################################################ 
#  ___ ___   ___    ___   ____   ______  __ __  ____     ___   #
# |   |   | /   \  /   \ |    \ |      ||  |  ||    \   /  _]  #
# | _   _ ||     ||     ||  _  ||      ||  |  ||  o  ) /  [_   #
# |  \_/  ||  O  ||  O  ||  |  ||_|  |_||  ~  ||   _/ |    _]  #
# |   |   ||     ||     ||  |  |  |  |  |___, ||  |   |   [_   #
# |   |   ||     ||     ||  |  |  |  |  |     ||  |   |     |  #
# |___|___| \___/  \___/ |__|__|  |__|  |____/ |__|   |_____|  #
#                                                              #
################################################################

################################################################
#                                                              #
# moontype.py
# -----------
#
# date:   november 2020
# author: Nicolas Méloni
#         Toulon, France
# source: https://github.com/nmeloni
#                                                              #
################################################################

################################################################
# 
# MOONTYPE is a typing shmup developed for the Github/itch.io
# game jam of november 2020 and a first attempt at game
# programming.
#
# Theme : MOONSHOT
# Pitch : The moon is collapsing and threatens the earth.
#         Use your more poetic instincts to type your way
#         through the meteors and save humanity !
################################################################

import pyxel
from random import randrange


MT_SCREEN_X = 256
MT_SCREEN_Y = 256

MT_PYXEL_KEY_OFFSET = pyxel.KEY_A 
MT_ASCII_KEY_OFFSET = ord("a")

MT_BULLET_SPEED = 5

POEME = ["la","nuit","je","mens","je","prends","des","trains","a","travers","la","pleine"]

class Text():
    """
    Text class:
    <x,y>: position of text
    <text>: text to be written
    """
    def __init__(self, x,y,text):
        self.x = x
        self.y = y
        self.text = text


    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def move_to(self,x,y):
        self.x = x
        self.y = y
        
class Rock():
    """
    Rock class:
    <x,y>: position of the rock
    <img,sx,sy,sw,sh>: first sprite coordinate
       <img> image bank (0,1 or 2)
       <sx,sy> top left coordinates
       <sw,sh> width and heigth 
    """
    def __init__(self, x, y, img, sx, sy, sw, sh):
        self.x = x
        self.y = y
        self.img=img
        self.sprite_x = sx
        self.sprite_y = sy
        self.sprite_w = sw
        self.sprite_h = sh
        self.sprite_current = 0 #current sprite to be drawn

    def move(self, dx,dy):
        self.x += dx
        self.y += dy
        
    def move_to(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.sprite_current = max(0, self.sprite_current-1)
        
class Meteor:
    """
    Meteor class
    basic falling object, made of a rock and a word
    <x,y>:position of the meteor
    <dx,dy>: fall vector, each component is a couple (nb_pixel, every_x_frame)
    <hp>: hit points
    <text>: a text class object
    <rock>: a rock class object
    """
    
    def __init__(self,x,y,dx,dy,hp,text,rock):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.hp = hp
        self.is_active = False
        self.active_letter = 0

        self.rock = rock
        self.rock.move_to(x,y)

        self.text = text
        self.text.move_to(x+(rock.sprite_w-len(text.text)*4)//2,y-6)
    
                

    def update(self):
        dx,dy = 0,0
        if pyxel.frame_count % self.dx[1] == 0:
            dx = self.dx[0]
        if pyxel.frame_count % self.dy[1] == 0:
            dy =  self.dy[0]
        self.x += dx
        self.y += dy
        self.text.move(dx,dy)
        self.rock.move(dx,dy)
            
        self.rock.update()
        
    def hit(self):
        self.rock.sprite_current = 4
        self.active_letter = (self.active_letter+1)% len(self.text.text)

    def is_destroyed(self):
        return self.hp <= 0

            
class App():
    """
    App class:
    game engine
    runs .update then .draw at every frame

    """
    def __init__(self):
        pyxel.init(MT_SCREEN_X,MT_SCREEN_Y, caption="--- MOON-TYPE --- ")
        pyxel.load("moontype.pyxres")

        self.game_speed = 40
        self.poem = POEME[::-1]
        self.meteor_l = []
        pyxel.run(self.update, self.draw)

    def new_meteor(self):
        if len(self.poem) == 0:
            return None
        word = self.poem.pop()
        x,y = randrange(10,240),0
        dx,dy = (0,1),(1,2)
        Txt = Text(0,0,word)
        Rck = Rock(0,0,1,0,24,16,16)
        return Meteor(x,y,dx,dy,len(word),Txt,Rck)
                
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if (pyxel.frame_count % self.game_speed) == 0:
            meteor = self.new_meteor()
            if meteor!= None:
                self.meteor_l.insert(0,meteor)
                
        if len(self.meteor_l) != 0:
            self.meteor_l[-1].is_active = True

        for meteor in self.meteor_l:
            meteor.update()
         
            
    def draw(self):
        pyxel.cls(0)
        for meteor in self.meteor_l:
            self.draw_meteor(meteor)
        
        
    def draw_rock(self, rock):
        frame = rock.sprite_current
        pyxel.blt(rock.x,rock.y,rock.img,rock.sprite_x+frame,rock.sprite_y,rock.sprite_w,rock.sprite_h,0)

    def draw_text(self, text, active_letter=-1, color=15,active_color=8):
        if active_letter == -1:
            pyxel.text(text.x,text.y,text.text,color)
        else:
            pyxel.text(text.x, text.y, text.text[0:active_letter],color)
            pyxel.text(text.x+active_letter*4, text.y-2, text.text[active_letter],active_color)
            pyxel.text(text.x+(active_letter+1)*4, text.y, text.text[active_letter+1:],15) 

    def draw_meteor(self,meteor):
        self.draw_rock(meteor.rock)
        if meteor.is_active:
            self.draw_text(meteor.text, meteor.active_letter)
        else:
            self.draw_text(meteor.text, -1)

                
if __name__=="__main__":
    App()


#class Bullet():
 #   def __init__(self,x,y,dx,dy,meteor):
 #       self.x = x
 #       self.y = y
 #       self.dx = dx
 #       self.dy = dy
 #       self.meteor = meteor

 #   def update(self):
 #       self.x += self.dx
 #       self.y += self.dy

 #   def hit(self):
 #       if abs(self.meteor.x+4-self.x) <= 8 and \
 #          abs(self.meteor.y+4-self.y) <= 8 :
 #           self.meteor.hp -= 1
 #           self.meteor.hit_frame = 4
 #           return True
 #       else:
 #           return False

 #   def destroy(self):
 #       return self.meteor.hp == 0

#class Explosion():
 #   def __init__(self,x,y):
 #       self.x = x
 #       self.y = y
 #       self.frame = 5
 #       
 #   def update(self):
 #       self.frame -= 1
 #   
#class App():
 #   def __init__(self):
 #       pyxel.init(MT_SCREEN_X,MT_SCREEN_Y, caption="--- MOONTYPE --- ")
 #       pyxel.load("moontype.pyxres")


 #       self.poem = POEME[::-1]
 #       self.meteor_list = [Meteor(randrange(16,240),0,self.poem.pop())]
 #       self.meteor_list[0].active = True

 #       self.bullet_list = []
 #       self.explosion_list = []
 #       
 #       pyxel.run(self.update, self.draw)

 #   def update(self):
 #       if pyxel.btnp(pyxel.KEY_ESCAPE):
 #           pyxel.quit()
 #       if (pyxel.frame_count % 60 == 0) and (len(self.poem)!=0):
 #           self.meteor_list.insert(0,Meteor(randrange(16,240),0,self.poem.pop()))
 #           
 #       for meteor in self.meteor_list:
 #           meteor.update()

 #       for explosion in self.explosion_list:
 #           explosion.update()

 #       while len(self.explosion_list) != 0 and self.explosion_list[-1].frame == 0:    
 #           self.explosion_list.pop()

 #       for bullet in self.bullet_list:
 #           bullet.update()
 #           if bullet.hit():
 #               print("hit")
 #               if bullet.destroy():
 #                   print("destroy")
 #                   self.explosion_list.insert(0,Explosion(bullet.meteor.x,bullet.meteor.y))
 #                   self.meteor_list.remove(bullet.meteor)
 #               self.bullet_list.remove(bullet)

 #       if len(self.meteor_list) != 0:
 #           for meteor in self.meteor_list[::-1]:
 #               if meteor.is_complete:
 #                   continue
 #               meteor.is_active = True
 #               letter = meteor.text[meteor.active_letter]
 #               # if the button corresponds to the active letter
 #               if pyxel.btn( ord(letter)-MT_ASCII_KEY_OFFSET+MT_PYXEL_KEY_OFFSET ):
 #                   # modify active letter
 #                   meteor.hit()
 #                   #compute direction and emit a bullet
 #                   x_B,y_B = MT_SCREEN_X//2,MT_SCREEN_Y
 #                   x_M,y_M = meteor.x+8, meteor.y+8
 #                   if x_M == x_B:
 #                       dx,dy = 0,4
 #                   else:
 #                       r = (y_M-y_B)/(x_M-x_B)
 #                       V_M = meteor.dy[0]/meteor.dy[1]
 #                       A,B,C = 1 + r*r, 2*r*V_M, V_M*V_M - MT_BULLET_SPEED*MT_BULLET_SPEED
 #                       beta = (B**2-4*A*C)**0.5
 #                       if (x_B-x_M) > 0:
 #                           dx = (-B - beta)/(2*A)
 #                       else:
 #                           dx = (-B + beta)/(2*A)
 #                       dy = (MT_BULLET_SPEED*MT_BULLET_SPEED - dx*dx)**0.5
 #                   bullet = Bullet(x_B,y_B,dx,-dy,meteor)
 #                   self.bullet_list.append(bullet)
 #               break
 #               

 #       
 #   def draw_meteor(self, meteor):
 #       
 #       if meteor.is_active:
 #           if meteor.is_complete:
 #                pyxel.text(meteor.text_x, meteor.y-7, meteor.text,pyxel.frame_count % 15 + 1)
 #           else:
 #               i = meteor.active_letter
 #               pyxel.text(meteor.text_x, meteor.y-5, meteor.text[0:i],15)
 #               pyxel.text(meteor.text_x+i*4, meteor.y-7, meteor.text[i],8)
 #               pyxel.text(meteor.text_x+(i+1)*4, meteor.y-5, meteor.text[i+1:],15)
 #       else:
 #           pyxel.text(meteor.text_x, meteor.y-7, meteor.text,15)
 #                   
 #       if meteor.hit_frame ==0:
 #           pyxel.blt(meteor.x, meteor.y, 1, 0, 24, 16,16,0)
 #       elif meteor.hit_frame  == 1 or meteor.hit   == 3:
 #           pyxel.blt(meteor.x, meteor.y, 1, 16, 24, 16,16,0)
 #       else:
 #           pyxel.blt(meteor.x, meteor.y, 1, 32, 24, 16,16,0)

 #   def draw_bullet(self, bullet):
 #       pyxel.circ(bullet.x,bullet.y,2, (pyxel.frame_count % 15)+1)

 #   def draw_explosion(self, explosion):
 #       pyxel.blt(explosion.x, explosion.y, 1, 48+16*(5-explosion.frame), 24, 16,16,0)
 #       
 #   def draw(self):
 #       pyxel.cls(0)
 #       for meteor in self.meteor_list:
 #           self.draw_meteor(meteor)
 #       for bullet in self.bullet_list:
 #           self.draw_bullet(bullet)
 #       for explosion in self.explosion_list:
 #           self.draw_explosion(explosion)

