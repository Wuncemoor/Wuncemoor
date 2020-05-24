import tcod as libtcod
from components.attributes import Attributes
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, \
    Finesse, Charisma, Devotion
from components.equippable import Equippable
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.inventory import Inventory
from components.item import Item
from components.level import Level
from components.phylo import Phylo
from components.stairs import Stairs
from components.equipment import Equipment
from components.combatant import Combatant
from maps.starting_map import get_cave, get_town, get_world_map
from camera import Camera
from entity import Entity
from equipment_slots import EquipmentSlots
from render_functions import RenderOrder


def get_player():
    phylo_component = Phylo('sapient', 'human', 'hero', 'regular', 'tabula_rasa')
    attribute_component = Attributes(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    inventory_component = Inventory(26)
    level_component = Level()
    competence_component = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(),
                                      Wisdom(), Finesse(), Charisma(), Devotion())
    equipment_component = Equipment()
    image = 'images\\hero.png'
    combatant_component = Combatant('Player', image, phylo=phylo_component, attributes=attribute_component,
                                    level=level_component, competence=competence_component,
                                    equipment=equipment_component, inventory=inventory_component)

    player = Entity(5, 20, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant_component)

    return player


def get_camera(player, constants):
    camera = Camera(player.x - int(constants['map_width'] / 2), player.y - int(constants['map_height'] / 2))
    return camera


def equip_player(player):
    image = 'images\\stick.png'
    item_component = Item(
        Equippable('Stick', image, EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'),
                   EquippableQuality('average')))
    stick = Entity(0, 0, item=item_component)
    player.combatant.inventory.add_item(stick)
    player.combatant.equipment.toggle_equip(stick)


def get_dungeons(constants):
    dungeons = {}

    world, nodes = get_world_map(constants['world_map_constants'])
    wm_tiles = world.maps[0].tiles
    dungeons[world.name] = world

    town = get_town(constants['start_town_width'], constants['start_town_height'], nodes[0])
    dungeons[town.name] = town

    town2 = get_town(constants['start_town_width'], constants['start_town_height'], nodes[1])
    dungeons[town2.name] = town2

    town3 = get_town(constants['start_town_width'], constants['start_town_height'], nodes[2])
    dungeons[town3.name] = town3

    town4 = get_town(constants['start_town_width'], constants['start_town_height'], nodes[3])
    dungeons[town4.name] = town4

    goblin_cave = get_cave(constants, 'goblin')
    dungeons[goblin_cave.name] = goblin_cave

    kobold_cave = get_cave(constants, 'kobold')
    dungeons[kobold_cave.name] = kobold_cave

    cave = get_cave(constants, None)
    dungeons[cave.name] = cave

    downstairsimg = constants['stairs'].get('down')
    upstairsimg = constants['stairs'].get('up')

    gob_stairs_comp = Stairs('Stairs', downstairsimg, 'goblin_cave', 0, goblin_cave.maps[0].entrance)
    gob_stairs = Entity(10, 30, libtcod.white, render_order=RenderOrder.STAIRS, stairs=gob_stairs_comp)
    town.maps[0].transitions.append(gob_stairs)

    gob_stairs_up_comp = Stairs('Stairs', upstairsimg, 'town', 0, (10, 30))
    gob_stairs_up = Entity(goblin_cave.maps[0].entrance[0], goblin_cave.maps[0].entrance[1], libtcod.white,
                           render_order=RenderOrder.STAIRS, stairs=gob_stairs_up_comp)
    goblin_cave.maps[0].transitions.append(gob_stairs_up)

    kob_stairs_comp = Stairs('Stairs', downstairsimg, 'kobold_cave', 0, kobold_cave.maps[0].entrance)
    kob_stairs = Entity(10, 25, libtcod.white, render_order=RenderOrder.STAIRS, stairs=kob_stairs_comp)
    town.maps[0].transitions.append(kob_stairs)

    kob_stairs_up_comp = Stairs('Stairs', upstairsimg, 'town', 0, (10, 25))
    kob_stairs_up = Entity(kobold_cave.maps[0].entrance[0], kobold_cave.maps[0].entrance[1], libtcod.white,
                           render_order=RenderOrder.STAIRS, stairs=kob_stairs_up_comp)
    kobold_cave.maps[0].transitions.append(kob_stairs_up)

    cave_stairs_comp = Stairs('Stairs', downstairsimg, 'cave', 0, cave.maps[0].entrance)
    cave_stairs = Entity(10, 20, libtcod.white, render_order=RenderOrder.STAIRS, stairs=cave_stairs_comp)
    town.maps[0].transitions.append(cave_stairs)

    cave_stairs_up_comp = Stairs('Stairs', upstairsimg, 'town', 0, (10, 20))
    cave_stairs_up = Entity(cave.maps[0].entrance[0], cave.maps[0].entrance[1], libtcod.white,
                            render_order=RenderOrder.STAIRS, stairs=cave_stairs_up_comp)
    cave.maps[0].transitions.append(cave_stairs_up)

    return dungeons, wm_tiles
