from ECS.__entity.__combatant.attributes import Attributes
from ECS.__entity.__combatant.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, \
    Improvisation, Wisdom, Finesse, Charisma, Devotion
from ECS.__entity.__combatant.level import Level
from ECS.__entity.__combatant.phylo import Phylo
from ECS.__entity.__combatant.satchel import Satchel
from ECS.__entity.__item.equippable import Equippable
from ECS.__entity.__item.__equippable.equippable_core import EquippableCore
from ECS.__entity.__item.__equippable.equippable_material import EquippableMaterial
from ECS.__entity.__item.__equippable.equippable_quality import EquippableQuality
from ECS.__entity.item import Item
from ECS.__entity.transition import Transition
from ECS.__entity.__combatant.equipment import Equipment
from ECS.__entity.combatant import Combatant
from ECS.__entity.age import Age
from maps.starting_map import get_cave, get_town, get_world_map

from ECS.entity import Entity
from enums.equipment_slots import EquipmentSlots
from enums.render_order import RenderOrder
from handlers.menus.journal import Quest, QuestNode
from config.image_objects import BUNDLE_HERO, BUNDLE_STICK, STAIRS_DOWN, STAIRS_UP
from config.constants import WHITE


def get_player():
    phylo = Phylo('sapient', 'sunborn', 'human', 'regular', 'tabula_rasa')
    attributes = Attributes(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    satchel = Satchel(3)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(),
                            Wisdom(), Finesse(), Charisma(), Devotion())
    equipment = Equipment()

    combatant = Combatant('Player', BUNDLE_HERO, phylo=phylo, attributes=attributes,
                          level=level, competence=competence,
                          equipment=equipment, satchel=satchel, sex='male')
    age = Age(10, 0, 0, 0, (1, 1))

    player = Entity(5, 20, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant, age=age)

    return player


def equip_player(party):
    item_component = Item(
        Equippable('Stick', BUNDLE_STICK, EquipmentSlots.MAIN_HAND, EquippableCore('staff', BUNDLE_STICK),
                   EquippableMaterial('wood'), EquippableQuality('average')))
    stick = Entity(0, 0, item=item_component)
    party.inventory.add_item(stick)


def get_dungeons():
    dungeons = {}

    world, nodes = get_world_map()

    wm_tiles = world.maps[0].tiles

    dungeons[world.name] = world

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

    return dungeons, wm_tiles


def get_intro_quest():
    title = 'An Ominous Dream'
    node2 = QuestNode("Talked to Samwise",
                      "I told Samwise all about my dream. He thought it was cool, but that I shouldn't worry so much.")
    node1 = QuestNode('Find Samwise',
                      "That was by FAR the most intense dream you've ever had. You've got to talk to Samwise about it!",
                      condition='samwise', plot_paths={'COMPLETE': node2})
    q = Quest(title, node1)
    q.plot.append(node1)

    return q
