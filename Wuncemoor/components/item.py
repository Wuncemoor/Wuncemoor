class Item:
    def __init__(self, equippable_component=None, useable_component=None):
        self.equippable = equippable_component
        self.useable = useable_component
        self.name = None
        self.image = None
        
        if self.equippable:
            self.name = self.equippable.name
            self.image = self.equippable.image
        else:
            self.name = self.useable.name
            self.image = self.useable.image
        