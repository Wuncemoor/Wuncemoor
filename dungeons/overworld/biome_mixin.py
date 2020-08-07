from opensimplex import OpenSimplex
from random import randint
from map_objects.floors import biome_floors
from config.constants import SIMPLEX


class BiomeMixin:
    """Mixin for OverworldBuilder. Allows placement of BiomeTileFloors via OpenSimplex algorithm"""

    def apply_simplex_biomes(self, map):
        (octaves, persist, lacuna, scale, moist_mod, temp_mod, water_level) = SIMPLEX
        width, height = map.width, map.height
        equator = height / 2

        heightmesh = OpenSimplex(seed=randint(1, 1000000))
        moistmesh = OpenSimplex(seed=randint(1, 1000000))

        for j in range(height):

            tempdiff = abs(equator - j) / equator

            for i in range(width):

                amp = 1
                freq = 1
                altitude = 0
                moist = 0
                temp = 1 - tempdiff

                for k in range(octaves):
                    octavex = j * scale * freq
                    octavey = i * scale * freq

                    hvalue = heightmesh.noise2d(x=octavex, y=octavey)
                    mvalue = moistmesh.noise2d(x=octavex, y=octavey)
                    altitude += hvalue * amp
                    moist += mvalue * amp

                    amp *= persist
                    freq *= lacuna
                altmod = (abs(altitude)) * .7
                temp -= altmod
                moist -= altmod
                moist += moist_mod
                temp += temp_mod
                templist = [('very_hot', 5 / 6), ('hot', 4 / 6), ('warm', 3 / 6), ('cool', 2 / 6), ('cold', 1 / 6),
                            ('very_cold', 0), ('polar', -10)]

                if altitude <= water_level:
                    if altitude > 0:
                        map.tiles[i][j].type = 'shallow'
                    else:
                        map.tiles[i][j].type = 'deep'
                    self.get_biome_floor(map.tiles[i][j])

                else:

                    temp = self.temperature(templist, temp)
                    moistlist = self.get_moistlist(temp)
                    biome = self.moisture(moistlist, moist)
                    map.tiles[i][j].type = biome
                    self.get_biome_floor(map.tiles[i][j])

    @staticmethod
    def get_biome_floor(tile):
        floor_dict = {
            'deep': biome_floors.DeepTileFloor(),
            'desert': biome_floors.DesertTileFloor(),
            'forest': biome_floors.ForestTileFloor(),
            'plains': biome_floors.PlainsTileFloor(),
            'savannah': biome_floors.SavannahTileFloor(),
            'shallow': biome_floors.ShallowTileFloor(),
            'snow': biome_floors.SnowTileFloor(),
            'taiga': biome_floors.TaigaTileFloor(),
            'temprain': biome_floors.TemprainTileFloor(),
            'tropicrain': biome_floors.TropicrainTileFloor(),
            'tundra': biome_floors.TundraTileFloor(),
        }
        tile.floor = floor_dict.get(tile.type)

    @staticmethod
    def moisture(table, moist_level):
        for (value, level) in table:
            if moist_level >= level:
                return value
        return -1

    @staticmethod
    def get_moistlist(temp):
        dict = {
            'very_hot': [('tropicrain', .4), ('savannah', 0), ('desert', -10)],
            'hot': [('temprain', .5), ('forest', .3), ('savannah', 0), ('desert', -10)],
            'warm': [('temprain', .65), ('forest', .3), ('savannah', 0), ('plains', -.25), ('desert', -10)],
            'cool': [('temprain', .7), ('forest', .2), ('savannah', -.2), ('plains', -.5), ('desert', -10)],
            'cold': [('taiga', 0), ('plains', -10)],
            'very_cold': [('tundra', 0), ('snow', -10)],
            'polar': [('snow', -10)],
        }

        return dict[temp]

    @staticmethod
    def temperature(table, temp_level):
        for (value, level) in table:
            if temp_level >= level:
                return value
        return -1

    @staticmethod
    def avg(list):
        x = 0
        for i in list:
            x += i
        return x / len(list)
