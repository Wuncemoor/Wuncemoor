from config.constants import BLACK
from handlers.input_handler import InputHandler
from handlers.log_handler import LogHandler
from handlers.logic.options import initialize_menu_options
from handlers.options_handler import OptionsHandler
from handlers.state_handlers import MenusHandler, TitleHandler, LifeHandler, DialogueHandler, TimeHandler, \
    EncounterHandler, RewardHandler
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
        self.title = TitleHandler()
        self.title.owner = self
        self.life = LifeHandler()
        self.life.owner = self
        self.menus = MenusHandler()
        self.menus.owner = self



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

    def preplay(self, dungeons, world, overworld_tiles, party):
        loot = Loot()
        self.artist.screen.fill(BLACK)
        self.artist.world_tiles = overworld_tiles
        self.world = world
        self.dungeons = dungeons
        self.dialogue = DialogueHandler([party.journal])
        self.time = TimeHandler([party])
        self.encounter = EncounterHandler(loot)
        self.reward = RewardHandler(loot)
        self.party = party
        self.party.options = initialize_menu_options(self.party.members)
        self.party.journal.options = initialize_menu_options(self.party.journal.subgroups)
        self.party.inventory.options = initialize_menu_options(self.party.inventory.subgroups)
        self.log = LogHandler()
        self.take_ownership()
        self.life.camera.refocus(party.p1.x, party.p1.y)
        self.life.fov.map = self.life.fov.initialize(self.world)
        self.state_handler = self.life

    def quit(self):
        py.quit()
        sys.exit()




