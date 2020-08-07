def get_cave(subtype):
    (width, height) = CAVE
    dungeon_builder = DungeonBuilder('cave', subtype, 5, width, height, 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon()

    return cave