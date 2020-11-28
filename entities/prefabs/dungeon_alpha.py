from ECS.__entity.age import Age
from ECS.__entity.noncombatant import Noncombatant
from ECS.__entity.shopkeeper import Shopkeeper
from ECS.entity import Entity
from builders.make_item import make_item
from config.image_objects import DUNGEON_ALPHA_NONCOMBATANT_IMAGE_BUNDLES as DANIB
from dialogue.prefabs.dungeon_alpha import get_samwise_dialogue, get_mage_dialogue, get_guard_captain_dialogue, \
    get_priest_dialogue, get_rogue_dialogue, get_homer_dialogue, get_mayor_dialogue, get_innkeeper_dialogue, \
    get_tavernkeeper_dialogue
from enums.render_order import RenderOrder
from handlers.menus.inventory import Inventory


def get_samwise():
    dialogue = get_samwise_dialogue()
    noncom = Noncombatant('samwise', DANIB.get('samwise'), dialogue)
    age = Age(13, 12, 28, 0, (1, 4))
    inven = Inventory()
    potion = make_item('healing_potion')
    inven.add_item(potion)
    shopkeeper = Shopkeeper(inven)
    samwise = Entity(73, 24, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age,
                     shopkeeper=shopkeeper)
    return samwise


def get_mage():

    dialogue = get_mage_dialogue()
    noncom = Noncombatant('Mage', DANIB.get('mage'), dialogue)
    age = Age(57, 4, 16, 0, (8, 15))
    inven = Inventory()
    potion = make_item('healing_potion')
    inven.add_item(potion)
    shopkeeper = Shopkeeper(inven)
    mage = Entity(10, 10, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age,
                  shopkeeper=shopkeeper)
    return mage


def get_guard_captain():

    dialogue = get_guard_captain_dialogue()
    noncom = Noncombatant('Guard Captain', DANIB.get('guard_captain'), dialogue)
    age = Age(36, 10, 11, 0, (2, 20))
    inven = Inventory()
    potion = make_item('healing_potion')
    inven.add_item(potion)
    shopkeeper = Shopkeeper(inven)
    guard_captain = Entity(17, 49, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age,
                           shopkeeper=shopkeeper)
    return guard_captain


def get_priest():

    dialogue = get_priest_dialogue()
    noncom = Noncombatant('Priest', DANIB.get('priest'), dialogue)
    age = Age(62, 3, 22, 0, (9, 9))
    inven = Inventory()
    potion = make_item('healing_potion')
    inven.add_item(potion)
    shopkeeper = Shopkeeper(inven)
    priest = Entity(87, 21, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age,
                           shopkeeper=shopkeeper)
    return priest


def get_rogue():

    dialogue = get_rogue_dialogue()
    noncom = Noncombatant('Rogue', DANIB.get('rogue'), dialogue)
    age = Age(19, 6, 25, 0, (6, 6))
    inven = Inventory()
    potion = make_item('healing_potion')
    inven.add_item(potion)
    shopkeeper = Shopkeeper(inven)
    rogue = Entity(86, 59, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age,
                           shopkeeper=shopkeeper)
    return rogue


def get_homer():

    dialogue = get_homer_dialogue()
    noncom = Noncombatant('Homer', DANIB.get('homer'), dialogue)
    age = Age(45, 9, 4, 0, (3, 27))
    homer = Entity(71, 15, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
    return homer


def get_mayor():

    dialogue = get_mayor_dialogue()
    noncom = Noncombatant('Mayor', DANIB.get('mayor'), dialogue)
    age = Age(48, 2, 16, 0, (10, 15))
    mayor = Entity(49, 10, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
    return mayor


def get_innkeeper():

    dialogue = get_innkeeper_dialogue()
    noncom = Noncombatant('Innkeeper', DANIB.get('innkeeper'), dialogue)
    age = Age(42, 11, 25, 0, (1, 6))
    innkeeper = Entity(78, 47, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
    return innkeeper


def get_tavernkeeper():
    dialogue = get_tavernkeeper_dialogue()
    noncom = Noncombatant('Tavernkeeper', DANIB.get('tavernkeeper'), dialogue)
    age = Age(31, 5, 20, 0, (7, 11))
    tavernkeeper = Entity(80, 55, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
    return tavernkeeper

