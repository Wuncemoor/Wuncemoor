from config.constants import KEYDOWN_DELAY
from enums.game_states import GameStates
from handlers import state_handlers
import pygame as py

from world_objects.loot import Loot


class GameHandler:
    """Handler that holds nearly all aspects of the game while delegating the heavy lifting to StateHandlers"""

    def __init__(self, options):
        self.state_handler = None
        self.fullscreen = True
        self.options = options
        self.options.owner = self
        self.title = state_handlers.TitleHandler(GameStates.TITLE)
        self.title.owner = self
        self.life = state_handlers.LifeHandler(GameStates.LIFE)
        self.life.owner = self
        self.menus = state_handlers.MenusHandler(GameStates.MENUS)
        self.menus.owner = self
        self.debug = state_handlers.DebugHandler(GameStates.DEBUG)
        self.debug.owner = self
        self.dialogue = None
        self.encounter = None
        self.reward = None
        self.shop = None
        self.model = None

    @property
    def state(self):
        return self.state_handler.superstate

    @property
    def substate(self):
        return self.state_handler.state

    def set_root_state(self):
        self.state_handler = self.title
        self.options.current = self.state_handler.menu

    def change_state(self, string):
        state_dict = {
            'title': self.title,
            'life': self.life,
            'menus': self.menus,
            'dialogue': self.dialogue,
            'shop': self.shop,
            'encounter': self.encounter,
            'reward': self.reward,
            'debug': self.debug,
        }

        self.set_key_repeat(string)
        self.state_handler = state_dict.get(string)

    @staticmethod
    def set_key_repeat(string):
        if string != 'life':
            py.key.set_repeat()
        else:
            py.key.set_repeat(KEYDOWN_DELAY)

    def take_ownership(self):
        self.model.world.owner = self.model
        self.model.time.owner = self.model
        self.model.party.owner = self.model
        self.model.log.owner = self.model
        self.dialogue.owner = self
        self.encounter.owner = self
        self.reward.owner = self
        self.shop.owner = self

    def preplay(self, model):
        loot = Loot()
        self.model = model
        self.dialogue = state_handlers.DialogueHandler(GameStates.DIALOGUE, [model.party.journal])
        self.shop = state_handlers.ShopHandler(GameStates.SHOP)
        self.encounter = state_handlers.EncounterHandler(GameStates.ENCOUNTER, loot)
        self.reward = state_handlers.RewardHandler(GameStates.REWARD, loot)
        self.debug.set_allowed_objs()
        self.take_ownership()
        self.life.initialize_components(model)
        self.state_handler = self.life
        self.state_handler.change_state('root', 'null')
