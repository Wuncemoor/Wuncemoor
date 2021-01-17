from pygame.transform import scale

from ECS.__entity.item import Item
from config.image_objects import DIALOGUE_BG, POINTER_RIGHT
from data_structures.gui_tools import get_alpha_surface
from data_structures.menu_tools import MenuSpecs
from abstracts.abstract_menu import AbstractMenu
from enums.game_states import GameStates, MenuStates, EncounterStates, RewardStates, ShopStates
from abstracts.abstract_mvc import MVC
from handlers.encounter.combat import CombatGrid
from handlers.logic.logic_chunks import AttackMob, GoToReward, RewardSifting, RewardDepositing, UseItem, \
    ExamineItem, DropItem, attempt_equip_item, drop_item, get_quest_details, toggle_starred, abandon_quest
from handlers.logic.options import Options, encounter_window_options, reward_options, OptionsFake, \
    settings_options, shop_base_categories
from handlers.menus.journal import Quest
from screens.title_screen import get_title_menu


class OptionsHandler(MVC):

    def __init__(self):
        self.current = None

    @staticmethod
    def wrap(options, fake=None):
        if fake:
            return OptionsFake(options, fake)
        else:
            return Options(options)

    def get(self, component=None):
        if component is None:
            self.current = self.mapping()
        else:
            self.current = MenuMaker.make(component)


    def traverse(self, path):
        if self.state == GameStates.TITLE:
            self.traverse_list(path)
        elif self.state == GameStates.DIALOGUE:
            return self.traverse_graph(path)
        elif self.owner.state == GameStates.SHOP and self.handler.state == ShopStates.BASE:
            self.traverse_list((path[0]))
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and self.handler.menu_type.submenu is None:
            self.current.traverse_list(path[0])
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY):
            self.current.traverse_list(path[1])
        elif self.handler.state == EncounterStates.THINKING:
            self.traverse_list(path[1])
        elif self.handler.state == EncounterStates.FIGHT_TARGETING:
            self.traverse_combat(path)
        elif self.handler.state == RewardStates.THINKING:
            self.traverse_list(path)

    def traverse_combat(self, path):
        x, y = path
        if x != 0:
            self.traverse_combat_rows(x)
        else:
            self.traverse_combat_columns(y)

    def traverse_combat_rows(self, x):
        viable = True
        current_x = self.current.x
        while viable:
            current_x += x
            if current_x < 0 or current_x == len(self.current.rows):
                viable = False
            else:
                col = self.current.rows[current_x]
                if len(col) > 0:
                    self.current.x = current_x
                    self.current.y = 0
                    viable = False

    def traverse_combat_columns(self, y):
        if (y < 0 and self.current.y == 0) or (y > 0 and self.current.y >= (len(self.current.rows[self.current.y]))):
            pass
        else:
            self.current.y += y

    def traverse_list(self, amount):

        if (amount < 0 and self.current.choice == 0) or (amount > 0 and self.current.choice >=
                                                         (len(self.current.options) - 1)):
            pass
        else:
            self.current.choice += amount

    def traverse_graph(self, path):
        key = chr(path)
        changes = []

        if key in self.handler.real_io.keys():
            self.current.conversation = self.handler.real_io.get(key)
            current_node = self.current.graph_dict.get(self.current.conversation)
            current_node.visited = True
            self.handler.set_real_talk()
            self.handler.broadcast_choice(current_node.signal)

            if self.current.conversation == 'exit':
                self.current.conversation = 'root'
                changes.append({'state': 'life'})
                self.current = None
            elif self.current.conversation == 'shop':
                self.current.conversation = 'root'
                shopkeeper = self.owner.dialogue.partner
                changes.append({'state': 'shop'})
                changes.append({'snapshot': True})
                self.current = shop_base_categories()
                self.owner.shop.shopkeeper = shopkeeper
        return changes

    def choose(self):
        if self.handler.state is EncounterStates.VICTORY:
            option = GoToReward
        elif isinstance(self.current, CombatGrid):
            option = AttackMob
        elif isinstance(self.current, OptionsFake):
            option = self.current.fake
        else:
            option = self.current.options[self.current.choice]

        return option.logic

    def title(self):
        return get_title_menu()

    def life(self):
        pass

    def menus(self):
        menus = {
            MenuStates.CHAR_SHEET: self.wrap([]),
            MenuStates.INVENTORY: self.owner.party.inventory.menu,
            MenuStates.JOURNAL: self.owner.party.journal.menu,
            MenuStates.MAP: self.wrap([]),
            MenuStates.SETTINGS: settings_options(),
        }
        return menus.get(self.handler.state)

    def dialogue(self):
        pass

    def shop(self):
        return shop_base_categories()

    def encounter(self):
        encounter = {
            EncounterStates.THINKING: encounter_window_options(),
            EncounterStates.FIGHT_TARGETING: self.owner.encounter.combat.grid,
        }
        return encounter.get(self.handler.state)

    def reward(self):
        reward = {
            RewardStates.THINKING: reward_options(),
            RewardStates.SIFTING: self.wrap(self.owner.reward.loot.items, fake=RewardSifting),
            RewardStates.DEPOSITING: self.wrap(self.owner.reward.loot.claimed, fake=RewardDepositing),
        }
        return reward.get(self.handler.state)

    def debug(self):
        pass


