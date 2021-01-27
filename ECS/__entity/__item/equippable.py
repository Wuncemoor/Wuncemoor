import math

from ECS.__entity.__item.__equippable.equippable_core import EquippableCore
from ECS.__entity.__item.__equippable.equippable_material import EquippableMaterial
from ECS.__entity.__item.__equippable.equippable_quality import EquippableQuality


class Equippable:
    """Component for Items to be worn, providing bonuses to the wearer."""
    def __init__(self, name=None, images=None, slot=None, core: EquippableCore = None,
                 material: EquippableMaterial = None, quality: EquippableQuality = None, *modifiers):
        self.name = name
        self.images = images
        self.slot = slot
        self.core = core
        self.material = material
        self.quality = quality

    @property
    def mass(self):
        return self.core.mass_modifier * self.material.mass_modifier
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
    def power_heat_bonus(self):
        return math.floor(self.core.spirit_bonuses[0] * self.modifier)

    @property
    def power_cold_bonus(self):
        return math.floor(self.core.spirit_bonuses[1] * self.modifier)

    @property
    def power_acid_bonus(self):
        return math.floor(self.core.spirit_bonuses[2] * self.modifier)

    @property
    def power_current_bonus(self):
        return math.floor(self.core.spirit_bonuses[3] * self.modifier)

    @property
    def power_aether_bonus(self):
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
    def initiative_bonus(self):
        return math.floor(self.core.initiative_bonus * self.modifier)

    @property
    def speed_bonus(self):
        return math.floor(self.core.speed_bonus * self.modifier)

    @property
    def critical_strike_bonus(self):
        return math.floor(self.core.critical_strike_bonus * self.modifier)

    @property
    def critical_damage_bonus(self):
        return math.floor(self.core.critical_damage_bonus * self.modifier)

    @property
    def presence_bonus(self):
        return math.floor(self.core.presence_bonus * self.modifier)

    @property
    def teamwork_bonus(self):
        return math.floor(self.core.teamwork_bonus * self.modifier)

    @property
    def savethrow_injury_bonus(self):
        return math.floor(self.core.savethrow_injury_bonus * self.modifier)

    @property
    def savethrow_illness_bonus(self):
        return math.floor(self.core.savethrow_illness_bonus * self.modifier)

    @property
    def savethrow_tenacity_bonus(self):
        return math.floor(self.core.savethrow_tenacity_bonus * self.modifier)

    @property
    def savethrow_apathy_bonus(self):
        return math.floor(self.core.savethrow_apathy_bonus * self.modifier)

    @property
    def savethrow_composure_bonus(self):
        return math.floor(self.core.savethrow_composure_bonus * self.modifier)

    @property
    def savethrow_pain_bonus(self):
        return math.floor(self.core.savethrow_pain_bonus * self.modifier)

    @property
    def savethrow_cognition_bonus(self):
        return math.floor(self.core.savethrow_cognition_bonus * self.modifier)

    @property
    def savethrow_force_bonus(self):
        return math.floor(self.core.savethrow_force_bonus * self.modifier)

    @property
    def savethrow_breath_bonus(self):
        return math.floor(self.core.savethrow_breath_bonus * self.modifier)

    @property
    def savethrow_reflex_bonus(self):
        return math.floor(self.core.savethrow_reflex_bonus * self.modifier)

    @property
    def savethrow_corruption_bonus(self):
        return math.floor(self.core.savethrow_corruption_bonus * self.modifier)

    @property
    def savethrow_will_bonus(self):
        return math.floor(self.core.savethrow_will_bonus * self.modifier)

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
