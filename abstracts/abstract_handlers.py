from abc import ABC, abstractmethod


class AbstractGameStateHandler(ABC):
    """Abstract class to be used as a blueprint when creating new game state classes."""

    def __init__(self, superstate):
        self._superstate = superstate
        self._state = None

    @property
    def superstate(self):
        """This is used by the GameHandler to determine which state the game is in and should never be modified."""
        return self._superstate

    @property
    def state(self):
        """This should only be modified explicitly through self.change_state"""
        return self._state

    @abstractmethod
    def change_state(self):
        """When used in a concrete class, this method should modify self._state"""
        pass
