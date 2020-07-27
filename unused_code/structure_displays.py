def add_house(map, x, y):
    house = Structure(Rect(x, y, 5, 6), get_house_images())
    map.structures.append(house)


def add_hut(map, x, y):
    hut = Structure(Rect(x, y, 17, 17), get_hut_obj())
    map.structures.append(hut)
