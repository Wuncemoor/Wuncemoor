from abc import ABC, abstractmethod


class TileFloor(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def image(self):
        pass

    @property
    @abstractmethod
    def image2(self):
        pass


class TileBlocker(TileFloor):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def image(self):
        pass

    @property
    @abstractmethod
    def image2(self):
        pass

    @property
    @abstractmethod
    def opaque(self):
        pass