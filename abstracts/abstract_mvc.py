from abc import ABC, abstractmethod
from enums.game_states import GameStates
from handlers.game_handler import GameHandler


class MVC(ABC):
    """Abstract for Model-View-Controller.  """

    def __init__(self, game: GameHandler) -> None:
        self.game = game

    @property
    def state(self):
        return self.game.state

    @property
    def handler(self):
        return self.game.state_handler

    @property
    def mapping(self):
        maps = {
            GameStates.DEBUG: self.debug,
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.SHOP: self.shop,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.reward,
        }
        return maps.get(self.state)

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def life(self):
        pass

    @abstractmethod
    def encounter(self):
        pass

    @abstractmethod
    def dialogue(self):
        pass

    @abstractmethod
    def shop(self):
        pass

    @abstractmethod
    def menus(self):
        pass

    @abstractmethod
    def reward(self):
        pass

