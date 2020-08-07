from config.constants import BLACK
from handlers.input_handler import InputHandler
from handlers.log_handler import LogHandler
from handlers.logic.options import initialize_menu_options
from handlers.options_handler import OptionsHandler
from handlers import state_handlers
from handlers.time_handler import TimeHandler
from handlers.logic_handler import LogicHandler
import pygame as py
import sys

from map_objects.loot import Loot


class GameHandler:

    def __init__(self, artist):
        self.state_handler = None
        self.artist = artist
        self.artist.owner = self
        self.logic = LogicHandler()
        self.logic.owner = self
        self.input = InputHandler()
        self.input.owner = self
        self.options = OptionsHandler()
        self.options.owner = self
        self.title = state_handlers.TitleHandler()
        self.title.owner = self
        self.life = state_handlers.LifeHandler()
        self.life.owner = self
        self.menus = state_handlers.MenusHandler()
        self.menus.owner = self
        self.debug = state_handlers.DebugHandler()
        self.debug.owner = self
        self.world = None
        self.dialogue = None
        self.time = None
        self.encounter = None
        self.reward = None
        self.party = None
        self.log = None

    @property
    def state(self):
        return self.state_handler.superstate

    def change_state(self, string):
        state_dict = {
            'title': self.title,
            'life': self.life,
            'menus': self.menus,
            'dialogue': self.dialogue,
            'encounter': self.encounter,
            'reward': self.reward,
            'debug': self.debug,
        }
        self.state_handler = state_dict.get(string)

    def take_ownership(self):
        self.world.owner = self
        self.dialogue.owner = self
        self.time.owner = self
        self.encounter.owner = self
        self.reward.owner = self
        self.party.owner = self
        self.log.owner = self

    def preplay(self, world, party):
        loot = Loot()
        self.artist.screen.fill(BLACK)
        self.world = world
        self.dialogue = state_handlers.DialogueHandler([party.journal])
        self.time = TimeHandler([party])
        self.encounter = state_handlers.EncounterHandler(loot)
        self.reward = state_handlers.RewardHandler(loot)
        self.party = party
        self.party.options = initialize_menu_options(self.party.members)
        self.party.journal.options = initialize_menu_options(self.party.journal.subgroups)
        self.party.inventory.options = initialize_menu_options(self.party.inventory.subgroups)
        self.log = LogHandler()
        self.debug.set_allowed_objs()
        self.take_ownership()
        self.life.camera.refocus(party.p1.x, party.p1.y)
        self.life.fov.map = self.life.fov.initialize(self.world)
        self.state_handler = self.life

    @staticmethod
    def quit():
        py.quit()
        sys.exit()
