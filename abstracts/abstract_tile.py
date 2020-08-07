from abc import ABC, abstractmethod


class AbstractTile(ABC):
    """Abstract for tiles. You likely want to inherit from FakeTile or Tile"""

    def __init__(self, variant):
        self.floor = self.initialize_floor(variant)
        self.blocker = self.initialize_blocker(variant)

    @abstractmethod
    def initialize_floor(self, variant):
        pass

    @abstractmethod
    def initialize_blocker(self, variant):
        pass

    @property
    def block_sight(self):
        if self.blocker is None:
            return False
        else:
            return self.blocker.opaque
