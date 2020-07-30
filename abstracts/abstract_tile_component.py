from abc import ABC, abstractmethod


class TileFloor(ABC):

    def __init__(self, image, image2):
        self.image = image
        self.image2 = image2

    @property
    @abstractmethod
    def name(self):
        pass


class TileBlocker(TileFloor):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def opaque(self):
        pass
