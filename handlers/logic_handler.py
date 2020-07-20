from enums.game_states import GameStates
from handlers.logic.logic_chunks import Move, Interact, MenusToggle, MenusExit, EncounterExit, EndTurn, EnemyTurn, \
    RewardToggle, RewardExit, LifeToMenus


class LogicHandler:

    def __init__(self):
        self.response = None

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.reward,
        }
        return maps.get(self.state)

    @property
    def handler(self):
        return self.owner.state_handler

    def translate(self, output):
        self.mapping(output)

    def title(self, output):

        if 'traverse_menu' in output:
            self.owner.options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = self.owner.options.choose()
            self.response(self)

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

    def dialogue(self, output):
        if 'converse' in output:
            self.owner.options.traverse(output.get('converse'))

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

    def mutate(self, changes):
        for change in changes:
            if 'message' in change:
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





