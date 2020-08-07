from random import randint
from enums.game_states import EncounterStates, GameStates
from config.image_objects import BACKGROUNDS
from handlers.encounter.combat import Combat
from handlers.logic.options import encounter_window_options
from handlers.views.camera import Camera
from handlers.views.fov_handler import FovHandler
from handlers.views.messages import Message


class TitleHandler:
    """Handler for GameStates.TITLE"""

    def __init__(self):
        self.superstate = GameStates.TITLE
        self.state = None


class LifeHandler:
    """Handler for GameStates.LIFE"""

    def __init__(self):
        self.superstate = GameStates.LIFE
        self.camera = Camera()
        self.camera.owner = self
        self.fov = FovHandler()
        self.fov.owner = self


class MenusHandler:
    """Handler for GameStates.MENUS"""

    def __init__(self):
        self.superstate = GameStates.MENUS
        self.state = None
        self.menu = None

    def change_state(self, menu):
        self.menu = menu
        self.state = menu.superstate
        self.confirm_submenu()
        self.owner.options.get()

    def confirm_submenu(self):
        if self.menu.sub is None:
            pass
        elif len(self.menu.sub) == 0:
            self.menu.sub = None


class DialogueHandler:
    """Handler for GameStates.DIALOGUE"""
    def __init__(self, observers):
        self.superstate = GameStates.DIALOGUE
        self.partner = None
        self.observers = observers
        self.real_talk = None
        self.real_io = None

    def set_real_talk(self):
        responses = []
        for observer in self.observers:
            response = observer.transduce_all(self.partner.name)
            for res in response:
                responses.append(res)
        current_node = self.partner.noncombatant.dialogue.graph_dict.get(
            self.partner.noncombatant.dialogue.conversation)
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

        dialogue = self.partner.noncombatant.dialogue

        nn_string = self.real_io.get(str(option))

        new_node = dialogue.graph_dict.get(nn_string)
        return new_node.visited


class EncounterHandler:
    """Handler for GameStates.ENCOUNTER"""

    def __init__(self, loot):
        self.superstate = GameStates.ENCOUNTER
        self.state = EncounterStates.THINKING
        self.background = None
        self.combat = None
        self.loot = loot
        self.steps_since = 0

    def change_state(self, state):
        self.state = state
        self.owner.options.get()

    def check(self, tile):
        encountering = (self.steps_since / (100 + self.steps_since)) * 50 > randint(1, 100)
        if encountering:
            self.new(tile)
            self.owner.state_handler = self
            self.owner.options.get()
        else:
            self.steps_since += 1

    def new(self, tile):
        self.state = EncounterStates.THINKING
        self.background = BACKGROUNDS.get(tile.type)
        self.combat = self.get_combat(tile)
        self.combat.owner = self
        self.loot.reset()
        self.steps_since = 0

    def get_combat(self, tile):
        combat = Combat(self.owner.party, tile)
        return combat

    def give_options(self):
        opts_dict = {
            EncounterStates.THINKING: encounter_window_options(),
            EncounterStates.FIGHT_TARGETING: self.combat.grid,
        }
        return opts_dict.get(self.state)


class RewardHandler:
    """Handler for GameStates.REWARD"""

    def __init__(self, loot):
        self.superstate = GameStates.REWARD
        self.loot = loot
        self.state = None

    def change_state(self, state):
        self.state = state
        self.owner.options.get()


class DebugHandler:
    """Handler for GameStates.DEBUG"""

    def __init__(self):
        self.superstate = GameStates.DEBUG
        self.previous_state = None
        self.allowed_inputs = self.init_allowed_inputs()
        self.allowed_objs = None
        self.current_input = ''
        self.message_slot = None

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
            'light_image': [[tile.floor.light_image for tile in row] for row in tiles],
            'dark_image': [[tile.floor.dark_image for tile in row] for row in tiles],
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






