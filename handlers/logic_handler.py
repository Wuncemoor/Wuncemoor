from abstracts.abstract_mvc import MVC
from handlers.logic.logic_chunks import life_attempt_party_move, RewardExit, Debug, DebugExit, DebugAttemptCommand, \
    ShopExit, \
    FullscreenToggle, life_goto_menus, \
    interact, encounter_end_turn, encounter_enemy_turn, encounter_goto_thinking, encounter_choose_option
from handlers.logic.menus_logic import menus_exit, menus_toggle


class LogicHandler(MVC):

    def __init__(self, game):
        super().__init__(game)
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
            self.response = life_attempt_party_move
            changes = self.response(self, output.get('move'))
            self.mutate(changes)
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
                changes = self.response(self.game.model.party, self.handler.menu_type.submenu)
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
            self.response = encounter_choose_option
            changes = self.response(self)
            self.mutate(changes)
        if 'exit' in output:
            self.response = encounter_goto_thinking
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
            self.response = self.game.options.current.pointer_logic
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
                self.game.model.log.debugger.add_message(change.get('debug_message'))
            elif 'message' in change:
                self.game.model.log.messages.add_message(change.get('message'))
            elif 'pickup_item' in change:
                item = change.get('pickup_item')
                self.game.model.party.inventory.add_item(item)
                self.game.model.world.current_map.entities.remove(item)
            elif 'drop_item' in change:
                menu = change.get('drop_item')
                item = menu.pop_pointer()
                item.x, item.y = self.game.model.party.x, self.game.model.party.y
                self.game.model.world.current_map.entities.append(item)
            elif 'dequipped' in change:
                item = self.game.model.party.p1.combatant.equipment.unequip(change.get('dequipped'))
                self.game.model.party.inventory.add_item(item)
            elif 'equipped' in change:
                menu = change.get('equipped')
                item = menu.pop_pointer()
                self.game.model.party.p1.combatant.equipment.equip(item)
            elif 'subsubstate' in change:
                self.handler.menu_type.change_state(change.get('subsubstate'), self.game.options)
            elif 'substate' in change:
                self.handler.change_state(change.get('substate'), self.game.options)
            elif 'state' in change:
                self.game.change_state(change.get('state'))
            elif 'xp' in change:
                self.game.model.party.p1.combatant.level.add_xp(change.get('xp'))
            elif 'dead' in change:
                entity = change.get('dead')
                self.handler.combat.destroy(entity)
                self.handler.loot.dissect(entity)
            elif 'end_turn' in change:
                self.response = encounter_end_turn
                changes = self.response(self)
                self.mutate(changes)
            elif 'automate' in change:
                self.response = encounter_enemy_turn
                changes = self.response(self)
                self.mutate(changes)
            elif 'set_choice' in change:
                self.game.options.current.choice = change.get('set_choice')
            elif 'snapshot' in change:
                self.handler.take_snapshot()
            elif 'party_facing' in change:
                self.game.model.party.change_direction(change.get('party_facing'))
            elif 'party_move' in change:
                self.game.model.party.move(change.get('party_move'))
                self.handler.camera.refocus(self.game.model.party.x, self.game.model.party.y)
                self.handler.fov.needs_recompute = True
            elif 'party_teleport' in change:
                self.game.model.party.teleport(change.get('party_teleport').go_to_xy)
                self.handler.camera.refocus(self.game.model.party.x, self.game.model.party.y)
                self.handler.fov.map = self.handler.fov.initialize(self.game.model.world)
                self.handler.fov.needs_recompute = True
            elif 'new_current_dungeon' in change:
                new_dungeon = change.get('new_current_dungeon')
                self.game.model.world.current_dungeon.time_dilation = self.game.model.time.stamp()
                self.game.model.time.apply_dilation(new_dungeon)
                self.game.model.world.current_dungeon = new_dungeon
            elif 'new_current_map' in change:
                self.game.model.world.current_map = change.get('new_current_map')
                self.handler.fov.map = self.handler.fov.initialize(self.game.model.world)
                self.handler.fov.needs_recompute = True
            elif 'dangerous_move' in change:
                self.game.model.time.goes_on()
                changes = self.game.encounter.check_for_encounter(change.get('dangerous_move'))
                self.mutate(changes)
            elif 'new_encounter' in change:
                self.mutate([{'state': 'encounter'}])
                self.handler.new_encounter(change.get('new_encounter'), self.game.options)





