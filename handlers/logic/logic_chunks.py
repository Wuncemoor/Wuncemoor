from abc import ABC, abstractmethod
from config.constants import DARK_BLUE, DARK_ORANGE
from enums.game_states import GameStates, EncounterStates
from handlers.views.messages import Message
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class Logic(ABC):

    @abstractmethod
    def logic(self):
        pass


class Option(Logic):

    @property
    @abstractmethod
    def text(self):
        pass


class NewGame(Option):

    text = 'Start A New Game'

    def logic(self):
        dungeons, world, overworld_tiles, party = get_game_variables()
        self.owner.preplay(dungeons, world, overworld_tiles, party)


class LoadGame(Option):

    text = 'Continue A Previous Game'

    def logic(self):
        dungeons, world, overworld_tiles, party = load_game()
        self.owner.preplay(dungeons, world, overworld_tiles, party)


class QuitGame(Option):

    text = 'Quit'

    def logic(self):
        self.owner.quit()


class Move(Logic):

    def logic(self, output):
        dx, dy = output
        x, y = self.owner.party.x, self.owner.party.y
        destination_x = x + dx
        destination_y = y + dy

        if not self.owner.world.is_blocked(destination_x, destination_y):

            self.owner.party.move(dx, dy)
            self.handler.camera.refocus(x, y)

            self.handler.fov.needs_recompute = True

            if self.owner.world.dangerous:
                self.owner.time.goes_on()
                tile = self.owner.world.tiles[destination_x][destination_y]
                self.owner.encounter.check(tile)


class Interact(Logic):

    def logic(self):
        nothing = True
        changes = []
        world = self.owner.world
        for entity in world.current_map.entities:
            if entity.x == self.owner.party.x and entity.y == self.owner.party.y:
                if entity.item:
                    pickup_results = self.owner.party.inventory.add_item(entity)
                    changes.extend(pickup_results)
                    nothing = False
                    break
        for transition in world.current_map.transitions:
            if transition.x == self.owner.party.x and transition.y == self.owner.party.y:
                new_dungeon = self.owner.dungeons[transition.transition.go_to_dungeon]
                if world.current_dungeon.name != transition.transition.go_to_dungeon:
                    world.current_dungeon.time_dilation = self.owner.time.stamp()
                    self.owner.time.apply_dilation(new_dungeon)
                    world.current_dungeon = new_dungeon

                new_map = new_dungeon.maps[transition.transition.go_to_floor]
                world.current_map = new_map
                self.owner.party.x, self.owner.party.y = transition.transition.go_to_xy[0], transition.transition.go_to_xy[1]
                self.handler.camera.refocus(self.owner.party.x, self.owner.party.y)

                self.handler.fov.map = self.handler.fov.initialize(world)
                self.handler.fov.needs_recompute = True
                nothing = False
                break
        for noncom in world.current_map.noncombatants:
            if noncom.x == self.owner.party.x and noncom.y == self.owner.party.y:
                self.owner.dialogue.partner = noncom
                self.owner.dialogue.set_real_talk()
                self.owner.state_handler = self.owner.dialogue
                self.owner.options.current = noncom.noncombatant.dialogue
                nothing = False
        if nothing:
            self.owner.log.messages.add_message(Message('Nothing to see here, move along...', DARK_BLUE))
        return changes


class ShowMenus(Logic):

    def logic(self, output):
        opts = {
            'inventory': self.owner.party.inventory,
            'journal': self.owner.party.journal,
            'party': self.owner.party,
            'map': self.owner.party.map,
        }
        if self.handler is self.owner.menus:
            if opts.get(output) is self.handler.menu:
                self.handler.menu.sub = None
                self.owner.options.current = None
                self.owner.state_handler = self.owner.life
            else:
                self.owner.menus.handle_menu(opts.get(output))
                self.owner.options.current = self.handler.menu.options
        else:
            self.owner.state_handler = self.owner.menus
            self.owner.menus.handle_menu(opts.get(output))


class MenusExit(Logic):

    def logic(self):
        if self.handler.menu.sub is None:
            self.owner.state_handler = self.owner.life
        else:
            self.handler.menu.sub = None
            self.owner.options.current = self.handler.menu.options


class GoToSubJournal(Logic):

    def logic(self):
        sub = self.owner.party.journal.get_subjournal()
        if len(sub) > 0:
            self.handler.menu.sub = sub
            self.owner.options.wrap_and_set(sub)


class GoToSubInventory(Logic):

    def logic(self):
        sub = self.owner.party.inventory.get_subinventory()
        if len(sub) > 0:
            self.handler.menu.sub = sub
            self.owner.options.wrap_and_set(sub)


class FightTargeting(Option):

    text = 'FIGHT'

    def logic(self):
        changes = [{'substate': 'fight_targeting'}]
        return changes


class EncounterExit(Logic):

    def logic(self):
        if self.handler.state is EncounterStates.FIGHT_TARGETING:
            changes = [{'substate': 'thinking'}]
        else:
            changes = []
        return changes


class UseSatchel(Option):

    text = 'ITEM'

    def logic(self):
        pass

class RunAway(Option):

    text = 'RUN'

    def logic(self):
        changes = [{'state': 'life'}]
        xp = self.handler.loot.xp
        if xp > 0:
            changes.append({'xp': xp})
            message = Message('You gain {0} experience points!'.format(xp), DARK_ORANGE)
        else:
            message = Message("You didn't learn much there...", DARK_ORANGE)
        changes.append({'message': message})

        return changes
