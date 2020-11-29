IDLE = 0
HIT  = 1 

class Rock:
    def __init__(self,x,y,idle,hitanim):
        self.x = x
        self.y = y
        self.idle = idle
        self.hitanim = hitanim
        self.anim = idle
        self.sprite = self.anim.get_sprite()
        self.state = IDLE
        self.previous_state = IDLE

    def set_xy(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x +=dx
        self.y +=dy
        
    def set_state(self,state):
        self.previous_state = self.state
        self.state = state

    def hit(self):
        self.set_state(HIT)
        self.hitanim.reset()

    def get_state(self):
        return self.state

    def update(self):
        if self.hitanim.done():
            self.hitanim.reset()
            self.set_state(IDLE)
            self.anim = self.idle
            self.anim.reset()
        elif self.state == IDLE:
            self.anim = self.idle
        elif self.state == HIT:
            self.anim = self.hitanim

        self.anim.update() 
        self.sprite = self.anim.get_sprite()

    def draw(self):
        self.sprite.draw(self.x,self.y)

    
