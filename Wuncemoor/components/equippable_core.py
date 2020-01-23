class EquippableCore:
    
    def __init__(self, core):
        self.core = core
        self.image = None
        self.resource_bonuses = [0,0,0,0]
        self.power_bonuses = [0,0,0]
        self.spirit_bonuses = [0,0,0,0,0]
        self.resist_phys_bonuses = [0,0,0]
        self.resist_ele_bonuses = [0,0,0,0,0]
        self.hit_dodge_bonuses = [0,0]
        self.values = [0,0]


        if self.core == 'staff':
        
            self.image = '/'
            self.resource_bonuses = [0,0,0,0]
            self.power_bonuses = [0,0,32]
            self.spirit_bonuses = [0,0,0,0,0]
            self.resist_phys_bonuses = [0,0,0]
            self.resist_ele_bonuses = [0,0,0,0,0]
            self.hit_dodge_bonuses = [0,0]
            self.values = [0,0]
            
        elif self.core == 'dagger':
        
            self.image = '-'
            self.resource_bonuses = [0,0,0,0]
            self.power_bonuses = [6,10,0]
            self.spirit_bonuses = [0,0,0,0,0]
            self.resist_phys_bonuses = [0,0,0]
            self.resist_ele_bonuses = [0,0,0,0,0]
            self.hit_dodge_bonuses = [5,0]
            self.values = [0,0]

        elif self.core == 'longsword':
            
            self.image = '-'
            self.resource_bonuses = [0,0,0,0]
            self.power_bonuses = [32,6,0]
            self.spirit_bonuses = [0,0,0,0,0]
            self.resist_phys_bonuses = [0,0,0]
            self.resist_ele_bonuses = [0,0,0,0,0]
            self.hit_dodge_bonuses = [5,0]
            self.values = [0,0]            

        elif self.core == 'shield':

            self.image = '['
            self.resource_bonuses = [0,0,0,0]
            self.power_bonuses = [0,0,0]
            self.spirit_bonuses = [0,0,0,0,0]
            self.resist_phys_bonuses = [15,15,15]
            self.resist_ele_bonuses = [5,5,5,5,0]
            self.hit_dodge_bonuses = [5,0]
            self.values = [0,0]            
            
            
        