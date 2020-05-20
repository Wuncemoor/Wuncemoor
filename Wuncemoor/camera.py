class Camera:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def refocus(self, px, py, game_map, constants):
        
        if px < constants['map_width']/2:
            self.x = 0
        elif px > game_map.width - constants['map_width']/2:
            self.x = game_map.width - constants['map_width']
        else:
            self.x = int(px - constants['map_width']/2)
        if py < constants['map_height']/2:
            self.y = 0
        elif py > game_map.height - constants['map_height']/2:
            self.y = game_map.height - constants['map_height']
        else:
            self.y = int(py - constants['map_height']/2)
            
