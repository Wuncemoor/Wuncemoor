from map_objects.mobs import orc, troll, goblin, goblin_mage, goblin_rogue, goblin_shaman, mini_goblin, \
    mini_goblin_mage, mini_goblin_rogue, mini_goblin_shaman, mega_goblin, mega_goblin_rogue, mega_goblin_mage, \
    mega_goblin_shaman, mini_kobold, mini_kobold_harasser, mini_kobold_trickster, mini_kobold_zealot, kobold, \
    kobold_harasser, kobold_trickster, kobold_zealot, mega_kobold, mega_kobold_harasser, mega_kobold_trickster, \
    mega_kobold_zealot, mini_rat, rat, mega_rat, mini_bat, bat, mega_bat, mini_salamander, salamander, mega_salamander,\
    mini_spider, spider, mega_spider, mini_snail, snail, mega_snail, mini_shrimp, shrimp, mega_shrimp, mini_raccoon, \
    raccoon, mega_raccoon, mini_bear, bear, mega_bear, mini_bramblelasher, bramblelasher, mega_bramblelasher
from builders.make_item import make_item
from loader_functions.image_objects import get_image_bundle


class MobDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_combatant(self, images):
        combatant = self.__builder.get_combatant(images)

        items = images.get('entities').get('items')
        inventory = self.__builder.get_inventory(items)


        return combatant


class MobBuilder:

    def __init__(self, node_power, mob):
        self.node_power = node_power
        self.mob = mob



    def get_combatant(self, images):
        bundle = get_image_bundle(images, self.mob)
        mobs = {'orc': orc(bundle),
                'troll': troll(bundle),
                'mini_goblin': mini_goblin(bundle),
                'goblin': goblin(bundle),
                'mega_goblin': mega_goblin(bundle),
                'mini_goblin_mage': mini_goblin_mage(bundle),
                'goblin_mage': goblin_mage(bundle),
                'mega_goblin_mage': mega_goblin_mage(bundle),
                'mini_goblin_rogue': mini_goblin_rogue(bundle),
                'goblin_rogue': goblin_rogue(bundle),
                'mega_goblin_rogue': mega_goblin_rogue(bundle),
                'mini_goblin_shaman': mini_goblin_shaman(bundle),
                'goblin_shaman': goblin_shaman(bundle),
                'mega_goblin_shaman': mega_goblin_shaman(bundle),
                'mini_kobold': mini_kobold(bundle),
                'kobold': kobold(bundle),
                'mega_kobold': mega_kobold(bundle),
                'mini_kobold_harasser': mini_kobold_harasser(bundle),
                'kobold_harasser': kobold_harasser(bundle),
                'mega_kobold_harasser': mega_kobold_harasser(bundle),
                'mini_kobold_trickster': mini_kobold_trickster(bundle),
                'kobold_trickster': kobold_trickster(bundle),
                'mega_kobold_trickster': mega_kobold_trickster(bundle),
                'mini_kobold_zealot': mini_kobold_zealot(bundle),
                'kobold_zealot': kobold_zealot(bundle),
                'mega_kobold_zealot': mega_kobold_zealot(bundle),
                'mini_rat': mini_rat(bundle),
                'rat': rat(bundle),
                'mega_rat': mega_rat(bundle),
                'mini_bat': mini_bat(bundle),
                'bat': bat(bundle),
                'mega_bat': mega_bat(bundle),
                'mini_salamander': mini_salamander(bundle),
                'salamander': salamander(bundle),
                'mega_salamander': mega_salamander(bundle),
                'mini_spider': mini_spider(bundle),
                'spider': spider(bundle),
                'mega_spider': mega_spider(bundle),
                'mini_snail': mini_snail(bundle),
                'snail': snail(bundle),
                'mega_snail': mega_snail(bundle),
                'mini_shrimp': mini_shrimp(bundle),
                'shrimp': shrimp(bundle),
                'mega_shrimp': mega_shrimp(bundle),
                'mini_raccoon': mini_raccoon(bundle),
                'raccoon': raccoon(bundle),
                'mega_raccoon': mega_raccoon(bundle),
                'mini_bear': mini_bear(bundle),
                'bear': bear(bundle),
                'mega_bear': mega_bear(bundle),
                'mini_bramblelasher': mini_bramblelasher(bundle),
                'bramblelasher': bramblelasher(bundle),
                'mega_bramblelasher': mega_bramblelasher(bundle),
                }
        return mobs[self.mob]

    def get_inventory(self, images):

        potion = make_item(images, 'healing_potion')
