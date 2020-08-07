from abstracts.abstract_mvc import MVC
from handlers.logic.logic_chunks import Move, Interact, MenusToggle, MenusExit, EncounterExit, EndTurn, EnemyTurn, \
    RewardToggle, RewardExit, LifeToMenus, Debug, DebugExit, DebugAttemptCommand


class LogicHandler(MVC):

    def __init__(self):
        self.response = None

    def translate(self, output):
        self.mapping(output)

    def debug(self, output):
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

        if 'traverse_menu' in output:
            self.owner.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.owner.options.choose()
            self.response(self)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def life(self, output):

        if 'move' in output:
            self.response = Move.logic
            self.response(self, output.get('move'))
        elif 'interact' in output:
            self.response = Interact.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'show_menus' in output:
            self.response = LifeToMenus.logic
            changes = self.response(self, output.get('show_menus'))
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def menus(self, output):
        if 'exit' in output:
            self.response = MenusExit.logic
            self.response(self)
        elif 'show_menus' in output:
            self.response = MenusToggle.logic
            changes = self.response(self, output.get('show_menus'))
            self.mutate(changes)
        elif 'traverse_menu' in output:
            self.owner.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            if self.handler.menu.sub is None:
                self.response = self.owner.options.choose()
                self.response(self)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def dialogue(self, output):
        if 'converse' in output:
            self.owner.options.traverse(output.get('converse'))
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def encounter(self, output):
        if 'traverse_menu' in output:
            self.owner.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.owner.options.choose()
            changes = self.response(self)
            self.mutate(changes)
        if 'exit' in output:
            self.response = EncounterExit.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'debug' in output:
            self.response = Debug.logic
            changes = self.response(self)
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def reward(self, output):
        if 'traverse_menu' in output:
            self.owner.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.owner.options.choose()
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
            prev = self.owner.state
            self.mutate(changes)
            self.owner.state_handler.previous_state = prev

    def mutate(self, changes):
        for change in changes:
            if 'debug_message' in change:
                self.owner.log.debugger.add_message(change.get('debug_message'))
            elif 'message' in change:
                self.owner.log.messages.add_message(change.get('message'))
            elif 'item_added' in change:
                self.owner.world.current_map.entities.remove(change.get('item_added'))
            elif 'substate' in change:
                self.handler.change_state(change.get('substate'))
            elif 'state' in change:
                self.owner.change_state(change.get('state'))
            elif 'xp' in change:
                self.owner.party.p1.combatant.level.add_xp(change.get('xp'))
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
                self.owner.options.current.choice = change.get('set_choice')





