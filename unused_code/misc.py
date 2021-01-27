@property
def leadership(self):
    """Used to determine formations, designated leader gives aura buffs"""
    captain = self.attributes.coordination + self.attributes.charisma
    return captain

# old enemy turn phase


def take_turn(self, target, fov_map, game_map, entities):
    results = []
    entity = self.owner
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):

        if entity.distance_to(target) >= 2:
            entity.move_astar(target, entities, game_map)

        elif target.combatant.attributes.current_hp > 0:
            attack_results = entity.combatant.attack(target)
            results.extend(attack_results)

    return results