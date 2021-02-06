from copy import copy
from random import randint

from abstracts.abstract_handlers import AbstractGameStateHandler
from enums.game_states import EncounterStates, GameStates, ShopStates, RewardStates, TitleStates
from config.image_objects import BACKGROUNDS
from handlers.encounter.combat import Combat
from handlers.views.camera import Camera
from handlers.views.fov_handler import FovHandler
from handlers.views.messages import Message
from screens.encounter_screen import get_encounter_thinking_menu
from screens.reward_screen import get_reward_thinking_menu
from screens.title_screen import get_title_menu


class TitleHandler(AbstractGameStateHandler):
    """Handler for GameStates.TITLE"""

    def __init__(self, superstate):
        super().__init__(superstate)
        self.menu = get_title_menu()

    def change_state(self):
        pass
        # self._state =


class LifeHandler(AbstractGameStateHandler):
    """Handler for GameStates.LIFE"""

    def __init__(self, superstate):
        super().__init__(superstate)
        self.camera = Camera()
        self.camera.owner = self
        self.fov = FovHandler()
        self.fov.owner = self

    def change_state(self):
        pass
        # self._state =


class MenusHandler(AbstractGameStateHandler):
    """Handler for GameStates.MENUS"""

    def __init__(self, superstate):
        super().__init__(superstate)
        self.menu_type = None

    def change_state(self, menu, options):
        self.menu_type = menu
        self._state = menu.superstate
        self.confirm_submenu()
        options.current = self.menu_type.menu

    def confirm_submenu(self):
        if self.menu_type.submenu is None:
            pass
        elif len(self.menu_type.submenu) == 0:
            self.menu_type.submenu = None


class DialogueHandler(AbstractGameStateHandler):
    """Handler for GameStates.DIALOGUE"""
    def __init__(self, superstate, observers):
        super().__init__(superstate)
        self.partner = None
        self.observers = observers
        self.real_talk = None
        self.real_io = None

    def change_state(self):
        pass
        # self._state =

    def set_real_talk(self):
        responses = []
        for observer in self.observers:
            response = observer.transduce_all(self.partner.name)
            for res in response:
                responses.append(res)
        current_node = self.partner.converser.dialogue.graph_dict.get(
            self.partner.converser.dialogue.conversation)
        options = current_node.options_text
        self.real_talk = [i for i in options if i.condition is None or i.condition in responses]
        self.set_real_io()

    def set_real_io(self):
        real = {}
        q = 1
        for option in self.real_talk:
            real[str(q)] = option.path
            q += 1
        self.real_io = real

    def broadcast_choice(self, signal):
        if signal is not None:
            for observer in self.observers:
                observer.update_plot(signal)

    def deja_vu_check(self, option):

        dialogue = self.partner.converser.dialogue

        nn_string = self.real_io.get(str(option))

        new_node = dialogue.graph_dict.get(nn_string)
        return new_node.visited


class EncounterHandler(AbstractGameStateHandler):
    """Handler for GameStates.ENCOUNTER"""

    def __init__(self, superstate, loot):
        super().__init__(superstate)
        self.background = None
        self.combat = None
        self.menu = self.initialize_menu()
        self.loot = loot
        self.steps_since = 0

    def change_state(self, state, options):

        state_options_dict = {
            EncounterStates.THINKING: self.menu,
            EncounterStates.FIGHT_TARGETING: self.combat.grid,
        }

        self._state = state
        options.current = state_options_dict.get(state)

    @staticmethod
    def initialize_menu():
        return get_encounter_thinking_menu()

    def check_for_encounter(self, tile):
        encountering = (self.steps_since / (100 + self.steps_since)) * 50 > randint(1, 100)
        if encountering:
            return [{'new_encounter': tile}]
        else:
            self.steps_since += 1
            return []

    def new_encounter(self, tile, options):
        self.combat = self.get_combat(tile)
        self.combat.owner = self
        self.change_state(EncounterStates.THINKING, options)
        self.background = BACKGROUNDS.get(tile.type)
        self.loot.reset()
        options.current.pointer = 0
        self.steps_since = 0

    def get_combat(self, tile):
        combat = Combat(self.owner.party, tile)
        return combat


