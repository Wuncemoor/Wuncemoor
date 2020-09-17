from abc import ABC, abstractmethod


class AbstractTile(ABC):
    """Abstract for tiles. You likely want to inherit from FakeTile or Tile"""

    def __init__(self):
        self.floor = self.initialize_floor()
        self.blocker = self.initialize_blocker()

    @abstractmethod
    def initialize_floor(self):
        pass

    @abstractmethod
    def initialize_blocker(self):
        pass

    @property
    def block_sight(self):
        if self.blocker is None:
            return False
        else:
            return self.blocker.opaque
