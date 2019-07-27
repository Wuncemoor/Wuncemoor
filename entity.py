#Generic object representing PC and NPC, items, etc
class Entity:

    #Creation
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        
    #Move the entity
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
