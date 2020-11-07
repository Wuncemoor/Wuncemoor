from config.constants import TILES_ON_SCREEN
from math import floor


class Camera:
    """Positioned in the top left corner of the game screen and follows the Party. Used by ArtistHandler to render
    tiles relative to Camera coordinates. """
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def refocus(self, px, py):
        """Called when Party coordinates changes, most commonly through a successful MOVE action or using a Transition
        to another Map or Dungeon. Fits to walls/corners as Party approaches."""
        (width, height) = TILES_ON_SCREEN

        # Ensures all tiles are valid to avoid bound errors/displaying "empty" tiles on potentially half of the screen
        if px < width/2:
            self.x = 0
        elif px > self.owner.owner.world.width - width/2:
            self.x = self.owner.owner.world.width - width
        else:
            self.x = int(px - floor(width/2))
        if py < height/2:
            self.y = 0
        elif py > self.owner.owner.world.height - height/2:
            self.y = self.owner.owner.world.height - height
        else:
            self.y = int(py - floor(height/2))

