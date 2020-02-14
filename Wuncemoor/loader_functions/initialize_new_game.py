import tcod as libtcod
from PIL import Image
from builders.dungeon_builder import DungeonDirector, DungeonBuilder
from components.combatant import Combatant
from components.item import Item
from components.inventory import Inventory
from components.level import Level
from components.stairs import Stairs
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.equipment import Equipment
from components.equippable import Equippable, get_equippable
from components.attributes import Attributes
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from map_objects.dungeon import Dungeon
from render_functions import RenderOrder
from maps.starting_map import get_starting_town, get_dungeon

    
def get_game_variables(constants):
    attribute_component = Attributes(10,10,10,10,10,10,10,10,10,10)
    inventory_component = Inventory(26)
    level_component = Level()
    competence_component = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(), Finesse(), Charisma(), Devotion())
    equipment_component = Equipment()
    combatant_component = Combatant('Player', '@', attributes=attribute_component, level=level_component, competence=competence_component, equipment=equipment_component, inventory=inventory_component)

    
    player = Entity(30, 30, libtcod.white, blocks=True, render_order = RenderOrder.ACTOR, combatant=combatant_component)
    
    entities = [player]
    
    item_component = Item(Equippable('Stick', '-', EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'), EquippableQuality('average')))
    stick = Entity(0, 0, libtcod.sky, item=item_component)
    player.combatant.inventory.add_item(stick)
    player.combatant.equipment.toggle_equip(stick)
    
    town_alpha = get_starting_town(constants['map_width'], constants['map_height'])
    
    start_map = get_dungeon(constants['map_width'], constants['map_height'])
    start_map.fill_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'], constants['map_width'], constants['map_height'])
    start_dungeon = Dungeon('start_dungeon', 1, [start_map])
    
    xy = start_map.entrance
    stairs_component = Stairs('Stairs', '>', 'start_dungeon', 0, xy)
    
    down_stairs = Entity(40, 40, libtcod.white, render_order=RenderOrder.STAIRS, stairs=stairs_component)
    town_alpha.maps[0].map_entities.append(down_stairs)
    
    
    dungeon_builder = DungeonBuilder('directed_dungeon', 5, constants['map_width'], constants['map_height'])
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    directed_dungeon = dungeon_director.get_dungeon()
    directed_entrance = directed_dungeon.maps[0].entrance
    directed_stairs_component = Stairs('Stairs', '>', 'directed_dungeon', 0, directed_entrance)
    directed_stairs = Entity(40, 10, libtcod.white, render_order=RenderOrder.STAIRS, stairs=directed_stairs_component)
    
    directed_stairs_up_component = Stairs('Stairs', '<', 'start', 0, (40,10))
    directed_stairs_up = Entity(40, 10, libtcod.white, render_order=RenderOrder.STAIRS, stairs=directed_stairs_up_component)
    
    town_alpha.maps[0].map_entities.append(directed_stairs)
    directed_dungeon.maps[0].map_entities.append(directed_stairs_up)
    
    dungeons = { 'start': town_alpha, 'start_dungeon': start_dungeon, 'directed_dungeon':directed_dungeon }
    game_map = GameMap(town_alpha.maps[0])
    
    entities.extend(game_map.current_map.map_entities)
    
    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN
    
    return player, dungeons, entities, game_map, message_log, game_state
    