from components.attributes import Attributes
from components.ai import BasicMonster
from components.combatant import Combatant
from components.phylo import Phylo
from components.level import Level
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.equipment import Equipment
from components.inventory import Inventory
from components.ai import BasicMonster

def orc():
    name = 'Orc'
    image = 'o'
    phylo = Phylo('humanoid', 'orcish', 'orc', 'regular', 'default')
    attribute_component = Attributes(5,0,0,7,10,10,10,10,10,10)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=350
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

    
def troll():
    name = 'Troll'
    image = 'T'
    phylo = Phylo('humanoid', 'giant', 'troll', 'regular', 'default')
    attribute_component = Attributes(1,0,0,10,10,10,10,10,10,10)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=1000
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
def mini_goblin():
    name = 'Goblin'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=50
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def goblin():
    name = 'Goblin'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=100

    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mega_goblin():
    name = 'Goblin'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=5000
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_goblin_mage():
    name = 'Goblin Mage'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'magic_dps')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=50
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def goblin_mage():
    name = 'Goblin Mage'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'magic_dps')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=100

    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mega_goblin_mage():
    name = 'Goblin Mage'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'magic_dps')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=5000
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_goblin_rogue():
    name = 'Goblin Rogue'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'melee_dps')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=50
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def goblin_rogue():
    name = 'Goblin Rogue'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'melee_dps')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=100

    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mega_goblin_rogue():
    name = 'Goblin Rogue'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'melee_dps')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=5000
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_goblin_shaman():
    name = 'Goblin Shaman'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'healer')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=50
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def goblin_shaman():
    name = 'Goblin Shaman'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'healer')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=100

    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mega_goblin_shaman():
    name = 'Goblin'
    image = 'g'
    phylo = Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'healer')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=5000
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_kobold_trickster():
    name = 'Kobold Trickster'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'rogue')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def kobold_trickster():
    name = 'Kobold Trickster'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'rogue')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_kobold_trickster():
    name = 'Kobold Trickster'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'rogue')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_kobold_harasser():
    name = 'Kobold Harasser'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'ranger')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def kobold_harasser():
    name = 'Kobold Harasser'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'ranger')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_kobold_harasser():
    name = 'Kobold Harasser'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'ranger')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_kobold_zealot():
    name = 'Kobold Zealot'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'paladin')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def kobold_zealot():
    name = 'Kobold Zealot'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'paladin')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_kobold_zealot():
    name = 'Kobold Zealot'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'paladin')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_kobold():
    name = 'Kobold'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def kobold():
    name = 'Kobold'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_kobold():
    name = 'Kobold'
    image = 'k'
    phylo = Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_rat():
    name = 'Rat'
    image = 'r'
    phylo = Phylo('beast', 'rodent', 'rat', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def rat():
    name = 'Rat'
    image = 'r'
    phylo = Phylo('beast', 'rodent', 'rat', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_rat():
    name = 'Rat'
    image = 'r'
    phylo = Phylo('beast', 'rodent', 'rat', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_bat():
    name = 'Bat'
    image = 'b'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def bat():
    name = 'Bat'
    image = 'b'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_bat():
    name = 'Bat'
    image = 'b'
    phylo = Phylo('beast', 'chiroptera', 'bat', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_salamander():
    name = 'Salamander'
    image = 's'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def salamander():
    name = 'Salamander'
    image = 's'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_salamander():
    name = 'Salamander'
    image = 's'
    phylo = Phylo('herptile', 'lizard', 'salamander', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_spider():
    name = 'Spider'
    image = 'S'
    phylo = Phylo('nature', 'insect', 'spider', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def spider():
    name = 'Spider'
    image = 'S'
    phylo = Phylo('nature', 'insect', 'spider', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_spider():
    name = 'Spider'
    image = 'S'
    phylo = Phylo('nature', 'insect', 'spider', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_snail():
    name = 'Snail'
    image = 's'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def snail():
    name = 'Snail'
    image = 's'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_snail():
    name = 'Snail'
    image = 's'
    phylo = Phylo('aquatic', 'mollusk', 'snail', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_shrimp():
    name = 'Shrimp'
    image = 's'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def shrimp():
    name = 'Shrimp'
    image = 's'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_shrimp():
    name = 'Shrimp'
    image = 's'
    phylo = Phylo('aquatic', 'crustacean', 'shrimp', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)

def mini_raccoon():
    name = 'Raccoon'
    image = 'r'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def raccoon():
    name = 'Raccoon'
    image = 'r'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_raccoon():
    name = 'Raccoon'
    image = 'r'
    phylo = Phylo('beast', 'carnivora', 'raccoon', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mini_bear():
    name = 'Bear'
    image = 'B'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'mini', 'default')
    attribute_component = Attributes(1,1,1,1,1,1,1,1,1,1)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=25
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def bear():
    name = 'Bear'
    image = 'B'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'regular', 'default')
    attribute_component = Attributes(2,2,2,2,2,2,2,2,2,2)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=75
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)
    
def mega_bear():
    name = 'Bear'
    image = 'B'
    phylo = Phylo('beast', 'carnivora', 'ursa', 'mega', 'default')
    attribute_component = Attributes(5,5,5,5,5,5,5,5,5,5)
    level = Level()
    competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
    equipment = Equipment()
    inventory = Inventory(26)
    ai_component = BasicMonster()
    xp=3500
    
    return Combatant(name, image, phylo, attribute_component, level, competence, equipment, inventory, ai_component, xp)