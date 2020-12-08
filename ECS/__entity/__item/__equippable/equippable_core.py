class EquippableCore:
    """Equippable component representing most of the Equipment piece, other than Quality/Material"""

    def __init__(self, core, obj):
        self.core = core
        self.image = obj
        self.resource_bonuses = [0, 0, 0, 0]
        self.power_bonuses = [0, 0, 0]
        self.spirit_bonuses = [0, 0, 0, 0, 0]
        self.resist_phys_bonuses = [0, 0, 0]
        self.resist_ele_bonuses = [0, 0, 0, 0, 0]
        self.hit_dodge_bonuses = [0, 0]
        self.initiative_bonus = 0
        self.speed_bonus = 0
        self.critical_strike_bonus = 0
        self.critical_damage_bonus = 0
        self.presence_bonus = 0
        self.teamwork_bonus = 0
        self.savethrow_injury_bonus = 0
        self.savethrow_illness_bonus = 0
        self.savethrow_tenacity_bonus = 0
        self.savethrow_apathy_bonus = 0
        self.savethrow_composure_bonus = 0
        self.savethrow_pain_bonus = 0
        self.savethrow_cognition_bonus = 0
        self.savethrow_force_bonus = 0
        self.savethrow_breath_bonus = 0
        self.savethrow_reflex_bonus = 0
        self.savethrow_corruption_bonus = 0
        self.savethrow_will_bonus = 0
        self.values = [0, 0]

        if self.core == 'staff':

            self.resource_bonuses = [0, 0, 0, 0]
            self.power_bonuses = [0, 0, 32]
            self.spirit_bonuses = [0, 0, 0, 0, 0]
            self.resist_phys_bonuses = [0, 0, 0]
            self.resist_ele_bonuses = [0, 0, 0, 0, 0]
            self.hit_dodge_bonuses = [0, 0]
            self.values = [0, 0]

        elif self.core == 'dagger':

            self.resource_bonuses = [0, 0, 0, 0]
            self.power_bonuses = [6, 10, 0]
            self.spirit_bonuses = [0, 0, 0, 0, 0]
            self.resist_phys_bonuses = [0, 0, 0]
            self.resist_ele_bonuses = [0, 0, 0, 0, 0]
            self.hit_dodge_bonuses = [5, 0]
            self.values = [0, 0]

        elif self.core == 'longsword':

            self.resource_bonuses = [0, 0, 0, 0]
            self.power_bonuses = [32, 6, 0]
            self.spirit_bonuses = [0, 0, 0, 0, 0]
            self.resist_phys_bonuses = [0, 0, 0]
            self.resist_ele_bonuses = [0, 0, 0, 0, 0]
            self.hit_dodge_bonuses = [5, 0]
            self.values = [0, 0]

        elif self.core == 'shield':

            self.resource_bonuses = [0, 0, 0, 0]
            self.power_bonuses = [0, 0, 0]
            self.spirit_bonuses = [0, 0, 0, 0, 0]
            self.resist_phys_bonuses = [15, 15, 15]
            self.resist_ele_bonuses = [5, 5, 5, 5, 0]
            self.hit_dodge_bonuses = [5, 0]
            self.values = [0, 0]
