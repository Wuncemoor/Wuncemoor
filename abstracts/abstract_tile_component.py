from abc import ABC, abstractmethod


class AbstractTileComponent(ABC):
    """You likely want to inherit from  AbstractTileFloor, AbstractTileBlocker, or AbstractTileOverhead"""

    def __init__(self, image=None):
        self.image = image

    @property
    @abstractmethod
    def name(self):
        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class AbstractTileFloor(AbstractTileComponent):
    """Abstract to make a type of ground for the Player to walk on. Can hold transitions which take Player to another
    Map when stepped on. """

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


class ModalTileFloor(AbstractTileFloor):
    """Some TileFloor images are dynamic based on neighboring tiles. Has dictionaries to change image."""

    def __init__(self):
        super().__init__()
        self.mode = None

    @property
    @abstractmethod
    def image_dict(self):
        pass

    def set_images(self):
        self.image = self.image_dict.get(self.mode)


class AbstractTileBlocker(AbstractTileComponent):
    """Abstract for TileBlocker components for Tile. Blocks field of view if opaque."""

    def __init__(self, image=None):
        super().__init__(image)

    @property
    @abstractmethod
    def opaque(self):
        pass


class ModalTileBlocker(AbstractTileBlocker):

    def __init__(self):
        super().__init__()
        self.mode = None

    @property
    @abstractmethod
    def image_dict(self):
        pass

    def set_images(self):
        self.image = self.image_dict.get(self.mode)


class AbstractTileOverhead(AbstractTileComponent):

    def __init__(self, distance_overhead: int, image=None):
        super().__init__(image)
        self.distance_overhead = distance_overhead

    @property
    @abstractmethod
    def name(self):
        pass
