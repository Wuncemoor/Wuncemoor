from enum import Enum	


class GameStates(Enum):
    TITLE = 1
    LIFE = 2
    PLAYER_DEAD = 3
    SHOW_INVENTORY = 4
    DROP_INVENTORY = 5
    TARGETING = 6
    LEVEL_UP = 7
    COMPETENCE_MENU = 8
    ENCOUNTER = 9
    DIALOGUE = 10
    SHOW_MAP = 11
    REWARD = 12
    MENUS = 13


class EncounterStates(Enum):

    THINKING = 1
    FIGHT_TARGETING = 2
    ENEMY_TURN = 3
    VICTORY = 4


class RewardStates(Enum):

    THINKING = 1
    SIFTING = 2
    DEPOSITING = 3


class MenuStates(Enum):

    PARTY = 1
    JOURNAL = 2
    INVENTORY = 3
    MAP = 4
