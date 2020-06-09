from ECS.__entity.__combatant.ai import BasicMonster
from ECS.__entity.__combatant.competence import Competence, Strength, Instinct, Coordination, Devotion, Charisma, \
    Finesse, Vitality, Arcana, Improvisation, Wisdom
from ECS.__entity.__combatant.equipment import Equipment
from ECS.__entity.__combatant.level import Level
from ECS.__entity.combatant import Combatant

from builders.make_item import make_item
from loader_functions.image_objects import get_image_bundle
from ECS.__entity.__combatant.attributes import Attributes
from ECS.__entity.__combatant.phylo import Phylo
from ECS.__entity.__combatant.inventory import Inventory


class MobDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_combatant(self, images):

        name = self.__builder.get_name()
        bundle = self.__builder.get_images(images)
        phylo = self.__builder.get_phylo()
        attributes = self.__builder.get_attributes()
        level = self.__builder.get_level()
        competence = self.__builder.get_competence()
        equipment = self.__builder.get_equipment()
        inventory = self.__builder.get_inventory(images)
        xp = self.__builder.get_xp()
        ai = self.__builder.get_ai()
        combatant = Combatant(name, bundle, phylo, attributes, level, competence, equipment, inventory, ai, xp)
        return combatant


class MobBuilder:

    def __init__(self, node_power, mob):
        self.node_power = node_power
        self.mob = mob

    def get_name(self):
        if 'mini_' or 'mega_' in self.mob:
            cut = self.mob[5:].capitalize()
            if '_' in cut:
                x = cut.index('_')
                cut.replace('_', ' ')
                cut[x + 1:].capitalize()
            return cut
        else:
            return self.mob.capitalize()

    def get_images(self, images):
        return get_image_bundle(images, self.mob)

    def get_phylo(self):

        phylo_dict = {
            'mini_goblin': Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'default'),
            'goblin': Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'default'),
            'mega_goblin': Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'default'),
            'mini_goblin_mage': Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'magic_dps'),
            'goblin_mage': Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'magic_dps'),
            'mega_goblin_mage': Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'magic_dps'),
            'mini_goblin_rogue': Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'melee_dps'),
            'goblin_rogue': Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'melee_dps'),
            'mega_goblin_rogue': Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'melee_dps'),
            'mini_goblin_shaman': Phylo('humanoid', 'goblinoid', 'goblin', 'mini', 'healer'),
            'goblin_shaman': Phylo('humanoid', 'goblinoid', 'goblin', 'regular', 'healer'),
            'mega_goblin_shaman': Phylo('humanoid', 'goblinoid', 'goblin', 'mega', 'healer'),
            'mini_kobold_trickster': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'rogue'),
            'kobold_trickster': Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'rogue'),
            'mega_kobold_trickster': Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'rogue'),
            'mini_kobold_harasser': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'ranger'),
            'kobold_harasser': Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'ranger'),
            'mega_kobold_harasser': Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'ranger'),
            'mini_kobold_zealot': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'paladin'),
            'kobold_zealot': Phylo('humanoid', 'goblinoid', 'kobold', 'regular', 'paladin'),
            'mega_kobold_zealot': Phylo('humanoid', 'goblinoid', 'kobold', 'mega', 'paladin'),
            'mini_kobold': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'default'),
            'kobold': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'default'),
            'mega_kobold': Phylo('humanoid', 'goblinoid', 'kobold', 'mini', 'default'),
            'mini_rat': Phylo('beast', 'rodent', 'rat', 'mini', 'default'),
            'rat': Phylo('beast', 'rodent', 'rat', 'regular', 'default'),
            'mega_rat': Phylo('beast', 'rodent', 'rat', 'mega', 'default'),
            'mini_bat': Phylo('beast', 'chiroptera', 'bat', 'mini', 'default'),
            'bat': Phylo('beast', 'chiroptera', 'bat', 'regular', 'default'),
            'mega_bat': Phylo('beast', 'chiroptera', 'bat', 'mega', 'default'),
            'mini_salamander': Phylo('herptile', 'lizard', 'salamander', 'mini', 'default'),
            'salamander': Phylo('herptile', 'lizard', 'salamander', 'regular', 'default'),
            'mega_salamander': Phylo('herptile', 'lizard', 'salamander', 'mega', 'default'),
            'mini_spider': Phylo('nature', 'insect', 'spider', 'mini', 'default'),
            'spider': Phylo('nature', 'insect', 'spider', 'regular', 'default'),
            'mega_spider': Phylo('nature', 'insect', 'spider', 'mega', 'default'),
            'mini_snail': Phylo('aquatic', 'mollusk', 'snail', 'mini', 'default'),
            'snail': Phylo('aquatic', 'mollusk', 'snail', 'regular', 'default'),
            'mega_snail': Phylo('aquatic', 'mollusk', 'snail', 'mega', 'default'),
            'mini_shrimp': Phylo('aquatic', 'crustacean', 'shrimp', 'mini', 'default'),
            'shrimp': Phylo('aquatic', 'crustacean', 'shrimp', 'regular', 'default'),
            'mega_shrimp': Phylo('aquatic', 'crustacean', 'shrimp', 'mega', 'default'),
            'mini_raccoon': Phylo('beast', 'carnivora', 'raccoon', 'mini', 'default'),
            'raccoon': Phylo('beast', 'carnivora', 'raccoon', 'regular', 'default'),
            'mega_raccoon': Phylo('beast', 'carnivora', 'raccoon', 'mega', 'default'),
            'mini_bear': Phylo('beast', 'carnivora', 'ursa', 'mini', 'default'),
            'bear': Phylo('beast', 'carnivora', 'ursa', 'regular', 'default'),
            'mega_bear': Phylo('beast', 'carnivora', 'ursa', 'mega', 'default'),
            'mini_bramblelasher': Phylo('nature', 'plantae', 'bramblelasher', 'mini', 'default'),
            'bramblelasher': Phylo('nature', 'plantae', 'bramblelasher', 'regular', 'default'),
            'mega_bramblelasher': Phylo('nature', 'plantae', 'bramblelasher', 'mega', 'default'),

        }

        return phylo_dict.get(self.mob)

    def get_attributes(self):

        att_dict = {
            'mini_goblin': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'goblin': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_goblin': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_goblin_mage': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'goblin_mage': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_goblin_mage': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_goblin_rogue': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'goblin_rogue': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_goblin_rogue': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_goblin_shaman': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'goblin_shaman': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_goblin_shaman': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_kobold_trickster': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'kobold_trickster': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_kobold_trickster': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_kobold_harasser': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'kobold_harasser': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_kobold_harasser': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_kobold_zealot': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'kobold_zealot': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_kobold_zealot': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_kobold': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'kobold': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_kobold': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_rat': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'rat': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_rat': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_bat': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'bat': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_bat': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_salamander': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'salamander': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_salamander': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_spider': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'spider': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_spider': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_snail': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'snail': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_snail': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_shrimp': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'shrimp': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_shrimp': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_raccoon': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'raccoon': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_raccoon': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_bear': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'bear': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_bear': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
            'mini_bramblelasher': Attributes(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            'bramblelasher': Attributes(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
            'mega_bramblelasher': Attributes(5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
        }

        return att_dict.get(self.mob)

    def get_level(self):
        return Level()

    def get_competence(self):
        return Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(),
                            Finesse(), Charisma(), Devotion())

    def get_equipment(self):
        return Equipment()

    def get_xp(self):

        xp_dict = {
            'mini_goblin': 25,
            'goblin': 75,
            'mega_goblin': 3500,
            'mini_goblin_mage': 25,
            'goblin_mage': 75,
            'mega_goblin_mage': 3500,
            'mini_goblin_rogue': 25,
            'goblin_rogue': 75,
            'mega_goblin_rogue': 3500,
            'mini_goblin_shaman': 25,
            'goblin_shaman': 75,
            'mega_goblin_shaman': 3500,
            'mini_kobold_trickster': 25,
            'kobold_trickster': 75,
            'mega_kobold_trickster': 3500,
            'mini_kobold_harasser': 25,
            'kobold_harasser': 75,
            'mega_kobold_harasser': 3500,
            'mini_kobold_zealot': 25,
            'kobold_zealot': 75,
            'mega_kobold_zealot': 3500,
            'mini_kobold': 25,
            'kobold': 75,
            'mega_kobold': 3500,
            'mini_rat': 25,
            'rat': 75,
            'mega_rat': 3500,
            'mini_bat': 25,
            'bat': 75,
            'mega_bat': 3500,
            'mini_salamander': 25,
            'salamander':  75,
            'mega_salamander': 3500,
            'mini_spider': 25,
            'spider': 75,
            'mega_spider': 3500,
            'mini_snail': 25,
            'snail': 75,
            'mega_snail': 3500,
            'mini_shrimp': 25,
            'shrimp': 75,
            'mega_shrimp': 3500,
            'mini_raccoon': 25,
            'raccoon': 75,
            'mega_raccoon': 3500,
            'mini_bear': 25,
            'bear': 75,
            'mega_bear': 3500,
            'mini_bramblelasher': 25,
            'bramblelasher': 75,
            'mega_bramblelasher': 3500,
        }

        return xp_dict.get(self.mob)

    def get_ai(self):
        return BasicMonster()

    def get_inventory(self, images):

        inven = Inventory(26)

        potion = make_item(images, 'healing_potion')
        inven.add_item(potion)

        return inven
