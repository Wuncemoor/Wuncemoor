from enums.equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, body=None, feet=None, belt=None, hands=None,
                 finger=None, neck=None, back=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.body = body
        self.feet = feet
        self.belt = belt
        self.hands = hands
        self.finger = finger
        self.neck = neck
        self.back = back

    @property
    def max_hp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.max_hp_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.max_hp_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.max_hp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.max_hp_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.max_hp_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.max_hp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.max_hp_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.max_hp_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.max_hp_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.max_hp_bonus
            
        return bonus
        
    @property
    def max_mp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.max_mp_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.max_mp_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.max_mp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.max_mp_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.max_mp_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.max_mp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.max_mp_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.max_mp_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.max_mp_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.max_mp_bonus

        return bonus

    @property
    def max_tp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.max_tp_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.max_tp_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.max_tp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.max_tp_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.max_tp_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.max_tp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.max_tp_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.max_tp_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.max_tp_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.max_tp_bonus

        return bonus

    @property
    def max_vp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.max_vp_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.max_vp_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.max_vp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.max_vp_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.max_vp_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.max_vp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.max_vp_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.max_vp_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.max_vp_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.max_vp_bonus

        return bonus
        
    @property
    def power_slash_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.power_slash_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.power_slash_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.power_slash_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.power_slash_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.power_slash_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.power_slash_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.power_slash_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.power_slash_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.power_slash_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.power_slash_bonus

        return bonus

    @property
    def power_pierce_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.power_pierce_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.power_pierce_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.power_pierce_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.power_pierce_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.power_pierce_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.power_pierce_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.power_pierce_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.power_pierce_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.power_pierce_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.power_pierce_bonus

        return bonus
        
    @property
    def power_blunt_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.power_blunt_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.power_blunt_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.power_blunt_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.power_blunt_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.power_blunt_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.power_blunt_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.power_blunt_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.power_blunt_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.power_blunt_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.power_blunt_bonus

        return bonus
        
    @property
    def spirit_heat_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.spirit_heat_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.spirit_heat_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.spirit_heat_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.spirit_heat_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.spirit_heat_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.spirit_heat_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.spirit_heat_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.spirit_heat_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.spirit_heat_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.spirit_heat_bonus

        return bonus
       
    @property
    def spirit_cold_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.spirit_cold_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.spirit_cold_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.spirit_cold_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.spirit_cold_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.spirit_cold_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.spirit_cold_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.spirit_cold_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.spirit_cold_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.spirit_cold_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.spirit_cold_bonus

        return bonus
        
    @property
    def spirit_acid_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.spirit_acid_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.spirit_acid_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.spirit_acid_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.spirit_acid_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.spirit_acid_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.spirit_acid_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.spirit_acid_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.spirit_acid_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.spirit_acid_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.spirit_acid_bonus

        return bonus
        
    @property
    def spirit_current_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.spirit_current_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.spirit_current_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.spirit_current_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.spirit_current_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.spirit_current_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.spirit_current_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.spirit_current_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.spirit_current_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.spirit_current_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.spirit_current_bonus

        return bonus
        
    @property
    def spirit_aether_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.spirit_aether_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.spirit_aether_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.spirit_aether_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.spirit_aether_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.spirit_aether_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.spirit_aether_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.spirit_aether_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.spirit_aether_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.spirit_aether_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.spirit_aether_bonus

        return bonus
        
    @property
    def resist_slash_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_slash_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_slash_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_slash_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_slash_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_slash_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_slash_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_slash_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_slash_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_slash_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_slash_bonus

        return bonus

    @property
    def resist_pierce_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_pierce_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_pierce_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_pierce_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_pierce_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_pierce_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_pierce_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_pierce_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_pierce_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_pierce_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_pierce_bonus

        return bonus
        
    @property
    def resist_blunt_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_blunt_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_blunt_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_blunt_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_blunt_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_blunt_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_blunt_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_blunt_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_blunt_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_blunt_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_blunt_bonus

        return bonus

    @property
    def resist_heat_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_heat_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_heat_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_heat_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_heat_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_heat_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_heat_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_heat_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_heat_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_heat_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_heat_bonus

        return bonus

    @property
    def resist_cold_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_cold_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_cold_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_cold_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_cold_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_cold_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_cold_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_cold_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_cold_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_cold_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_cold_bonus

        return bonus

    @property
    def resist_acid_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_acid_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_acid_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_acid_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_acid_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_acid_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_acid_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_acid_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_acid_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_acid_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_acid_bonus

        return bonus

    @property
    def resist_current_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_current_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_current_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_current_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_current_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_current_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_current_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_current_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_current_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_current_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_current_bonus

        return bonus

    @property
    def resist_aether_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.resist_aether_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.resist_aether_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.resist_aether_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.resist_aether_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.resist_aether_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.resist_aether_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.resist_aether_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.resist_aether_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.resist_aether_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.resist_aether_bonus

        return bonus

    @property
    def accuracy_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.accuracy_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.accuracy_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.accuracy_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.accuracy_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.accuracy_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.accuracy_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.accuracy_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.accuracy_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.accuracy_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.accuracy_bonus

        return bonus

    @property
    def dodge_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.item.equippable:
            bonus += self.main_hand.item.equippable.dodge_bonus
            
        if self.off_hand and self.off_hand.item.equippable:
            bonus += self.off_hand.item.equippable.dodge_bonus
            
        if self.head and self.head.item.equippable:
            bonus += self.head.item.equippable.dodge_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.item.equippable.dodge_bonus
        
        if self.feet and self.feet.item.equippable:
            bonus += self.feet.item.equippable.dodge_bonus
            
        if self.belt and self.belt.item.equippable:
            bonus += self.belt.item.equippable.dodge_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.item.equippable.dodge_bonus
            
        if self.finger and self.finger.item.equippable:
            bonus += self.feet.item.equippable.dodge_bonus
            
        if self.neck and self.neck.item.equippable:
            bonus += self.feet.item.equippable.dodge_bonus
            
        if self.back and self.back.item.equippable:
            bonus += self.back.item.equippable.dodge_bonus

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
