class Dungeon:
    
    def __init__(self, name, floors, maps, np, edges=None):
        self.name = name
        self.floors = floors
        self.maps = maps
        self.np = np
        self.edges = edges
        
    def set_name(self, name):
        self.name = name
        
    def set_floors(self, floors):
        self.floors = floors
    
    def set_maps(self, maps):
        self.maps = maps
    
    def set_node_power(self, np):
        self.np = np
    