from config.constants import TILES_ON_SCREEN


class Camera:
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def refocus(self, px, py, game_map):
        (width, height) = TILES_ON_SCREEN
        
        if px < width/2:
            self.x = 0
        elif px > game_map.width - width/2:
            self.x = game_map.width - width
        else:
            self.x = int(px - width/2)
        if py < height/2:
            self.y = 0
        elif py > game_map.height - height/2:
            self.y = game_map.height - height
        else:
            self.y = int(py - height/2)
