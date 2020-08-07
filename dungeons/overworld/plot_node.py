class PlotNode:
    """Represents core plot location on overworld. Made by OverworldBuilder then passed to DungeonBuilder to connect
    the plot location back to overworld via MajorRoad """

    def __init__(self, name, x, y, entrance, no_fly_zone=[]):
        self.name = name
        self.x = x
        self.y = y
        self.entrance = entrance
        self.no_fly_zone = no_fly_zone

