class EquippableMaterial:
    """Equippable component representing the material that the Item is made of."""
    
    def __init__(self, material):
        
        self.material = material
        self.modifier = 0
        
        if self.material == 'wood':
            self.modifier = 0.25
        elif self.material == 'stone':
            self.modifier = 0.35
        elif self.material == 'bone':
            self.modifier = 0.4
        elif self.material == 'copper':
            self.modifier  = 0.5
        elif self.material == 'bronze':
            self.modifier = 0.7
        elif self.material == 'iron':
            self.modifier = 1.0
            