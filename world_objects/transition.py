
class Transition:
    """Used to connect maps, stored in TileFloors"""
    def __init__(self, name, images, go_to_dungeon, go_to_floor, go_to_xy):
        self.name = name
        self.images = images
        self.go_to_dungeon = go_to_dungeon
        self.go_to_floor = go_to_floor
        self.go_to_xy = go_to_xy

    def __repr__(self):
        return 'Transition(' + self.name + ', ' + repr(self.images) + ', ' + self.go_to_dungeon + ', ' \
               + str(self.go_to_floor) + ', ' + str(self.go_to_xy) + ') '
