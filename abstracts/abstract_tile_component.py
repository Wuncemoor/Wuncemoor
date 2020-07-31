from abc import ABC, abstractmethod


class AbstractTileComponent(ABC):

    def __init__(self):
        self.light_image = None
        self.dark_image = None

    @property
    @abstractmethod
    def name(self):
        pass


class AbstractTileFloor(AbstractTileComponent):

    def __init__(self):
        super().__init__()
        self.transition = None

    def has_transition(self):
        if self.transition is not None:
            return True
        return False

class ModalTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.mode = None

    @property
    @abstractmethod
    def light_dict(self):
        pass

    @property
    @abstractmethod
    def dark_dict(self):
        pass


class AbstractTileBlocker(AbstractTileComponent):

    @property
    @abstractmethod
    def opaque(self):
        pass
