from abc import ABC, abstractmethod


class AbstractGameStateHandler(ABC):
    """Abstract class to be used as a blueprint when creating new game state classes."""

    def __init__(self, superstate):
        self._superstate = superstate
        self._state = None

    @property
    def superstate(self):
        return self._superstate

    @property
    def state(self):
        return self._state

    @abstractmethod
    def change_state(self):
        """When used in a concrete class, this method should modify self._state"""
        pass
