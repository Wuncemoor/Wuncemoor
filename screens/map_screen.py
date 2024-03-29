from config.image_objects import MAP_BG
from data_structures.gui_tools import get_surface, align_and_blit, get_alpha_surface


def map_screen(self):
    display = get_surface(MAP_BG)
    overworld_tiles = self.game.model.world.dungeons['overworld'].maps[0].tiles
    window = get_alpha_surface(len(overworld_tiles[0]), len(overworld_tiles))

    i, j = 0, 0

    for row in self.game.model.world.mini:
        for img in row:
            if overworld_tiles[j][i].explored:
                window.blit(img, (i, j))
            i += 1
        j += 1
        i = 0
    align_and_blit(display, window)
    align_and_blit(self.screen, display)