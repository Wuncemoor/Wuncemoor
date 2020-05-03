import tcod as libtcod
from components.attributes import Attributes
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
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
from loader_functions.constants import get_constants
from maps.starting_map import get_starting_town, get_directed_dungeon, get_cave, get_goblin_cave, get_kobold_cave, get_map, get_world_map
from map_objects.dungeon import Dungeon
from camera import Camera
from entity import Entity
from equipment_slots import EquipmentSlots
from render_functions import RenderOrder

def get_player():
    phylo_component = Phylo('sapient','human','hero','regular','tabula_rasa')
    attribute_component = Attributes(10,10,10,10,10,10,10,10,10,10)
    inventory_component = Inventory(26)
    level_component = Level()
    competence_component = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(), Finesse(), Charisma(), Devotion())
    equipment_component = Equipment()
    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\hero.png'
    combatant_component = Combatant('Player', image, phylo=phylo_component, attributes=attribute_component, level=level_component, competence=competence_component, equipment=equipment_component, inventory=inventory_component)

    
    player = Entity(64, 25, libtcod.white, blocks=True, render_order = RenderOrder.ACTOR, combatant=combatant_component)
    
    return player
def get_camera(player, constants):

    camera = Camera(player.x - int(constants['map_width']/2), player.y - int(constants['map_height']/2))
    return camera
    
def equip_player(player):
    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\\stick.png'
    item_component = Item(Equippable('Stick', image, EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'), EquippableQuality('average')))
    stick = Entity(0, 0, libtcod.sky, item=item_component)
    player.combatant.inventory.add_item(stick)
    player.combatant.equipment.toggle_equip(stick)

def get_dungeons(constants):
    
    dungeons = {}
    
    town_alpha = get_starting_town(constants)
    dungeons[town_alpha.name] = town_alpha
    
    
    directed_dungeon = get_directed_dungeon(constants)
    dungeons[directed_dungeon.name] = directed_dungeon
    
    goblin_cave = get_cave(constants, 'goblin')
    dungeons[goblin_cave.name] = goblin_cave
    
    kobold_cave = get_cave(constants, 'kobold')
    dungeons[kobold_cave.name]  = kobold_cave
    
    cave = get_cave(constants, None)
    dungeons[cave.name] = cave
    
    downstairsimg = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\stairsdown.png'
    upstairsimg = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\stairsup.png'

    directed_entrance = directed_dungeon.maps[0].entrance
    directed_stairs_component = Stairs('Stairs', downstairsimg, 'directed_dungeon', 0, directed_entrance)
    directed_stairs = Entity(40, 10, libtcod.white, render_order=RenderOrder.STAIRS, stairs=directed_stairs_component)
    
    directed_stairs_up_component = Stairs('Stairs', upstairsimg, 'start', 0, (40,10))
    directed_stairs_up = Entity(directed_dungeon.maps[0].entrance[0], directed_dungeon.maps[0].entrance[1], libtcod.white, render_order=RenderOrder.STAIRS, stairs=directed_stairs_up_component)
    
    town_alpha.maps[0].map_entities.append(directed_stairs)
    directed_dungeon.maps[0].map_entities.append(directed_stairs_up)
    
    gob_stairs_comp = Stairs('Stairs', downstairsimg, 'goblin_cave', 0, goblin_cave.maps[0].entrance)
    gob_stairs = Entity(10, 30, libtcod.white, render_order=RenderOrder.STAIRS, stairs=gob_stairs_comp)
    town_alpha.maps[0].map_entities.append(gob_stairs)
    
    gob_stairs_up_comp = Stairs('Stairs', upstairsimg, 'start', 0, (10,30))
    gob_stairs_up = Entity(goblin_cave.maps[0].entrance[0], goblin_cave.maps[0].entrance[1], libtcod.white, render_order=RenderOrder.STAIRS, stairs=gob_stairs_up_comp)
    goblin_cave.maps[0].map_entities.append(gob_stairs_up)
    
    kob_stairs_comp = Stairs('Stairs', downstairsimg, 'kobold_cave', 0, kobold_cave.maps[0].entrance)
    kob_stairs = Entity(10, 25, libtcod.white, render_order=RenderOrder.STAIRS, stairs=kob_stairs_comp)
    town_alpha.maps[0].map_entities.append(kob_stairs)
    
    kob_stairs_up_comp = Stairs('Stairs', upstairsimg, 'start', 0, (10,25))
    kob_stairs_up = Entity(kobold_cave.maps[0].entrance[0], kobold_cave.maps[0].entrance[1], libtcod.white, render_order=RenderOrder.STAIRS, stairs=kob_stairs_up_comp)
    kobold_cave.maps[0].map_entities.append(kob_stairs_up)
    
    cave_stairs_comp = Stairs('Stairs', downstairsimg, 'cave', 0, cave.maps[0].entrance)
    cave_stairs = Entity(10, 20, libtcod.white, render_order=RenderOrder.STAIRS, stairs=cave_stairs_comp)
    town_alpha.maps[0].map_entities.append(cave_stairs)
    
    cave_stairs_up_comp = Stairs('Stairs', upstairsimg, 'start', 0, (10,20))
    cave_stairs_up = Entity(cave.maps[0].entrance[0], cave.maps[0].entrance[1], libtcod.white, render_order=RenderOrder.STAIRS, stairs=cave_stairs_up_comp)
    cave.maps[0].map_entities.append(cave_stairs_up)
    


    
    return dungeons
    
    