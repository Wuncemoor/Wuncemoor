from opensimplex import OpenSimplex
import random


def apply_simplex_biomes(map, constants):
    equator = constants['height'] / 2

    heightmesh = OpenSimplex(seed=random.randint(1, 1000000))
    heightmesh2 = OpenSimplex(seed=random.randint(1, 1000000))
    heightmesh3 = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh2 = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh3 = OpenSimplex(seed=random.randint(1, 1000000))

    for j in range(constants['height']):

        tempdiff = abs(equator - j) / equator

        for i in range(constants['width']):

            amp = 1
            freq = 1
            height = 0
            moist = 0
            temp = 1 - tempdiff

            for k in range(constants['octaves']):
                octavex = j * constants['scale'] * freq
                octavey = i * constants['scale'] * freq

                hvalue = heightmesh.noise2d(x=octavex, y=octavey)
                hvalue2 = heightmesh2.noise2d(x=octavex, y=octavey)
                hvalue3 = heightmesh3.noise2d(x=octavex, y=octavey)
                mvalue = moistmesh.noise2d(x=octavex, y=octavey)
                mvalue2 = moistmesh2.noise2d(x=octavex, y=octavey)
                mvalue3 = moistmesh3.noise2d(x=octavex, y=octavey)
                height += avg([hvalue, hvalue2, hvalue3]) * amp
                moist += avg([mvalue, mvalue2, mvalue3]) * amp

                amp *= constants['persist']
                freq *= constants['lacuna']
            heightmod = (abs(height)) * .7
            temp -= heightmod
            moist -= heightmod
            moist += constants['moist_mod']
            temp += constants['temp_mod']
            templist = [('very_hot', 5 / 6), ('hot', 4 / 6), ('warm', 3 / 6), ('cool', 2 / 6), ('cold', 1 / 6),
                        ('very_cold', 0), ('polar', -10)]

            if height <= constants['water_level']:
                if height > 0:
                    map.tiles[i][j].type = 'shallow'
                else:
                    map.tiles[i][j].type = 'deep'

            else:

                temp = temperature(templist, temp)
                moistlist = get_moistlist(temp)
                biome = moisture(moistlist, moist)
                map.tiles[i][j].type = biome

def moisture(table, moist_level):
    for (value, level) in table:
        if moist_level >= level:
            return value
    return -1


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


def temperature(table, temp_level):
    for (value, level) in table:
        if temp_level >= level:
            return value
    return -1


def avg(list):
    x = 0
    for i in list:
        x += i
    return x / len(list)