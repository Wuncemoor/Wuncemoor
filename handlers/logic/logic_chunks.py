from ECS.entity import Entity
from abstracts.abstract_logic import AbstractLogic
from config.constants import DARK_BLUE, DARK_ORANGE, BLACK, WHITE, SCREEN_SIZE, MIDNIGHT_BLUE, DARK_PURPLE, RED
from abstracts.abstract_menu import AbstractMenu
from enums.game_states import EncounterStates, RewardStates, GameStates, ShopStates
from handlers.party_handler import PartyHandler
from handlers.views.messages import Message
from loader_functions.data_loaders import load_game
from loader_functions.new_game_functions import make_new_game_model
import pygame as py


def new_game(mvc):
    model = make_new_game_model()
    mvc.game.preplay(model)


def load_game(mvc):
    world, party = load_game()
    mvc.game.preplay(world, party)


def goto_settings(mvc):
    mvc.game.quit()


def goto_acknowledgements(mvc):
    mvc.game.quit()


def quit_game(mvc):
    mvc.game.quit()


def life_attempt_party_move(self, output):
    changes = [{'party_facing': output}]
    dx, dy = output
    destination_x = self.game.model.party.x + dx
    destination_y = self.game.model.party.y + dy
    tile = self.game.model.world.current_map.tiles[destination_y][destination_x]

    if not tile.blocker:
        changes.append({'party_move': output})

        if tile.floor.has_transition():
            transition = tile.floor.transition
            world = self.game.model.world
            new_dungeon = world.dungeons[transition.go_to_dungeon]
            if world.current_dungeon.name != transition.go_to_dungeon:
                changes.append({'new_current_dungeon': new_dungeon})

            new_map = new_dungeon.maps[transition.go_to_floor]
            changes.append({'new_current_map': new_map})
            changes.append({'party_teleport': transition})

        elif self.game.model.world.dangerous:
            changes.append({'dangerous_move': tile})
    return changes


def interact(self):
    changes = []
    changes.extend(attempt_pickup_item(self.game.model.party, self.game.model.world.current_map.items))

    for entity in self.game.model.world.current_map.conversers:
        if entity.x == self.game.model.party.x and entity.y == self.game.model.party.y:
            self.game.dialogue.partner = entity
            self.game.dialogue.set_real_talk()
            self.game.state_handler = self.game.dialogue
            self.game.options.current = entity.converser.dialogue
    if len(changes) == 0:
        message = Message('Nothing to see here, move along...', DARK_BLUE)
        changes.append({'message': message})
    return changes


def attempt_pickup_item(party, entities):
    changes = []
    for entity in entities:
        if entity.x == party.x and entity.y == party.y and (party.inventory.unused_carry_capacity >= entity.mass):
            message = Message('{0} added to party inventory!'.format(entity.name), DARK_PURPLE)
            changes.extend([{'pickup_item': entity}, {'message': message}])
            break
    if len(entities) > 0 and len(changes) == 0:
        message = Message("That's too heavy! Get rid of some things or get stronger!", RED)
        changes.extend([{'message': message}])
    return changes


def life_goto_menus(obj):
    return [{'state': 'menus'}, {'substate': obj}]


def shop_base_goto_sub(self):
    player_sub, shop_sub = self.handler.get_subinventories(self.game.options.current.choice)
    if len(shop_sub) > 0:
        changes = [{'substate': ShopStates.BUYING}]
        self.handler.sub_index = self.game.options.current.choice
        self.game.options.wrap_and_set(shop_sub)
    elif len(player_sub) > 0:
        changes = [{'substate': ShopStates.SELLING}]
        self.handler.sub_index = self.game.options.current.choice
        self.game.options.wrap_and_set(player_sub)
    elif len(self.handler.transaction_details) > 0:
        changes = [{'substate': ShopStates.TRANSACTING}]
        self.handler.sub_index = self.game.options.current.choice
        self.game.options.wrap_and_set(self.handler.transaction_details)
    else:
        changes = []
    return changes


