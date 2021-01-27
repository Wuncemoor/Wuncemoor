import tcod as libtcod
from random import randint
from handlers.views.messages import Message


class BasicMonster:
    """Basic mob behavior. """

    def take_turn(self, player):
        results = []
        mob = self.owner
        attack_results = mob.combatant.attack(player)
        results.extend(attack_results)
        return results


class ConfusedMonster:
    """Old mob behavior for when hit with a confusing spell"""
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns
        
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        
        if self.number_of_turns > 0:
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1
            
            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)
                
            self.number_of_turns -= 1
        else:
            self.owner.ai = self.previous_ai
            results.append({'message':Message('The {0} is no longer confused!'.format(self.owner.name), libtcod.red)})
            
        return results
