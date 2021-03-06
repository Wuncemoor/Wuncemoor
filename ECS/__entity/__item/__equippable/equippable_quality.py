class EquippableQuality:
    """Equippable component representing the quality of the Item."""
    def __init__(self, quality):
        
        self.quality = quality
        self.modifier = 0
        
        if self.quality == 'rusty':
            self.modifier = 0.5
        elif self.quality == 'average':
            self.modifier = 1.0
        elif self.quality == 'fine':
            self.modifier = 1.5
        
    