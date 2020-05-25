from components.stairs import Stairs
from entity import Entity

class Road:

    def __init__ (self, rect, go_to_dungeon=None, go_to_floor=None, go_to_xy=None, transitions_img=None):
        self.rect = rect
        self.go_to_dungeon = go_to_dungeon
        self.go_to_floor = go_to_floor
        self.go_to_xy = go_to_xy
        self.transitions = []
        self.transitions_img = transitions_img

    def set_transitions(self, dimension):
        stairs = Stairs('Stairs', self.transitions_img, self.go_to_dungeon, self.go_to_floor, self.go_to_xy)
        if dimension == 'vertical':
            for j in range(self.rect.y1, self.rect.y2):
                self.transitions.append(Entity(self.rect.x1, j, stairs=stairs))
                self.transitions.append(Entity(self.rect.x2-1, j, stairs=stairs))

        elif dimension == 'horizontal':
            for i in range(self.rect.x1, self.rect.x2):
                self.transitions.append(Entity(i, self.rect.y1, stairs=stairs))
                self.transitions.append(Entity(i, self.rect.y2-1, stairs=stairs))