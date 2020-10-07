class Item:
    """Component for Entities. Behavior is determined by Item components"""
    def __init__(self, value: int, equippable=None, useable=None, craftable=None, important=False, stackable=False):
        self.value = value
        self.equippable = equippable
        self.useable = useable
        self.craftable = craftable
        self.important = important
        self.stackable = stackable
        self.name = None
        self.images = None
        
        if self.equippable:
            self.name = self.equippable.name
            self.images = self.equippable.images
        elif self.useable:
            self.name = self.useable.name
            self.images = self.useable.images
        elif self.craftable:
            self.name = self.craftable.name
            self.images = self.craftable.images
        else:
            self.name = self.important.name
            self.images = self.important.images

