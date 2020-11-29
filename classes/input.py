import pyxel

class Input():
    def __init__(self):
        self.input_list = []

    def get_input_list(self):
         self.input_list = [key for key in range(pyxel.KEY_A,pyxel.KEY_Z+1) if pyxel.btnr(key)]
         self.input_list += [key for key in (pyxel.KEY_UP,pyxel.KEY_DOWN,pyxel.KEY_LEFT,pyxel.KEY_RIGHT,pyxel.KEY_SPACE)  if pyxel.btnr(key)]         
         return self.input_list
