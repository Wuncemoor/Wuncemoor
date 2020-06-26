class Dungeon:
    
    def __init__(self, name, floors, maps, np, edges=None):
        self.name = name
        self.floors = floors
        self.maps = maps
        self.np = np
        self.edges = edges
        self.time_dilation = 0