class MenuMaker:
    """Contains a variety of static methods for making menus on demand."""

    @staticmethod
    def make(component):
        component_class_func_dict = {Item: MenuMaker.make_item_menu, Quest: MenuMaker.make_quest_menu}
        make_func = component_class_func_dict.get(component.__class__)
        menu = make_func(component)
        return menu

    @staticmethod
    def make_item_menu(component):
        data, logic = MenuMaker.get_item_menu_datalogic(component)
        BG_WIDTH = 80
        BG_HEIGHT = 24 * len(data)
        bg = get_alpha_surface(BG_WIDTH, BG_HEIGHT)
        bg.blit(scale(DIALOGUE_BG, (BG_WIDTH, BG_HEIGHT)), (0, 0))
        pointer_image = get_alpha_surface(16, 16)
        pointer_image.blit(scale(POINTER_RIGHT, (16, 16)), (0, 0))
        specs = MenuSpecs(bg=bg, pointer_image=pointer_image, pointer_y_offset=8, font_size=16, pointer_delta=20,
                          button_x_offset=12, button_y_offset=4)
        return BasicMenu(data, logic, specs)


    @staticmethod
    def get_item_menu_datalogic(component):
        logic = []
        data = []
        if component.equippable:
            logic.extend([attempt_equip_item])
            data.append('Equip')
        if component.useable:
            logic.extend([UseItem])
            data.append('Use')
        logic.extend([ExamineItem])
        data.append('Examine')
        if not component.important:
            logic.extend([drop_item])
            data.append('Drop')
        return data, logic

    @staticmethod
    def make_quest_menu(quest):
        logic = [get_quest_details, toggle_starred]
        data = ['Quest Details']
        if quest.starred:
            data.append('Mark As Unimportant')
        else:
            data.append('Mark As Important')
        if not quest.part_of_main_storyline:
            logic.extend([abandon_quest])
            data.append('Abandon Quest')
        BG_WIDTH = 150
        BG_HEIGHT = 24 * len(data)
        bg = get_alpha_surface(BG_WIDTH, BG_HEIGHT)
        bg.blit(scale(DIALOGUE_BG, (BG_WIDTH, BG_HEIGHT)), (0, 0))
        pointer_image = get_alpha_surface(16, 16)
        pointer_image.blit(scale(POINTER_RIGHT, (16, 16)), (0, 0))
        specs = MenuSpecs(bg=bg, pointer_image=pointer_image, pointer_y_offset=8, font_size=16, pointer_delta=20,
                          button_x_offset=12, button_y_offset=4)
        return BasicMenu(data, logic, specs)



