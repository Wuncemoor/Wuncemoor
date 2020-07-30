from abc import ABC, abstractmethod


class AbstractTileComponent(ABC):

    def __init__(self):
        self.image = None
        self.image2 = None

    @property
    @abstractmethod
    def name(self):
        pass


class AbstractTileFloor(AbstractTileComponent):

    def __init__(self):
        super().__init__()
        self.transition = None

    @property
    @abstractmethod
    def name(self):
        pass

    def has_transition(self):
        if self.transition is not None:
            return True
        return False


class AbstractTileBlocker(AbstractTileComponent):

    @property
    @abstractmethod
    def opaque(self):
        pass
