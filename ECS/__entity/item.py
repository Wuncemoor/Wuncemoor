class Item:
    def __init__(self, equippable_component=None, useable_component=None):
        self.equippable = equippable_component
        self.useable = useable_component
        self.name = None
        self.images = None
        
        if self.equippable:
            self.name = self.equippable.name
            self.images = self.equippable.images
        else:
            self.name = self.useable.name
            self.images = self.useable.images
        