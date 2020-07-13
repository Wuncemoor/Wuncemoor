from random import randint
from ECS.entity import Entity
from builders.mob_builder import MobBuilder, MobDirector
from enums.game_states import EncounterStates, GameStates
from config.image_objects import BACKGROUNDS
from enums.render_order import RenderOrder
from handlers.views.camera import Camera
from handlers.views.fov_handler import FovHandler
from map_objects.chances.mob_chances import MobChances
from random_utils import random_choice_from_dict


class TitleHandler:
    def __init__(self):
        self.superstate = GameStates.TITLE


class LifeHandler:
    def __init__(self):
        self.superstate = GameStates.LIFE
        self.camera = Camera()
        self.camera.owner = self
        self.fov = FovHandler()
        self.fov.owner = self


class MenusHandler:
    def __init__(self):
        self.superstate = GameStates.MENUS
        self.state = None
        self.display = None
        self.menu = None

    def handle_menu(self, menu_obj):
        self.menu = menu_obj
        self.state = menu_obj.superstate
        self.owner.options.current = self.menu.options


class DialogueHandler:
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
            self.partner.noncombatant.dialogue.current_convo)
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


class TimeHandler:

    def __init__(self, observers):
        self.observers = observers
        self.year = -65
        self.month = 1
        self.day = 1
        self.hour = 6

    def goes_on(self):
        for party in self.observers:
            for member in party.members():
                member.age.get_older([0, 0, 0, 1])
        self.hour += 1
        self.new_day()

    def new_day(self):
        if self.hour > 23:
            self.hour -= 24
            self.day += 1
            self.new_month()

    def new_month(self):
        if self.day > 30:
            self.day -= 30
            self.month += 1
            self.new_year()

    def new_year(self):
        if self.month > 12:
            self.month -= 12
            self.year += 1

    def travel(self, time):
        self.year += time[0]
        self.month += time[1]
        self.new_year()
        self.day += time[2]
        self.new_month()
        self.hour += time[3]
        self.new_day()

    def apply_dilation(self, dungeon):
        for dmap in dungeon.maps:
            for entity in dmap.entities:
                if entity.age:
                    diff = map(lambda x, y: x - y, self.stamp(), dungeon.time_dilation)
                    entity.age.get_older(list(diff))
            for noncom in dmap.noncombatants:
                if noncom.age:
                    diff = map(lambda x, y: x - y, self.stamp(), dungeon.time_dilation)
                    noncom.age.get_older(list(diff))

    def stamp(self):
        return [self.year, self.month, self.day, self.hour]


class EncounterHandler:

    def __init__(self, loot):
        self.superstate = GameStates.ENCOUNTER
        self.state = EncounterStates.THINKING
        self.background = None
        self.mob = None
        self.options = None
        self.current_option = 0
        self.loot = loot
        self.steps_since = 0

    def check(self):
        return (self.steps_since / (100 + self.steps_since)) * 50 > randint(1, 100)

    def new(self, tile, options):
        self.state = EncounterStates.THINKING
        self.background = BACKGROUNDS.get(tile.type)
        self.mob = self.get_encounter_mob(tile)
        self.options = options
        self.current_option = 0
        self.loot.reset()
        self.steps_since = 0

    @staticmethod
    def get_encounter_mob(tile):
        mob_chances = MobChances(tile.type, tile.subtype, tile.np)
        mcs = mob_chances.get_mob_chances()
        monster_choice = random_choice_from_dict(mcs)

        mob_builder = MobBuilder(0, monster_choice)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        combatant = mob_director.get_combatant()
        mob = Entity(0, 0, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant)
        return mob


class RewardHandler:

    def __init__(self, loot):
        self.superstate = GameStates.REWARD
        self.loot = loot
        self.state = None
        self.options = ['AUTO', 'MANUAL', 'LEAVE']
        self.current_option = 0