def encounter_choose_option(self):

    state_to_func_dict = {
        EncounterStates.THINKING: self.handler.menu.pointer_logic,
        EncounterStates.FIGHT_TARGETING: basic_weapon_attack,
        EncounterStates.VICTORY: encounter_goto_reward,
    }

    func = state_to_func_dict.get(self.handler.state)

    return func(self)


def encounter_goto_targeting(self):
    return [{'substate': EncounterStates.FIGHT_TARGETING}]


def encounter_goto_satchel(self):
    return []


def encounter_goto_life(self):
    changes = [{'state': 'life'}]
    xp = self.handler.loot.xp
    if xp > 0:
        changes.append({'xp': xp})
        message = Message('You gain {0} experience points!'.format(xp), DARK_ORANGE)
    else:
        message = Message("You didn't learn much there...", DARK_ORANGE)
    changes.append({'message': message})

    return changes


def encounter_goto_thinking(self):
    if self.handler.state is EncounterStates.FIGHT_TARGETING:
        changes = [{'substate': EncounterStates.THINKING}]
    else:
        changes = []
    return changes


def basic_weapon_attack(self):
    changes = []
    combat = self.handler.combat
    x, y = combat.grid.x, combat.grid.y
    attack_results = combat.party.p1.combatant.attack(combat.grid.rows[x][y])
    changes.extend(attack_results)
    return changes


def encounter_end_turn(self):
    changes = []
    if len(self.handler.combat.enemies.members) > 0:
        if self.handler.state is EncounterStates.ENEMY_TURN:
            changes.append({'substate': EncounterStates.THINKING})
        else:
            changes.append({'substate': EncounterStates.ENEMY_TURN})
            changes.append({'automate': 'enemy_turn'})
    else:
        changes.append({'message': Message('YOU WIN THE FIGHT!', BLACK)})
        changes.append({'message': Message('Press [Enter] to loot.', BLACK)})
        changes.append({'substate': EncounterStates.VICTORY})
    return changes


def encounter_enemy_turn(self):
    player = self.handler.combat.party.p1
    changes = self.handler.combat.enemies.p1.combatant.ai.take_turn(player)
    changes.append({'substate': EncounterStates.THINKING})
    return changes


def encounter_goto_reward(self):
    return [{'state': 'reward'}, {'substate': RewardStates.THINKING}]


def reward_auto(self):
    self.handler.loot.claimed.extend(self.handler.loot.items)
    self.handler.loot.items = []
    self.game.options.current.choice = 2
    return []


def reward_manual(self):
    loot = self.handler.loot
    if (len(loot.items) + len(loot.claimed)) > 0:
        if len(loot.items) > 0:
            changes = [{'substate': RewardStates.SIFTING}]
        else:
            changes = [{'substate': RewardStates.DEPOSITING}]
    else:
        changes = []
    return changes


def reward_goto_life(self):
    loot = self.handler.loot
    changes = [{'xp': loot.xp}]
    self.game.model.party.inventory.take_loot(loot.claimed)
    self.game.options.current.choice = 0

    changes.append({'state': 'life'})
    return changes


def reward_sifting(self):
    changes = []
    loot = self.handler.loot
    loot.claim(self.game.options.current.choice)
    if len(loot.items) == 0:
        changes.append({'substate': RewardStates.THINKING})
        changes.append({'set_choice': 2})
    elif self.game.options.current.choice > len(loot.items) - 1:
        self.game.options.current.choice -= 1
    return changes


def reward_depositing(self):
    changes = []
    loot = self.handler.loot
    loot.unclaim(self.game.options.current.choice)
    if len(loot.claimed) == 0:
        changes.append({'substate': RewardStates.SIFTING})
    elif self.game.options.current.choice > len(loot.claimed) - 1:
        self.game.options.current.choice -= 1
    return changes


