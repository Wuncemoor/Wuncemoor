class Dungeon:
    
    def __init__(self, name, floors, maps, np):
        self.name = name
        self.floors = floors
        self.maps = maps
        self.np = np
        self.time_dilation = [-65, 1, 1, 6]

    def __repr__(self):
        return 'Dungeon(' + self.name + ', ' + str(self.floors) + ', ' + repr(self.maps) + ', ' + str(self.np) + ')'
