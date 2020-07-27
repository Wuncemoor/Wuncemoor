from config.image_objects import STRUCTURE, ALPHA


class Structure:

    def __init__(self, rect, file_objs):
        self.rect = rect
        self.file_objs = file_objs


def make_room(x, y):
    tiles = Tiles2D(x + 2, y + 5)
    add_vwall_images(tiles)
    add_hwall_images(tiles, x)
    carve_room(tiles, x, y)


def add_hwall_images(tiles, length):
    y = 0
    for row in tiles:
        if y == 0:
            for i in row[1:length + 1]:
                i.image = ALPHA
                i.blocked = False
                i.block_sight = False
        if y in (0, len(tiles) - 3):
            for i in row[1: length + 1]:
                i.image_air = STRUCTURE.get('wall_top_h')
        elif y in (1, len(tiles) - 2):
            for i in row[1:length + 1]:
                i.image = STRUCTURE.get('wall_mid')
        elif y in (2, len(tiles) - 1):
            for i in row[1:length + 1]:
                i.image = STRUCTURE.get('wall_bot')
        y += 1


def add_vwall_images(tiles):

    y = 0
    for row in tiles:
        if y == 0:
            row[0].image = ALPHA
            row[0].image_air = STRUCTURE.get('pillar_top')
            row[0].blocked = False
            row[0].block_sight = False
            row[-1].image = ALPHA
            row[-1].image_air = STRUCTURE.get('pillar_top')
            row[-1].blocked = False
            row[-1].block_sight = False
        elif y == len(tiles) - 3:
            row[0].image = STRUCTURE.get('wall_top_v')
            row[0].image_air = STRUCTURE.get('pillar_top')
            row[-1].image = STRUCTURE.get('wall_top_v')
            row[-1].image_air = STRUCTURE.get('pillar_top')
        elif y == len(tiles) - 2:
            row[0].image = STRUCTURE.get('pillar_mid')
            row[-1].image = STRUCTURE.get('pillar_mid')
        elif y == len(tiles) - 1:
            row[0].image = STRUCTURE.get('pillar_bot')
            row[-1].image = STRUCTURE.get('pillar_bot')
        else:
            row[0].image = STRUCTURE.get('wall_top_v')
            row[-1].image = STRUCTURE.get('wall_top_v')
        y += 1


def carve_room(tiles, x, y):
    for row in tiles[2: 2 + y]:
        for tile in row[1: 1 + x]:
            tile.image = STRUCTURE.get('inn_floor_s')
            tile.blocked = False
            tile.block_sight = False
