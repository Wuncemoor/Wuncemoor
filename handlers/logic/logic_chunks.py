from abc import ABC, abstractmethod
from config.constants import DARK_BLUE, DARK_ORANGE, BLACK
from enums.game_states import EncounterStates, RewardStates
from handlers.views.messages import Message
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class Logic(ABC):

    @abstractmethod
    def logic(self):
        pass


class NewGame(Logic):

    def logic(self):
        world, party = get_game_variables()
        self.owner.preplay(world, party)


class LoadGame(Logic):

    def logic(self):
        world, party = load_game()
        self.owner.preplay(world, party)


class QuitGame(Logic):

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
                new_dungeon = self.owner.world.dungeons[transition.transition.go_to_dungeon]
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


class MenusToggle(Logic):

    def logic(self, output):

        if self.handler.menu is output:
            return MenusSubToLife.logic(self)
        else:
            return MenusToMenus.logic(self, output)


class LifeToMenus(Logic):

    def logic(self, obj):
        return [{'state': 'menus'}, {'substate': obj}]


class MenusToMenus(Logic):

    def logic(self, obj):
        return [{'substate': obj}]


class MenusSubToLife(Logic):

    def logic(self):
        self.handler.menu.sub = None
        return [{'state': 'life'}]


class MenusExit(Logic):

    def logic(self):
        if self.handler.menu.sub is None:
            self.owner.state_handler = self.owner.life
        else:
            self.handler.menu.sub = None
            self.owner.options.current = self.handler.menu.options


class MenuGoToSub(Logic):

    def logic(self):
        sub = self.handler.menu.get_sub()
        if len(sub) > 0:
            self.handler.menu.sub = sub
            self.owner.options.wrap_and_set(sub)


class FightTargeting(Logic):

    def logic(self):
        changes = [{'substate': EncounterStates.FIGHT_TARGETING}]
        return changes


class EncounterExit(Logic):

    def logic(self):
        if self.handler.state is EncounterStates.FIGHT_TARGETING:
            changes = [{'substate': EncounterStates.THINKING}]
        else:
            changes = []
        return changes


class UseSatchel(Logic):

    def logic(self):
        pass


class RunAway(Logic):

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


class AttackMob(Logic):

    def logic(self):
        changes = []
        combat = self.handler.combat
        x, y = combat.grid.x, combat.grid.y
        attack_results = combat.party.p1.combatant.attack(combat.grid.rows[x][y])
        changes.extend(attack_results)
        return changes


class EndTurn(Logic):

    def logic(self):
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


class EnemyTurn(Logic):

    def logic(self):
        player = self.handler.combat.party.p1
        changes = self.handler.combat.enemies.p1.combatant.ai.take_turn_e(player)
        changes.append({'substate': EncounterStates.THINKING})
        return changes


class GoToReward(Logic):

    def logic(self):
        changes = [{'state': 'reward'}, {'substate': RewardStates.THINKING}]
        return changes


class RewardAuto(Logic):

    def logic(self):
        self.handler.loot.claimed.extend(self.handler.loot.items)
        self.handler.loot.items = []
        self.owner.options.current.choice = 2
        return []


class RewardManual(Logic):

    def logic(self):
        loot = self.handler.loot
        if (len(loot.items) + len(loot.claimed)) > 0:
            if len(loot.items) > 0:
                changes = [{'substate': RewardStates.SIFTING}]
            else:
                changes = [{'substate': RewardStates.DEPOSITING}]
        else:
            changes = []
        return changes


class RewardToLife(Logic):

    def logic(self):
        loot = self.handler.loot
        changes = [{'xp': loot.xp}]
        self.owner.party.inventory.take_loot(loot.claimed)
        self.owner.options.current.choice = 0

        changes.append({'state': 'life'})
        return changes


class RewardSifting(Logic):

    def logic(self):
        changes = []
        loot = self.handler.loot
        loot.claim(self.owner.options.current.choice)
        if len(loot.items) == 0:
            changes.append({'substate': RewardStates.THINKING})
            changes.append({'set_choice': 2})
        elif self.owner.options.current.choice > len(loot.items) - 1:
            self.owner.options.current.choice -= 1
        return changes


class RewardDepositing(Logic):

    def logic(self):
        changes = []
        loot = self.handler.loot
        loot.unclaim(self.owner.options.current.choice)
        if len(loot.claimed) == 0:
            changes.append({'substate': RewardStates.SIFTING})
        elif self.owner.options.current.choice > len(loot.claimed) - 1:
            self.owner.options.current.choice -= 1
        return changes


class RewardToggle(Logic):

    def logic(self, direction):
        changes = []
        loot = self.handler.loot
        if self.handler.state == RewardStates.SIFTING and direction == 'right' and len(loot.claimed) > 0:
            changes.append({'substate': RewardStates.DEPOSITING})
        elif self.handler.state == RewardStates.DEPOSITING and direction == 'left' and len(loot.items) > 0:
            changes.append({'substate': RewardStates.SIFTING})
        return changes


class RewardExit(Logic):

    def logic(self):
        changes = []
        state = self.handler.state
        if state in (RewardStates.SIFTING, RewardStates.DEPOSITING):
            changes.append({'substate': RewardStates.THINKING})
        elif state == RewardStates.THINKING and self.owner.options.current.choice == 2:
            changes.extend(RewardToLife.logic(self))
        elif state == RewardStates.THINKING:
            self.owner.options.current.choice = 2
        return changes