def reward_toggle(self, direction):
    changes = []
    loot = self.handler.loot
    if self.handler.state == RewardStates.SIFTING and direction == 'right' and len(loot.claimed) > 0:
        changes.append({'substate': RewardStates.DEPOSITING})
    elif self.handler.state == RewardStates.DEPOSITING and direction == 'left' and len(loot.items) > 0:
        changes.append({'substate': RewardStates.SIFTING})
    return changes


class RewardExit(AbstractLogic):

    def logic(self):
        changes = []
        state = self.handler.state
        if state in (RewardStates.SIFTING, RewardStates.DEPOSITING):
            changes.append({'substate': RewardStates.THINKING})
        elif state == RewardStates.THINKING and self.game.options.current.choice == 2:
            changes.extend(RewardToLife.logic(self))
        elif state == RewardStates.THINKING:
            self.game.options.current.choice = 2
        return changes


class Debug(AbstractLogic):

    def logic(self):
        changes = [{'state': 'debug'}]
        return changes


class DebugExit(AbstractLogic):

    def logic(self, prev):
        string_dict = {
            GameStates.TITLE: 'title',
            GameStates.LIFE: 'life',
            GameStates.MENUS: 'menus',
            GameStates.ENCOUNTER: 'encounter',
            GameStates.REWARD: 'reward',
            GameStates.DIALOGUE: 'dialogue',
        }
        changes = [{'state': string_dict.get(prev)}]
        return changes


class DebugAttemptCommand(AbstractLogic):

    def logic(self):
        changes = [{'debug_message': Message('Command entered: ' + self.handler.current_input, WHITE)}]
        try:
            exec(self.handler.current_input, self.handler.allowed_inputs)
            changes.append({'debug_message': Message('COMMAND ACCEPTED', WHITE)})
            for message in self.handler.message_slot:
                changes.append({'debug_message': message})
            self.handler.current_input = ''
        except NameError:
            changes.append({'debug_message': Message('COMMAND NOT RECOGNIZED', WHITE)})

        return changes


class ShopExit(AbstractLogic):

    def logic(self):
        if self.handler.state == ShopStates.BASE:
            changes = [{'state': 'life'}]
        elif self.handler.state in (ShopStates.BUYING, ShopStates.SELLING, ShopStates.TRANSACTING):
            changes = [{'substate': ShopStates.BASE}]
        return changes


class FullscreenToggle(AbstractLogic):

    def logic(self):

        if self.game.fullscreen:
            self.game.screen = py.display.set_mode(SCREEN_SIZE)
            self.game.fullscreen = False
        else:
            self.game.screen = py.display.set_mode(SCREEN_SIZE, flags=py.FULLSCREEN)
            self.game.fullscreen = True


def attempt_equip_item(party: PartyHandler, menu: AbstractMenu):
    slot = menu.pointer_data.item.equippable.slot
    currently_equipped = party.p1.combatant.equipment.slots_dict.get(slot)
    changes = []
    if currently_equipped:
        # check weight limit later
        changes.append({'dequipped': slot})
    changes.append({'equipped': menu})
    message = Message('{0} equipped the {1}!'.format(party.p1.name, menu.pointer_data.name), MIDNIGHT_BLUE)
    changes.append({'message': message})
    changes.append({'subsubstate': 2})
    return changes


def drop_item(party: PartyHandler, menu: AbstractMenu):
    message = Message('{0} was dropped on the ground.'.format(menu.pointer_data.name), BLACK)
    return [{'drop_item': menu}, {'message': message}, {'subsubstate': 2}]


def examine_item(party: PartyHandler, menu: AbstractMenu):
    return [{'subsubstate': 4}]


class UseItem(AbstractLogic):
    pass


class DropItem(AbstractLogic):
    pass


def get_quest_details(party, menu):
    return []


def toggle_starred(party, menu):
    return []


def abandon_quest(party, menu):
    return []