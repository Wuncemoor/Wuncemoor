from ECS.entity import Entity
from ECS.__entity.item import Item
from ECS.__entity.__item.useable import Useable
from ECS.__entity.__item.equippable import Equippable
from ECS.__entity.__item.__equippable.equippable_core import EquippableCore
from ECS.__entity.__item.__equippable.equippable_quality import EquippableQuality
from ECS.__entity.__item.__equippable.equippable_material import EquippableMaterial
from handlers.views.messages import Message
from enums.render_order import RenderOrder
from enums.equipment_slots import EquipmentSlots
from item_functions import heal, cast_fireball, cast_confuse, cast_lightning
import tcod as libtcod
from config.image_objects import BUNDLE_WEAPONS, BUNDLE_POTION, SCROLL


def make_item(item_choice):

    if item_choice == 'healing_potion':

        item_component = Item(
            useable=Useable('Healing Potion', BUNDLE_POTION, use_function=heal, amount=400))
        item = Entity(0, 0, render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'sword':
        image = BUNDLE_WEAPONS.get('longsword')
        equippable_core = EquippableCore('longsword', image)
        equippable_material = EquippableMaterial('wood')
        equippable_quality = EquippableQuality('average')

        equippable_component = Equippable('Sword', image, EquipmentSlots.MAIN_HAND, equippable_core,
                                          equippable_material, equippable_quality)
        item_component = Item(equippable_component)
        item = Entity(0, 0, item=item_component)
    elif item_choice == 'shield':
        image = BUNDLE_WEAPONS.get('shield')
        equippable_core = EquippableCore('shield', image)
        equippable_material = EquippableMaterial('iron')
        equippable_quality = EquippableQuality('average')

        equippable_component = Equippable('Shield', image, EquipmentSlots.OFF_HAND, equippable_core,
                                          equippable_material, equippable_quality)
        item_component = Item(equippable_component)
        item = Entity(0, 0, item=item_component)
    elif item_choice == 'fireball_scroll':
        image = SCROLL
        msg = 'Left-click a target tile for the fireball, or right-click to rethink your life decisions.'
        item_component = Item(
            useable=Useable('Fireball Scroll', image, use_function=cast_fireball, targeting=True,
                                      targeting_message=Message(msg, libtcod.light_cyan), damage=250, radius=3))
        item = Entity(0, 0, render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'confusion_scroll':
        image = SCROLL
        item_component = Item(
            useable=Useable('Confusion Scroll', image, use_function=cast_confuse, targeting=True,
                                      targeting_message=Message(
                                          'Left-click an enemy to confuse it, or right-click to cancel.',
                                          libtcod.light_cyan)))
        item = Entity(0, 0, render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'lightning_scroll':
        image = SCROLL
        item_component = Item(
            useable=Useable('Lightning Scroll', image, use_function=cast_lightning, damage=400,
                                      maximum_range=5))
        item = Entity(0, 0, render_order=RenderOrder.ITEM, item=item_component)

    return item
