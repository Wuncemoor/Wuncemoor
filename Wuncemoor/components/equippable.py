from equipment_slots import EquipmentSlots
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.item import Item
import math


class Equippable:
    def __init__(self, name=None, image=None, slot=None, core=None, material=None, quality=None, *modifiers):
        self.name = name
        self.image = image
        self.slot = slot
        self.core = core
        self.material = material
        self.quality = quality
        
    @property
    def max_hp_bonus(self):
       return math.floor(self.core.resource_bonuses[0])
    @property
    def max_mp_bonus(self):
        return math.floor(self.core.resource_bonuses[1] * self.modifier)
    @property
    def max_tp_bonus(self):
        return math.floor(self.core.resource_bonuses[2] * self.modifier)
    @property
    def max_vp_bonus(self): 
        return math.floor(self.core.resource_bonuses[3] * self.modifier)
    @property
    def power_slash_bonus(self):
        return math.floor(self.core.power_bonuses[0] * self.modifier)
    @property
    def power_pierce_bonus(self): 
        return math.floor(self.core.power_bonuses[1] * self.modifier)
    @property
    def power_blunt_bonus(self):
        return math.floor(self.core.power_bonuses[2] * self.modifier)
    @property
    def spirit_heat_bonus(self):
        return math.floor(self.core.spirit_bonuses[0] * self.modifier)
    @property
    def spirit_cold_bonus(self):
        return math.floor(self.core.spirit_bonuses[1] * self.modifier)
    @property
    def spirit_acid_bonus(self):
        return math.floor(self.core.spirit_bonuses[2] * self.modifier)
    @property
    def spirit_current_bonus(self):
        return math.floor(self.core.spirit_bonuses[3] * self.modifier)
    @property
    def spirit_aether_bonus(self):
        return math.floor(self.core.spirit_bonuses[4] * self.modifier)
    @property
    def resist_slash_bonus(self):
        return math.floor(self.core.resist_phys_bonuses[0] * self.modifier)
    @property
    def resist_pierce_bonus(self):
        return math.floor(self.core.resist_phys_bonuses[1] * self.modifier)
    @property
    def resist_blunt_bonus(self):
        return math.floor(self.core.resist_phys_bonuses[2] * self.modifier)
    @property
    def resist_heat_bonus(self):
        return math.floor(self.core.resist_ele_bonuses[0] * self.modifier)
    @property
    def resist_cold_bonus(self):
        return math.floor(self.core.resist_ele_bonuses[1] * self.modifier)
    @property
    def resist_acid_bonus(self):
        return math.floor(self.core.resist_ele_bonuses[2] * self.modifier)
    @property
    def resist_current_bonus(self):
        return math.floor(self.core.resist_ele_bonuses[3] * self.modifier)
    @property
    def resist_aether_bonus(self):
        return math.floor(self.core.resist_ele_bonuses[4] * self.modifier)
    @property
    def accuracy_bonus(self):
        return math.floor(self.core.hit_dodge_bonuses[0] * self.modifier)
    @property
    def dodge_bonus(self):
        return math.floor(self.core.hit_dodge_bonuses[1] * self.modifier)
    @property
    def node_value(self):
        return math.floor(self.core.values[0] * self.modifier)
    @property
    def price(self):
        return math.floor(self.core.values[1] * self.modifier)
    
    @property
    def modifier(self):
        modifier = 0
        if self.material and self.quality:
            modifier = self.material.modifier * self.quality.modifier
        return modifier
        
    def set_name(self, name):
        core = self.core.core.capitalize()
        material = self.material.material.capitalize()
        quality = self.quality.quality.capitalize()
        
        self.name = quality + ' ' + material + ' ' + core
        
    
    def set_image(self, image):
        self.image = image
        
    def set_core(self,core):
        self.core = core
        
    def set_material(self, material):
        self.material = material
        
    def set_quality(self, quality):
        self.quality = quality
        
    def set_slot(self, slot):
        self.slot = slot


def get_equippable(input):

    if input == 'stick':
        item_component = Item(Equippable('Stick', '-', EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'), EquippableQuality('average')))
    if input == 'stone_dagger':
        item_component = Item(Equippable('Stone Dagger', '-', EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('stone'), EquippableQuality('average')))
    if input == 'bone_dagger':
        item_component = Item(Equippable('Bone Dagger', '-', EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('bone'), EquippableQuality('average')))
    if input =='copper_dagger':
        item_component = Item(Equippable('Copper Dagger', '-', EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('copper'), EquippableQuality('average')))
    if input == 'bronze_dagger':
        item_component = Item(Equippable('Bronze Dagger', '-', EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('bronze'), EquippableQuality('average')))
    if input == 'rusty_iron_longsword':
        item_component = Item(Equippable('Rusty Iron Longsword', '-', EquipmentSlots.MAIN_HAND, EquippableCore('sword'), EquippableMaterial('iron'), EquippableQuality('rusty')))

    return equippable_component