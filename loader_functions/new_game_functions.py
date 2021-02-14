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
from ECS.__entity.__combatant.equipment import Equipment
from ECS.__entity.combatant import Combatant
from ECS.__entity.age import Age
from handlers.log_handler import LogHandler
from handlers.menus.char_sheet import CharSheet
from handlers.menus.inventory import Inventory
from handlers.menus.map import Map
from ECS.entity import Entity
from enums.equipment_slots import EquipmentSlots
from enums.render_order import RenderOrder
from handlers.menus.journal import Quest, QuestNode, Journal
from config.image_objects import BUNDLE_HERO, BUNDLE_STICK
from handlers.party_handler import PartyHandler
from handlers.time_handler import TimeHandler
from handlers.world_handler import WorldHandler


def get_party():
    player = get_player()
    party = PartyHandler(player)
    party.char_sheet = CharSheet()
    party.inventory = Inventory()
    party.inventory.owner = party
    party.inventory.money += 100
    party.map = Map()
    party.x, party.y = player.x, player.y
    party.focus = party.p1

    return party


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
    age = Age(10, 0, 0, 0)
    player = Entity(13, 13, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant, age=age)

    # player = Entity(75, 19, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant, age=age)
    return player


def get_starting_items(party):
    item_component = Item(1,
        Equippable('Stick', BUNDLE_STICK, EquipmentSlots.MAIN_HAND, EquippableCore('staff', BUNDLE_STICK),
                   EquippableMaterial('wood'), EquippableQuality('average')))
    stick = Entity(0, 0, item=item_component)
    party.inventory.add_item(stick)


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


def make_new_game_model():

    party = get_party()

    get_starting_items(party)

    world = WorldHandler()
    world.new()

    journal = Journal()
    journal.current_quests.append(get_intro_quest())
    party.journal = journal
    time = TimeHandler([party])
    log = LogHandler()

    model = DataModel(world, party, time, log)

    return model


class DataModel:
    """One container to store and isolate all data that represents the current state of the program. Used to easily save
     and load games."""

    def __init__(self, world, party, time, log):
        self.world = world
        self.party = party
        self.time = time
        self.log = log
