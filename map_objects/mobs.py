from ECS.__entity.__combatant.attributes import Attributes
from ECS.__entity.combatant import Combatant
from ECS.__entity.__combatant.phylo import Phylo
from ECS.__entity.__combatant.level import Level
from ECS.__entity.__combatant.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, \
    Improvisation, Wisdom, Finesse, Charisma, Devotion
from ECS.__entity.__combatant.equipment import Equipment
from ECS.__entity.__combatant.inventory import Inventory
from ECS.__entity.__combatant.ai import BasicMonster
from loader_functions.image_objects import get_image_bundle


def orc(bundle):
    name = 'Orc'
    phylo = Phylo('humanoid', 'orcish', 'orc', 'regular', 'default')
    attribute_component = Attributes(5, 0, 0, 7, 10, 10, 10, 10, 10, 10)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 350

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def troll(bundle):
    name = 'Troll'
    phylo = Phylo('humanoid', 'giant', 'troll', 'regular', 'default')
    attribute_component = Attributes(1, 0, 0, 10, 10, 10, 10, 10, 10, 10)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 1000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_goblin(bundle):
    name = 'Goblin'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 50

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def goblin(bundle):
    name = 'Goblin'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 100

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_goblin(bundle):
    name = 'Goblin'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 5000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_goblin_mage(bundle):
    name = 'Goblin Mage'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'magic_dps')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 50

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def goblin_mage(bundle):
    name = 'Goblin Mage'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'magic_dps')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 100

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_goblin_mage(bundle):
    name = 'Goblin Mage'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'magic_dps')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 5000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_goblin_rogue(bundle):
    name = 'Goblin Rogue'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'melee_dps')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 50

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def goblin_rogue(bundle):
    name = 'Goblin Rogue'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'melee_dps')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 100

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_goblin_rogue(bundle):
    name = 'Goblin Rogue'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'melee_dps')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 5000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_goblin_shaman(bundle):
    name = 'Goblin Shaman'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'healer')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 50

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def goblin_shaman(bundle):
    name = 'Goblin Shaman'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'healer')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 100

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_goblin_shaman(bundle):
    name = 'Goblin'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'healer')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 5000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_kobold_trickster(bundle):
    name = 'Kobold Trickster'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'rogue')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def kobold_trickster(bundle):
    name = 'Kobold Trickster'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'rogue')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_kobold_trickster(bundle):
    name = 'Kobold Trickster'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'rogue')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_kobold_harasser(bundle):
    name = 'Kobold Harasser'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'ranger')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def kobold_harasser(bundle):
    name = 'Kobold Harasser'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'ranger')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_kobold_harasser(bundle):
    name = 'Kobold Harasser'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'ranger')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_kobold_zealot(bundle):
    name = 'Kobold Zealot'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'paladin')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def kobold_zealot(bundle):
    name = 'Kobold Zealot'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'paladin')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_kobold_zealot(bundle):
    name = 'Kobold Zealot'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'paladin')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_kobold(bundle):
    name = 'Kobold'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def kobold(bundle):
    name = 'Kobold'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_kobold(bundle):
    name = 'Kobold'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_rat(bundle):
    name = 'Rat'
    phylo = Phylo('beast', 'rodent', 'rat', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def rat(bundle):
    name = 'Rat'
    phylo = Phylo('beast', 'rodent', 'rat', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_rat(bundle):
    name = 'Rat'
    phylo = Phylo('beast', 'rodent', 'rat', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_bat(bundle):
    name = 'Bat'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def bat(bundle):
    name = 'Bat'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_bat(bundle):
    name = 'Bat'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_salamander(bundle):
    name = 'Salamander'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def salamander(bundle):
    name = 'Salamander'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_salamander(bundle):
    name = 'Salamander'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_spider(bundle):
    name = 'Spider'
    phylo = Phylo('nature', 'insect', 'spider', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def spider(bundle):
    name = 'Spider'
    phylo = Phylo('nature', 'insect', 'spider', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_spider(bundle):
    name = 'Spider'
    phylo = Phylo('nature', 'insect', 'spider', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_snail(bundle):
    name = 'Snail'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def snail(bundle):
    name = 'Snail'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_snail(bundle):
    name = 'Snail'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_shrimp(bundle):
    name = 'Shrimp'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def shrimp(bundle):
    name = 'Shrimp'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_shrimp(bundle):
    name = 'Shrimp'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_raccoon(bundle):
    name = 'Raccoon'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def raccoon(bundle):
    name = 'Raccoon'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_raccoon(bundle):
    name = 'Raccoon'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_bear(bundle):
    name = 'Bear'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 25

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def bear(bundle):
    name = 'Bear'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 75

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_bear(bundle):
    name = 'Bear'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 3500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mini_bramblelasher(bundle):
    name = 'Bramblelasher'
    phylo = Phylo('nature', 'plantae', 'bramblelasher', 'mini', 'default')
    attribute_component = Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 100

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def bramblelasher(bundle):
    name = 'Bramblelasher'
    phylo = Phylo('nature', 'plantae', 'bramblelasher', 'regular', 'default')
    attribute_component = Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 500

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)


def mega_bramblelasher(bundle):
    name = 'Bramblelasher'
    phylo = Phylo('nature', 'plantae', 'bramblelasher', 'mega', 'default')
    attribute_component = Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    level = Level()
    competence = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    
    xp = 5000

    return Combatant(name, bundle, phylo, attribute_component, level, competence, equipment, inventory,
                     ai_component, xp)
