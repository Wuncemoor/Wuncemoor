from equipment_slots import EquipmentSlots
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
import math

class Equippable:
    def __init__(self, slot, core, material, quality, *modifiers):
        self.slot = slot
        self.core = core
        self.material = material
        self.quality = quality
        self.modifier = self.material.modifier * self.quality.modifier
        
        self.max_hp_bonus = math.floor(self.core.resource_bonuses[0] * self.modifier)
        self.max_mp_bonus = math.floor(self.core.resource_bonuses[1] * self.modifier)
        self.max_tp_bonus = math.floor(self.core.resource_bonuses[2] * self.modifier)
        self.max_vp_bonus = math.floor(self.core.resource_bonuses[3] * self.modifier)
        
        self.power_slash_bonus = math.floor(self.core.power_bonuses[0] * self.modifier)
        self.power_pierce_bonus = math.floor(self.core.power_bonuses[1] * self.modifier)
        self.power_blunt_bonus = math.floor(self.core.power_bonuses[2] * self.modifier)
        
        self.spirit_heat_bonus = math.floor(self.core.spirit_bonuses[0] * self.modifier)
        self.spirit_cold_bonus = math.floor(self.core.spirit_bonuses[1] * self.modifier)
        self.spirit_acid_bonus = math.floor(self.core.spirit_bonuses[2] * self.modifier)
        self.spirit_current_bonus = math.floor(self.core.spirit_bonuses[3] * self.modifier)
        self.spirit_aether_bonus = math.floor(self.core.spirit_bonuses[4] * self.modifier)
        
        self.resist_slash_bonus = math.floor(self.core.resist_phys_bonuses[0] * self.modifier)
        self.resist_pierce_bonus = math.floor(self.core.resist_phys_bonuses[1] * self.modifier)
        self.resist_blunt_bonus = math.floor(self.core.resist_phys_bonuses[2] * self.modifier)
        
        self.resist_heat_bonus = math.floor(self.core.resist_ele_bonuses[0] * self.modifier)
        self.resist_cold_bonus = math.floor(self.core.resist_ele_bonuses[1] * self.modifier)
        self.resist_acid_bonus = math.floor(self.core.resist_ele_bonuses[2] * self.modifier)
        self.resist_current_bonus = math.floor(self.core.resist_ele_bonuses[3] * self.modifier)
        self.resist_aether_bonus = math.floor(self.core.resist_ele_bonuses[4] * self.modifier)
        
        self.accuracy_bonus = math.floor(self.core.hit_dodge_bonuses[0] * self.modifier)
        self.dodge_bonus = math.floor(self.core.hit_dodge_bonuses[1] * self.modifier)
        
        self.node_value = math.floor(self.core.values[0] * self.modifier)
        self.price = math.floor(self.core.values[1] * self.modifier)
        
        
def get_equippable(input):

    if input == 'stick':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'), EquippableQuality('average'))
    if input == 'stone_dagger':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('stone'), EquippableQuality('average'))
    if input == 'bone_dagger':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('bone'), EquippableQuality('average'))
    if input =='copper_dagger':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('copper'), EquippableQuality('average'))
    if input == 'bronze_dagger':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('dagger'), EquippableMaterial('bronze'), EquippableQuality('average'))
    if input == 'rusty_iron_longsword':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, EquippableCore('sword'), EquippableMaterial('iron'), EquippableQuality('rusty'))

    return equippable_component