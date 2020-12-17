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
    def equipment_slots(self):
        return [self.head, self.shoulders, self.chest, self.arms, self.wrists, self.hands, self.legs, self.feet,
                self.face, self.neck, self.back, self.waist, self.finger1, self.finger2, self.satchel, self.main_hand,
                self.off_hand, self.quiver, self.food, self.drink]

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

    def toggle_equip(self, equippable_entity):
        results = []
        
        slot = equippable_entity.item.equippable.slot
        
        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})
                    
                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': equippable_entity})
                    
                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.HEAD:
            if self.head == equippable_entity:
                self.head = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.head:
                    results.append({'dequipped': equippable_entity})
                    
                self.head = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.BODY:
            if self.body == equippable_entity:
                self.body = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.body:
                    results.append({'dequipped': equippable_entity})
                    
                self.body = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.FEET:
            if self.feet == equippable_entity:
                self.feet = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.feet:
                    results.append({'dequipped': equippable_entity})
                    
                self.feet = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.BELT:
            if self.belt == equippable_entity:
                self.belt = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.belt:
                    results.append({'dequipped': equippable_entity})
                    
                self.feet = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.HANDS:
            if self.hands == equippable_entity:
                self.hands = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.hands:
                    results.append({'dequipped': equippable_entity})
                    
                self.hands = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.FINGER:
            if self.finger == equippable_entity:
                self.finger = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.finger:
                    results.append({'dequipped': equippable_entity})
                    
                self.finger = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.NECK:
            if self.neck == equippable_entity:
                self.neck = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.neck:
                    results.append({'dequipped': equippable_entity})
                    
                self.neck = equippable_entity
                results.append({'equipped': equippable_entity})
                
        elif slot == EquipmentSlots.BACK:
            if self.back == equippable_entity:
                self.back = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.back:
                    results.append({'dequipped': equippable_entity})
                    
                self.back = equippable_entity
                results.append({'equipped': equippable_entity})

        return results

    def drop_dead(self):
        drop = [item for item in (self.main_hand, self.off_hand, self.head, self.body, self.feet, self.belt, self.hands,
                                  self.finger, self.neck, self.back) if item is not None]
        return drop
