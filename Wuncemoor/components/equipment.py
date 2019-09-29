from equipment_slots import EquipmentSlots

class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, body=None, feet=None, belt=None, hands=None, finger=None, neck=None, back=None, accessory=None):
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
        self.accessory = accessory
        
    @property
    def max_hp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.max_hp_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_hp_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.max_hp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.max_hp_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.max_hp_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.max_hp_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.max_hp_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.max_hp_bonus
            
        return bonus
        
    @property
    def max_mp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_mp_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_mp_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_mp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.max_mp_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_mp_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.max_mp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.max_mp_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.max_mp_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.max_mp_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.max_mp_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.max_mp_bonus
            
        return bonus

    @property
    def max_tp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_tp_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_tp_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_tp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.max_tp_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_tp_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.max_tp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.max_tp_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.max_tp_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.max_tp_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.max_tp_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.max_tp_bonus
            
        return bonus

    @property
    def max_vp_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_vp_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_vp_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_vp_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.max_vp_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_vp_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.max_vp_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.max_vp_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.max_vp_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.max_vp_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.max_vp_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.max_vp_bonus
            
        return bonus

        
    @property
    def power_slash_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_slash_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_slash_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_slash_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.power_slash_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_slash_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.power_slash_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.power_slash_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.power_slash_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.power_slash_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.power_slash_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.power_slash_bonus
            
        return bonus

    @property
    def power_pierce_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_pierce_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_pierce_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_pierce_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.power_pierce_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_pierce_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.power_pierce_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.power_pierce_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.power_pierce_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.power_pierce_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.power_pierce_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.power_pierce_bonus

            
        return bonus
        
    @property
    def power_blunt_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_blunt_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_blunt_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_blunt_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.power_blunt_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_blunt_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.power_blunt_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.power_blunt_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.power_blunt_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.power_blunt_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.power_blunt_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.power_blunt_bonus
            
        return bonus
        
    @property
    def spirit_heat_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.spirit_heat_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.spirit_heat_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.spirit_heat_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.spirit_heat_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.spirit_heat_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.spirit_heat_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.spirit_heat_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.spirit_heat_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.spirit_heat_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.spirit_heat_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.spirit_heat_bonus
            
        return bonus
       
    @property
    def spirit_cold_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.spirit_cold_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.spirit_cold_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.spirit_cold_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.spirit_cold_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.spirit_cold_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.spirit_cold_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.spirit_cold_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.spirit_cold_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.spirit_cold_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.spirit_cold_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.spirit_cold_bonus
            
        return bonus
        
    @property
    def spirit_acid_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.spirit_acid_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.spirit_acid_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.spirit_acid_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.spirit_acid_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.spirit_acid_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.spirit_acid_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.spirit_acid_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.spirit_acid_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.spirit_acid_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.spirit_acid_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.spirit_acid_bonus
            
        return bonus
        
    @property
    def spirit_current_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.spirit_current_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.spirit_current_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.spirit_current_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.spirit_current_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.spirit_current_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.spirit_current_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.spirit_current_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.spirit_current_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.spirit_current_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.spirit_current_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.spirit_current_bonus
            
        return bonus
        
    @property
    def spirit_aether_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.spirit_aether_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.spirit_aether_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.spirit_aether_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.spirit_aether_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.spirit_aether_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.spirit_aether_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.spirit_aether_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.spirit_aether_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.spirit_aether_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.spirit_aether_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.spirit_aether_bonus
            
        return bonus
        
       
                
        
    @property
    def resist_slash_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_slash_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_slash_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_slash_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_slash_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_slash_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_slash_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_slash_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_slash_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_slash_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_slash_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_slash_bonus
            
        return bonus

    @property
    def resist_pierce_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_pierce_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_pierce_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_pierce_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_pierce_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_pierce_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_pierce_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_pierce_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_pierce_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_pierce_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_pierce_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_pierce_bonus
            
        return bonus
        
    @property
    def resist_blunt_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_blunt_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_blunt_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_blunt_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_blunt_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_blunt_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_blunt_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_blunt_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_blunt_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_blunt_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_blunt_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_blunt_bonus
            
        return bonus

    @property
    def resist_heat_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_heat_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_heat_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_heat_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_heat_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_heat_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_heat_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_heat_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_heat_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_heat_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_heat_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_heat_bonus
            
        return bonus

    @property
    def resist_cold_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_cold_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_cold_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_cold_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_cold_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_cold_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_cold_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_cold_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_cold_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_cold_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_cold_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_cold_bonus
            
        return bonus

    @property
    def resist_acid_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_acid_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_acid_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_acid_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_acid_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_acid_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_acid_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_acid_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_acid_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_acid_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_acid_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_acid_bonus
            
        return bonus

    @property
    def resist_current_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_current_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_current_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_current_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_current_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_current_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_current_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_current_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_current_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_current_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_current_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_current_bonus

        return bonus

    @property
    def resist_aether_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resist_aether_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resist_aether_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.resist_aether_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.resist_aether_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resist_aether_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.resist_aether_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.resist_aether_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.resist_aether_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.resist_aether_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.resist_aether_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.resist_aether_bonus
            
        return bonus
    @property
    def accuracy_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.accuracy_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.accuracy_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.accuracy_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.accuracy_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.accuracy_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.accuracy_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.accuracy_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.accuracy_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.accuracy_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.accuracy_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.accuracy_bonus
            
        return bonus

    @property
    def dodge_bonus(self):
    
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.dodge_bonus
            
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.dodge_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.dodge_bonus
            
        if self.body and self.body.eqiuppable:
            bonus += self.body.equippable.dodge_bonus
        
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.dodge_bonus
            
        if self.belt and self.belt.equippable:
            bonus += self.belt.equippable.dodge_bonus
            
        if self.hands and self.hands.eqiuppable:
            bonus += self.feet.equippable.dodge_bonus
            
        if self.finger and self.finger.equippable:
            bonus += self.feet.equippable.dodge_bonus
            
        if self.neck and self.neck.equippable:
            bonus += self.feet.equippable.dodge_bonus
            
        if self.back and self.back.equippable:
            bonus += self.back.equippable.dodge_bonus
            
        if self.accessory and self.accessory.equippable:
            bonus += self.accessory.equippable.dodge_bonus
            
        return bonus

       
    def toggle_equip(self, equippable_entity):
        results = []
        
        slot = equippable_entity.equippable.slot
        
        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': equippable_entity})
                    
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
                self.belt == None
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
                
        elif slot == EquipmentSlots.FINGERS:
            if self.fingers == equippable_entity:
                self.fingers = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.fingers:
                    results.append({'dequipped': equippable_entity})
                    
                self.fingers = equippable_entity
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
                
        elif slot == EquipmentSlots.ACCESSORY:
            if self.accessory == equippable_entity:
                self.accessory = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.accessory:
                    results.append({'dequipped': equippable_entity})
                    
                self.accessory = equippable_entity
                results.append({'equipped': equippable_entity})
                
        return results