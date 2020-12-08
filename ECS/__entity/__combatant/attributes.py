class Attributes:
    """Contains the 10 primary stats and their base derivatives."""

    def __init__(self, strength=0, instinct=0, coordination=0, endurance=0, arcana=0, improvisation=0, wisdom=0,
                 finesse=0, charisma=0, devotion=0):
        self.strength = strength
        self.instinct = instinct
        self.coordination = coordination
        self.endurance = endurance
        self.arcana = arcana
        self.improvisation = improvisation
        self.wisdom = wisdom
        self.finesse = finesse
        self.charisma = charisma
        self.devotion = devotion
        self.current_hp = (20 * (self.strength + self.strength + self.instinct + self.coordination + self.endurance))
        self.current_mp = (20 * (self.arcana + self.arcana + self.instinct + self.improvisation + self.wisdom))
        self.current_tp = (20 * (self.finesse + self.finesse + self.coordination + self.improvisation + self.charisma))
        self.current_vp = (20 * (self.devotion + self.devotion + self.endurance + self.wisdom + self.charisma))

    # Base maximum resource functions
    @property
    def base_max_hp(self):
        return 20 * (self.strength + self.strength + self.instinct + self.coordination + self.endurance)

    @property
    def base_max_mp(self):
        return 20 * (self.arcana + self.arcana + self.instinct + self.improvisation + self.wisdom)

    @property
    def base_max_tp(self):
        return 20 * (self.finesse + self.finesse + self.coordination + self.improvisation + self.charisma)

    @property
    def base_max_vp(self):
        return 20 * (self.devotion + self.devotion + self.endurance + self.wisdom + self.charisma)

    # Base Primary Stats

    @property
    def base_power_slash(self):
        return self.strength

    @property
    def base_power_pierce(self):
        return self.strength

    @property
    def base_power_blunt(self):
        return self.strength

    @property
    def base_power_heat(self):
        return self.arcana

    @property
    def base_power_cold(self):
        return self.arcana

    @property
    def base_power_acid(self):
        return self.arcana

    @property
    def base_power_current(self):
        return self.arcana

    @property
    def base_power_aether(self):
        return self.devotion

    @property
    def base_resist_slash(self):
        return self.endurance

    @property
    def base_resist_pierce(self):
        return self.endurance

    @property
    def base_resist_blunt(self):
        return self.endurance

    @property
    def base_resist_heat(self):
        return self.endurance + self.arcana

    @property
    def base_resist_cold(self):
        return self.endurance + self.arcana

    @property
    def base_resist_acid(self):
        return self.endurance + self.arcana

    @property
    def base_resist_current(self):
        return self.endurance + self.arcana

    @property
    def base_resist_aether(self):
        return self.endurance + self.devotion

    # Base Secondary Stats

    @property
    def base_initiative(self):
        return int((3*self.instinct + self.improvisation)/2)

    @property
    def base_speed(self):
        return int(((4*self.finesse) + (2*self.coordination))/3)

    @property
    def base_accuracy(self):
        return int(self.coordination + self.finesse)

    @property
    def base_dodge(self):
        return int(((5*self.finesse) + (2*self.instinct) + self.improvisation)/4)

    @property
    def base_critical_strike(self):
        return int(self.finesse + self.instinct)

    @property
    def base_critical_damage(self):
        return int(self.finesse + self.strength)

    @property
    def base_presence(self):
        return int(2*self.strength)

    @property
    def base_teamwork(self):
        return int(2*self.coordination)

    # Base Saving Throws

    @property
    def base_savethrow_injury(self):
        return int(self.endurance + ((2 * self.coordination + self.strength) / 3))

    @property
    def base_savethrow_illness(self):
        return int(2 * self.endurance)

    @property
    def base_savethrow_tenacity(self):
        return int(self.arcana + (2 * self.instinct + self.endurance)/3)

    @property
    def base_savethrow_apathy(self):
        return int((4 * self.devotion + self.charisma + self.endurance)/3)

    @property
    def base_savethrow_composure(self):
        return int(((3 * (self.charisma + self.wisdom)) + (2 * self.endurance))/4)

    @property
    def base_savethrow_pain(self):
        return int(((3 * self.endurance) + self.wisdom) / 2)

    @property
    def base_savethrow_cognition(self):
        return int((3 * (self.coordination + self.wisdom) + self.endurance + self.arcana)/4)

    @property
    def base_savethrow_force(self):
        return int(self.strength + (self.endurance + self.improvisation)/2)

    @property
    def base_savethrow_breath(self):
        return int((3 * self.endurance + self.instinct)/2)

    @property
    def base_savethrow_reflex(self):
        return int(2 * self.finesse)

    @property
    def base_savethrow_corruption(self):
        return int(self.devotion + (self.charisma + self.wisdom)/2)

    @property
    def base_savethrow_will(self):
        return int(self.arcana + self.wisdom)