class RewardHandler(AbstractGameStateHandler):
    """Handler for GameStates.REWARD"""

    def __init__(self, superstate, loot):
        super().__init__(superstate)
        self.loot = loot
        self.menu = self.initialize_menu()

    def change_state(self, state, options):
        state_options_dict = {
            RewardStates.THINKING: self.menu,
            # RewardStates.SIFTING: self.wrap(self.owner.reward.loot.items, fake=reward_sifting),
            # RewardStates.DEPOSITING: self.wrap(self.owner.reward.loot.claimed, fake=reward_depositing),
        }
        self._state = state
        options.current = state_options_dict.get(state)

    @staticmethod
    def initialize_menu():
        return get_reward_thinking_menu()


class DebugHandler(AbstractGameStateHandler):
    """Handler for GameStates.DEBUG"""

    def __init__(self, superstate):
        super().__init__(superstate)
        self.previous_state = None
        self.allowed_inputs = self.init_allowed_inputs()
        self.allowed_objs = None
        self.current_input = ''
        self.message_slot = None

    def change_state(self):
        pass
        # self._state =

    def init_allowed_inputs(self):
        """All other commands not recognized, will add "suggestions" later"""
        allowed_inputs = {'clear': self.clear, 'repr': self.repr, 'str': self.str, 'name': self.name,
                          'bool_map': self.bool_map}
        return allowed_inputs

    def set_allowed_objs(self):
        """All other commands not recognized, will add "suggestions" later"""
        tiles = self.owner.world.current_map.tiles
        objs = {
            'floor': [[tile.floor for tile in row] for row in tiles],
            'light_image': [[tile.floor.image for tile in row] for row in tiles],
            'transition': [[tile.floor.transition for tile in row] for row in tiles],
        }
        self.allowed_objs = objs

    def clear(self):
        """Clear debug screen of old text"""
        self.owner.log.debugger.messages.clear()
        # Remove message from previous command
        self.message_slot = []

    def repr(self, obj, x, y):
        """Returns __repr__ of obj on current map"""

        message = Message.placeholder()
        sub_obj = self.allowed_objs.get(obj)[y][x]
        message.text = repr(sub_obj)
        self.message_slot = [message]

    def str(self, obj, x, y):
        """Returns __str__ of obj on current map"""

        message = Message.placeholder()
        sub_obj = self.allowed_objs.get(obj)[y][x]
        message.text = str(sub_obj)
        self.message_slot = [message]

    def name(self, obj, x, y):
        """Returns obj.name"""

        message = Message.placeholder()
        sub_obj = self.allowed_objs.get(obj)[y][x]
        if sub_obj is None:
            message.text = 'OBJECT NOT FOUND'
        else:
            message.text = sub_obj.name
        self.message_slot = [message]

    def bool_map(self, obj):
        """Returns current map as ASCII made of 1's and 0's based on existence of obj"""
        mes = []
        tiles = self.owner.world.current_map.tiles
        obj_dict = {
            'transition': [[tile.floor.transition for tile in row] for row in tiles],
        }
        vals = obj_dict.get(obj)
        for row in vals:
            message = Message.placeholder()
            text = ''
            for val in row:
                if val is not None:
                    text += '1 '
                else:
                    text += '0 '
            message.text = text
            mes.append(message)
        self.message_slot = mes


class ShopHandler(AbstractGameStateHandler):
    """Handler for GameStates.SHOP"""

    def __init__(self, superstate):
        super().__init__(superstate)
        self.shopkeeper = None
        self.snapshot = None
        self.sub_index = None
        self.transaction_details = []

    def change_state(self, state):
        self.state = state
        if self.state is ShopStates.BASE:
            case = None
        else:
            case = 'sub'
        self.owner.options.get(case=case)
        self.owner.options.current.choice = self.sub_index
        if self.state is ShopStates.BASE:
            self.sub_index = None

    def get_subinventories(self, index):
        player_subinv = self.snapshot[0].menu[index]
        shop_subinv = self.snapshot[1].menu[index]
        return player_subinv, shop_subinv

    def take_snapshot(self):
        player_inventory = copy(self.owner.party.inventory)
        shop_inventory = copy(self.shopkeeper.shopkeeper.inventory)
        self.snapshot = [player_inventory, shop_inventory]
