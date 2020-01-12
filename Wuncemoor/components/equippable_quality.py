class EquippableQuality:
    
    def __init__(self, quality):
        
        self.quality = quality
        self.modifier = 0
        
        if self.quality == 'rusty':
            self.modifier = 0.5
        elif self.quality == 'average':
            self.modifier = 1.0
        
    