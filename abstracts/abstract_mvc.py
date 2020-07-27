from abc import ABC, abstractmethod
from enums.game_states import GameStates


class MVC(ABC):

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.reward,
        }
        return maps.get(self.state)

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
    def menus(self):
        pass

    @abstractmethod
    def reward(self):
        pass
