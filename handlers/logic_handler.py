from abstracts.abstract_mvc import MVC
from handlers.logic.logic_chunks import Move, EncounterExit, EndTurn, EnemyTurn, \
    RewardToggle, RewardExit, Debug, DebugExit, DebugAttemptCommand, ShopExit, FullscreenToggle, life_goto_menus, \
    interact
from handlers.logic.menus_logic import menus_exit, menus_toggle


class LogicHandler(MVC):

    def __init__(self):
        self.response = None

    def translate(self, output):
        self.mapping(output)

    def debug(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        if 'exit' in output:
            self.response = DebugExit.logic
            changes = self.response(self, self.handler.previous_state)
            self.mutate(changes)
        elif 'command_send' in output:
            self.response = DebugAttemptCommand.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'command_pop' in output:
            self.handler.current_input = self.handler.current_input[:-1]
        elif 'command_extend' in output:
            self.handler.current_input += output.get('command_extend')

    def title(self, output):

        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'traverse_menu' in output:
            self.game.title.menu.traverse_list(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.game.title.menu.logic[self.game.title.menu.pointer]
            self.response(self)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def life(self, output):

        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'move' in output:
            self.response = Move.logic
            self.response(self, output.get('move'))
        elif 'interact' in output:
            self.response = interact
            changes = self.response(self)
            self.mutate(changes)
        elif 'show_menus' in output:
            self.response = life_goto_menus
            changes = self.response(output.get('show_menus'))
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def menus(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'exit' in output:
            self.response = menus_exit
            changes = self.response(self)
            self.mutate(changes)
        elif 'show_menus' in output:
            self.response = menus_toggle
            changes = self.response(self, output.get('show_menus'))
            self.mutate(changes)
        elif 'traverse_menu' in output:
            self.game.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            if self.handler.menu_type.state == self.handler.menu_type.state.__class__(1):
                self.response = self.handler.menu_type.menu.logic
                changes = self.response(self)
            elif self.handler.menu_type.state == self.handler.menu_type.state.__class__(2):
                self.response = self.handler.menu_type.submenu.logic
                changes = self.response()
            elif self.handler.menu_type.state == self.handler.menu_type.state.__class__(3):
                self.response = self.game.options.current.logic[self.game.options.current.pointer]
                changes = self.response(self.game.party, self.handler.menu_type.submenu)
            self.mutate(changes)

        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def dialogue(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'converse' in output:
            changes = self.game.options.traverse(output.get('converse'))
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def shop(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'exit' in output:
            self.response = ShopExit.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'traverse_menu' in output:
            self.game.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            if self.handler.sub_index is None:
                self.response = self.game.options.choose()
                changes = self.response(self)
                self.mutate(changes)

    def encounter(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'traverse_menu' in output:
            self.game.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.game.options.choose()
            changes = self.response(self)
            self.mutate(changes)
        if 'exit' in output:
            self.response = EncounterExit.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def reward(self, output):
        if 'fullscreen' in output:
            self.response = FullscreenToggle.logic
            self.response(self)
        elif 'traverse_menu' in output:
            self.game.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.game.options.choose()
            changes = self.response(self)
            self.mutate(changes)
        elif 'toggle' in output:
            self.response = RewardToggle.logic
            changes = self.response(self, output.get('toggle'))
            self.mutate(changes)
        elif 'exit' in output:
            self.response = RewardExit.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.game.state
            self.mutate(changes)
            self.game.state_handler.previous_state = prev

    def mutate(self, changes):
        for change in changes:
            if 'debug_message' in change:
                self.game.log.debugger.add_message(change.get('debug_message'))
            elif 'message' in change:
                self.game.log.messages.add_message(change.get('message'))
            elif 'pickup_item' in change:
                item = change.get('pickup_item')
                self.game.party.inventory.add_item(item)
                self.game.world.current_map.entities.remove(item)
            elif 'drop_item' in change:
                menu = change.get('drop_item')
                item = menu.pop_pointer()
                item.x, item.y = self.game.party.x, self.game.party.y
                self.game.world.current_map.entities.append(item)
            elif 'dequipped' in change:
                item = self.game.party.p1.combatant.equipment.unequip(change.get('dequipped'))
                self.game.party.inventory.add_item(item)
            elif 'equipped' in change:
                menu = change.get('equipped')
                item = menu.pop_pointer()
                self.game.party.p1.combatant.equipment.equip(item)
            elif 'subsubstate' in change:
                self.handler.menu_type.state = self.handler.menu_type.state.__class__(change.get('subsubstate'))
                self.handler.menu_type.change_state(change.get('subsubstate'), self.game.options)
            elif 'substate' in change:
                self.handler.change_state(change.get('substate'), self.game.options)
            elif 'state' in change:
                self.game.change_state(change.get('state'))
            elif 'xp' in change:
                self.game.party.p1.combatant.level.add_xp(change.get('xp'))
            elif 'dead' in change:
                entity = change.get('dead')
                self.handler.combat.destroy(entity)
                self.handler.loot.dissect(entity)
            elif 'end_turn' in change:
                self.response = EndTurn.logic
                changes = self.response(self)
                self.mutate(changes)
            elif 'automate' in change:
                self.response = EnemyTurn.logic
                changes = self.response(self)
                self.mutate(changes)
            elif 'set_choice' in change:
                self.game.options.current.choice = change.get('set_choice')
            elif 'snapshot' in change:
                self.handler.take_snapshot()






