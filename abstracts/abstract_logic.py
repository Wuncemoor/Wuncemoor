from abc import ABC, abstractmethod


class AbstractLogic(ABC):
    """LogicHandler uses objects that inherit from this"""

    @abstractmethod
    def logic(self):
        pass