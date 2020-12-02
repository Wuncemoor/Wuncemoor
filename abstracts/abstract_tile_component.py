from abc import ABC, abstractmethod
from dataclasses import dataclass

from pygame.surface import Surface

from world_objects.transition import Transition


@dataclass
class AbstractTileComponent(ABC):
    """You likely want to inherit from  AbstractTileFloor, AbstractTileBlocker, or AbstractTileOverhead"""

    image: Surface = None

    @property
    @abstractmethod
    def name(self):
        pass


@dataclass
class AbstractTileFloor(AbstractTileComponent):
    """Abstract to make a type of ground for the Player to walk on. Can hold transitions which take Player to another
    Map when stepped on. """

    transition: Transition = None

    @property
    @abstractmethod
    def name(self):
        pass

    def has_transition(self):
        if self.transition is not None:
            return True
        return False


@dataclass
class ModalTileFloor(AbstractTileFloor):
    """Some TileFloor images are dynamic based on neighboring tiles. Has dictionaries to change image."""

    mode: str = None

    @property
    @abstractmethod
    def image_dict(self):
        pass

    def set_images(self):
        self.image = self.image_dict.get(self.mode)


@dataclass
class AbstractTileBlocker(AbstractTileComponent):
    """Abstract for TileBlocker components for Tile. Blocks field of view if opaque."""

    int_image: Surface = None

    @property
    @abstractmethod
    def opaque(self):
        pass


@dataclass
class ModalTileBlocker(AbstractTileBlocker):

    mode: str = None

    @property
    @abstractmethod
    def image_dict(self):
        pass

    def set_images(self):
        self.image = self.image_dict.get(self.mode)


@dataclass
class AbstractTileOverhead(AbstractTileComponent):

    distance_overhead: int = 1
    is_interior: bool = False

    @property
    @abstractmethod
    def name(self):
        pass
