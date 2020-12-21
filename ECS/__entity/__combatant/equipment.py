from enums.equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, quiver=None, head=None, shoulders=None, chest=None, arms=None,
                 wrists=None, hands=None, legs=None, feet=None, face=None, neck=None, back=None, waist=None,
                 finger1=None, finger2=None, satchel=None, food=None, drink=None):
        self.head = head
        self.shoulders = shoulders
        self.chest = chest
        self.arms = arms
        self.wrists = wrists
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.face = face
        self.neck = neck
        self.back = back
        self.waist = waist
        self.finger1 = finger1
        self.finger2 = finger2
        self.satchel = satchel
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.quiver = quiver
        self.food = food
        self.drink = drink

    @property
    def mass(self):
        return sum([slot.mass for slot in self.equipment_slots if slot is not None])

    @property
    def equipment_slots(self):
        return [self.head, self.shoulders, self.chest, self.arms, self.wrists, self.hands, self.legs, self.feet,
                self.face, self.neck, self.back, self.waist, self.finger1, self.finger2, self.satchel, self.main_hand,
                self.off_hand, self.quiver, self.food, self.drink]

    @property
    def slots_dict(self):
        return {EquipmentSlots.HEAD: self.head, EquipmentSlots.SHOULDERS: self.shoulders,
                EquipmentSlots.CHEST: self.chest, EquipmentSlots.ARMS: self.arms,
                EquipmentSlots.HANDS: self.hands, EquipmentSlots.LEGS: self.legs,
                EquipmentSlots.FEET: self.feet, EquipmentSlots.FACE: self.face,
                EquipmentSlots.NECK: self.neck, EquipmentSlots.BACK: self.back,
                EquipmentSlots.WAIST: self.waist, EquipmentSlots.FINGER1: self.finger1,
                EquipmentSlots.FINGER2: self.finger2, EquipmentSlots.SATCHEL: self.satchel,
                EquipmentSlots.MAIN_HAND: self.main_hand, EquipmentSlots.OFF_HAND: self.off_hand,
                EquipmentSlots.QUIVER: self.quiver, EquipmentSlots.FOOD: self.food,
                EquipmentSlots.DRINK: self.drink}

    @property
    def max_hp_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.max_hp_bonus
        return bonus
        
    @property
    def max_mp_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.max_mp_bonus
        return bonus

    @property
    def max_tp_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.max_tp_bonus
        return bonus

    @property
    def max_vp_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.max_vp_bonus
        return bonus
        
    @property
    def power_slash_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_slash_bonus
        return bonus

    @property
    def power_pierce_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_pierce_bonus
        return bonus
        
    @property
    def power_blunt_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_blunt_bonus
        return bonus
        
    @property
    def power_heat_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_heat_bonus
        return bonus


    @property
    def power_cold_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_cold_bonus
        return bonus
        
    @property
    def power_acid_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_acid_bonus
        return bonus
        
    @property
    def power_current_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_current_bonus
        return bonus
        
    @property
    def power_aether_bonus(self):
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.power_aether_bonus
        return bonus
        
    @property
    def resist_slash_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_slash_bonus
        return bonus

    @property
    def resist_pierce_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_pierce_bonus
        return bonus
        
    @property
    def resist_blunt_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_blunt_bonus
        return bonus

    @property
    def resist_heat_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_heat_bonus
        return bonus

    @property
    def resist_cold_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_cold_bonus
        return bonus

    @property
    def resist_acid_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_acid_bonus
        return bonus

    @property
    def resist_current_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_current_bonus
        return bonus

    @property
    def resist_aether_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.resist_aether_bonus
        return bonus

    @property
    def accuracy_bonus(self):
    
        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.accuracy_bonus
        return bonus

    @property
    def dodge_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.dodge_bonus
        return bonus

    @property
    def initiative_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.initiative_bonus
        return bonus

    @property
    def speed_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.speed_bonus
        return bonus

    @property
    def critical_strike_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.critical_strike_bonus
        return bonus

    @property
    def critical_damage_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.critical_damage_bonus
        return bonus

    @property
    def presence_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.presence_bonus
        return bonus

    @property
    def teamwork_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.teamwork_bonus
        return bonus

    @property
    def savethrow_injury_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_injury_bonus
        return bonus

    @property
    def savethrow_illness_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_illness_bonus
        return bonus

    @property
    def savethrow_tenacity_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_tenacity_bonus
        return bonus

    @property
    def savethrow_apathy_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_apathy_bonus
        return bonus

    @property
    def savethrow_composure_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_composure_bonus
        return bonus

    @property
    def savethrow_pain_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_pain_bonus
        return bonus

    @property
    def savethrow_cognition_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_cognition_bonus
        return bonus

    @property
    def savethrow_force_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_force_bonus
        return bonus

    @property
    def savethrow_breath_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_breath_bonus
        return bonus

    @property
    def savethrow_reflex_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_reflex_bonus
        return bonus

    @property
    def savethrow_corruption_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_corruption_bonus
        return bonus

    @property
    def savethrow_will_bonus(self):

        bonus = 0
        for slot in self.equipment_slots:
            if slot is not None:
                bonus += slot.item.equippable.savethrow_will_bonus
        return bonus

    def unequip(self, slot):
        slot_gear = self.slots_dict.get(slot)
        added_to_inventory = slot_gear
        if slot == EquipmentSlots.HEAD:
            self.head = None
        elif slot == EquipmentSlots.SHOULDERS:
            self.shoulders = None
        elif slot == EquipmentSlots.CHEST:
            self.chest = None
        elif slot == EquipmentSlots.ARMS:
            self.arms = None
        elif slot == EquipmentSlots.HANDS:
            self.hands = None
        elif slot == EquipmentSlots.LEGS:
            self.legs = None
        elif slot == EquipmentSlots.FEET:
            self.feet = None
        elif slot == EquipmentSlots.FACE:
            self.face = None
        elif slot == EquipmentSlots.NECK:
            self.neck = None
        elif slot == EquipmentSlots.BACK:
            self.back = None
        elif slot == EquipmentSlots.WAIST:
            self.waist = None
        elif slot == EquipmentSlots.FINGER1:
            self.finger1 = None
        elif slot == EquipmentSlots.FINGER2:
            self.finger2 = None
        elif slot == EquipmentSlots.SATCHEL:
            self.satchel = None
        elif slot == EquipmentSlots.MAIN_HAND:
            self.main_hand = None
        elif slot == EquipmentSlots.OFF_HAND:
            self.off_hand = None
        elif slot == EquipmentSlots.QUIVER:
            self.quiver = None
        elif slot == EquipmentSlots.FOOD:
            self.food = None
        elif slot == EquipmentSlots.DRINK:
            self.drink = None

        return added_to_inventory

    def equip(self, entity):
        slot = entity.item.equippable.slot
        if slot == EquipmentSlots.HEAD:
            self.head = entity
        elif slot == EquipmentSlots.SHOULDERS:
            self.shoulders = entity
        elif slot == EquipmentSlots.CHEST:
            self.chest = entity
        elif slot == EquipmentSlots.ARMS:
            self.arms = entity
        elif slot == EquipmentSlots.HANDS:
            self.hands = entity
        elif slot == EquipmentSlots.LEGS:
            self.legs = entity
        elif slot == EquipmentSlots.FEET:
            self.feet = entity
        elif slot == EquipmentSlots.FACE:
            self.face = entity
        elif slot == EquipmentSlots.NECK:
            self.neck = entity
        elif slot == EquipmentSlots.BACK:
            self.back = entity
        elif slot == EquipmentSlots.WAIST:
            self.waist = entity
        elif slot == EquipmentSlots.FINGER1:
            self.finger1 = entity
        elif slot == EquipmentSlots.FINGER2:
            self.finger2 = entity
        elif slot == EquipmentSlots.SATCHEL:
            self.satchel = entity
        elif slot == EquipmentSlots.MAIN_HAND:
            self.main_hand = entity
        elif slot == EquipmentSlots.OFF_HAND:
            self.off_hand = entity
        elif slot == EquipmentSlots.QUIVER:
            self.quiver = entity
        elif slot == EquipmentSlots.FOOD:
            self.food = entity
        elif slot == EquipmentSlots.DRINK:
            self.drink = entity

    def drop_dead(self):
        drop = [item for item in self.equipment_slots if item is not None]
        return drop
