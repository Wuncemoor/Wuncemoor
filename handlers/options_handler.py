from enums.game_states import GameStates, MenuStates, EncounterStates, RewardStates, ShopStates
from abstracts.abstract_mvc import MVC
from handlers.encounter.combat import CombatGrid
from handlers.logic.logic_chunks import AttackMob, GoToReward, RewardSifting, RewardDepositing
from handlers.logic.options import title_options, Options, encounter_window_options, reward_options, OptionsFake, \
    settings_options, shop_base_categories


class OptionsHandler(MVC):

    def __init__(self):
        self.current = None


    @staticmethod
    def wrap(options, fake=None):
        if fake:
            return OptionsFake(options, fake)
        else:
            return Options(options)

    def wrap_and_set(self, options):
        self.current = self.wrap(options)

    def get(self, case=None):
        if case is None:
            self.current = self.mapping()
        elif case == 'sub':
            pass

    def traverse(self, path):
        if self.state == GameStates.TITLE:
            self.traverse_list(path)
        elif self.state == GameStates.DIALOGUE:
            return self.traverse_graph(path)
        elif self.owner.state == GameStates.SHOP and self.handler.state == ShopStates.BASE:
            self.traverse_list((path[0]))
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and self.handler.menu_type.sub is None:
            self.traverse_list(path[0])
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY):
            self.traverse_list(path[1])
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
        return title_options()

    def life(self):
        pass

    def menus(self):
        menus = {
            MenuStates.PARTY: self.wrap([]),
            MenuStates.INVENTORY: self.owner.party.inventory.options,
            MenuStates.JOURNAL: self.owner.party.journal.options,
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




