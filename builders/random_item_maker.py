from ECS.__entity.__item.equippable import Equippable
from ECS.__entity.__item.__equippable.equippable_core import EquippableCore
from ECS.__entity.__item.__equippable.equippable_material import EquippableMaterial
from ECS.__entity.__item.__equippable.equippable_quality import EquippableQuality
from enums.equipment_slots import EquipmentSlots
import random
from config.image_objects import BUNDLE_WEAPONS


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_equippable(self):
        equippable = Equippable()

        core = self.__builder.get_core()
        equippable.core = core

        equippable.material = self.__builder.get_material()

        equippable.quality = self.__builder.get_quality()

        equippable.slot = self.__builder.get_slot()

        name = self.__builder.get_name()
        equippable.set_name(name)

        image = self.__builder.get_image(core)
        equippable.images = image

        return equippable


class EquippableBuilder:

    def __init__(self, node_power):
        self.node_power = node_power

    def get_name(self):
        return 'test item'

    def get_image(self, core):

        return core.image

    def get_quality(self):

        chance = random.randint(1, 20)
        if chance == 1:
            q = EquippableQuality('rusty')
            return q
        elif chance < 20:
            q = EquippableQuality('average')
            return q
        else:
            q = EquippableQuality('fine')
            return q

    def get_material(self):

        if self.node_power < 10:
            m = EquippableMaterial('wood')
            return m
        elif self.node_power < 25:
            m = EquippableMaterial('stone')
            return m
        elif self.node_power < 50:
            m = EquippableMaterial('bone')
            return m
        elif self.node_power < 100:
            m = EquippableMaterial('copper')
            return m
        elif self.node_power < 250:
            m = EquippableMaterial('bronze')
            return m
        elif self.node_power < 500:
            m = EquippableMaterial('iron')
            return m

    def get_core(self):

        options = ['staff', 'dagger', 'shield']
        c = random.choice(options)
        return EquippableCore(c, BUNDLE_WEAPONS.get(c))

    def get_slot(self):

        return EquipmentSlots.MAIN_HAND
