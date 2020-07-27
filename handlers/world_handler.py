from builders.world_builder import DungeonDirector


class WorldHandler:

    def __init__(self):
        self.build = DungeonDirector()
        self.build.owner = self
        self.dungeons = None
        self.current_dungeon = None
        self.current_map = None

    def new(self):
        dungeons = {}

        overworld = self.build.overworld()

        dungeons[overworld.name] = overworld

        town = get_town(nodes[0])
        dungeons[town.name] = town

        town2 = get_town(nodes[1])
        dungeons[town2.name] = town2

        town3 = get_town(nodes[2])
        dungeons[town3.name] = town3

        town4 = get_town(nodes[3])
        dungeons[town4.name] = town4

        goblin_cave = get_cave('goblin')
        dungeons[goblin_cave.name] = goblin_cave

        downstairsimg = STAIRS_DOWN
        upstairsimg = STAIRS_UP

        # kobold_cave = get_cave( 'kobold')
        # dungeons[kobold_cave.name] = kobold_cave
        #
        #
        # cave = get_cave(None)
        # dungeons[cave.name] = cave

        gob_stairs_comp = Transition('Stairs', downstairsimg, 'goblin_cave', 0, goblin_cave.maps[0].entrance)
        gob_stairs = Entity(10, 30, WHITE, render_order=RenderOrder.STAIRS, transition=gob_stairs_comp)
        town.maps[0].transitions.append(gob_stairs)

        gob_stairs_up_comp = Transition('Stairs', upstairsimg, 'town', 0, (10, 30))
        gob_stairs_up = Entity(goblin_cave.maps[0].entrance[0], goblin_cave.maps[0].entrance[1], WHITE,
                               render_order=RenderOrder.STAIRS, transition=gob_stairs_up_comp)
        goblin_cave.maps[0].transitions.append(gob_stairs_up)

        # kob_stairs_comp = Transition('Stairs', downstairsimg, 'kobold_cave', 0, kobold_cave.maps[0].entrance)
        # kob_stairs = Entity(10, 25, libtcod.white, render_order=RenderOrder.STAIRS, transition=kob_stairs_comp)
        # town.maps[0].transitions.append(kob_stairs)
        #
        # kob_stairs_up_comp = Transition('Stairs', upstairsimg, 'town', 0, (10, 25))
        # kob_stairs_up = Entity(kobold_cave.maps[0].entrance[0], kobold_cave.maps[0].entrance[1], libtcod.white,
        #                        render_order=RenderOrder.STAIRS, transition=kob_stairs_up_comp)
        # kobold_cave.maps[0].transitions.append(kob_stairs_up)
        #
        # cave_stairs_comp = Transition('Stairs', downstairsimg, 'cave', 0, cave.maps[0].entrance)
        # cave_stairs = Entity(10, 20, libtcod.white, render_order=RenderOrder.STAIRS, transition=cave_stairs_comp)
        # town.maps[0].transitions.append(cave_stairs)
        #
        # cave_stairs_up_comp = Transition('Stairs', upstairsimg, 'town', 0, (10, 20))
        # cave_stairs_up = Entity(cave.maps[0].entrance[0], cave.maps[0].entrance[1], libtcod.white,
        #                         render_order=RenderOrder.STAIRS, transition=cave_stairs_up_comp)
        # cave.maps[0].transitions.append(cave_stairs_up)
        self.dungeons = dungeons
        self.current_dungeon = dungeons['town']
        self.current_map = dungeons['town'].maps[0]

    @property
    def width(self):
        return self.current_map.width

    @property
    def height(self):
        return self.current_map.height

    @property
    def tiles(self):
        return self.current_map.tiles

    @property
    def variant(self):
        return self.current_map.variant

    @property
    def dungeon_level(self):
        return self.current_map.dungeon_level

    @property
    def dangerous(self):
        return self.current_map.dangerous

    def is_blocked(self, x, y):
        if self.current_map.tiles[x][y].blocked:
            return True

        return False
