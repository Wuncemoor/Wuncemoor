import math


class Equippable:
    def __init__(self, name=None, images=None, slot=None, core=None, material=None, quality=None, *modifiers):
        self.name = name
        self.images = images
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
