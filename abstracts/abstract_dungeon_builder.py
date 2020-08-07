from abc import ABC, abstractmethod


class AbstractDungeonBuilder(ABC):
    """Abstract for DungeonBuilders. Requires at minimum an InitMap mixin to make concrete."""

    def __init__(self, basename, subtype, floors, width, height, np):
        self.basename = basename
        self.subtype = subtype
        self.floors = floors
        self.width = width
        self.height = height
        self.np = np

    @abstractmethod
    def initialize_map(self):
        pass

    @abstractmethod
    def get_maps(self):
        pass

    @property
    def name(self):
        if self.subtype is None:
            return self.basename
        else:
            return self.subtype + '_' + self.basename

    def get_name(self):
        return self.name

    def get_floors(self):
        return self.floors

    def get_np(self):
        return self.np




