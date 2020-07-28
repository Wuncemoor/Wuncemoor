from abc import ABC, abstractmethod

from map_objects.concrete_maps import DangerousMap, SafeMap


class AbstractDungeonBuilder(ABC):

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


class DangerousDungeonBuilder(AbstractDungeonBuilder):

    def initialize_map(self):
        map = DangerousMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map

    @abstractmethod
    def get_maps(self):
        pass


class SafeDungeonBuilder(AbstractDungeonBuilder):

    def initialize_map(self):
        map = SafeMap(self.width, self.height, variant=self.basename)
        map.initialize_tiles()
        return map

    @abstractmethod
    def get_maps(self):
        pass


