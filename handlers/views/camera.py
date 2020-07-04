from config.constants import TILES_ON_SCREEN


class Camera:
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def refocus(self, px, py):
        (width, height) = TILES_ON_SCREEN
        
        if px < width/2:
            self.x = 0
        elif px > self.owner.owner.world.width - width/2:
            self.x = self.owner.owner.world.width - width
        else:
            self.x = int(px - width/2)
        if py < height/2:
            self.y = 0
        elif py > self.owner.owner.world.height - height/2:
            self.y = self.owner.owner.world.height - height
        else:
            self.y = int(py - height/2)
