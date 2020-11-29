class Animation:
    def __init__(self,sprites,frame_list):
        self.sprites = sprites
        self.idle = sprites[0]
        self.frame_list = frame_list
        self.timer = 0
        self.sprite = self.sprites[0]

    def update(self):
        self.timer += 1
        if self.timer < len(self.frame_list):
            self.sprite = self.sprites[self.frame_list[self.timer]]
        else:
            self.sprite = self.idle
        
        
    def get_sprite(self):
        return self.sprite
    
    def done(self):
        return self.timer >= len(self.frame_list)

    def reset(self):
        self.timer = 0
    
