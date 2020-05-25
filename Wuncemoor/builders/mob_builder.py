from map_objects.mobs import orc, troll, goblin, goblin_mage, goblin_rogue, goblin_shaman, mini_goblin, \
    mini_goblin_mage, mini_goblin_rogue, mini_goblin_shaman, mega_goblin, mega_goblin_rogue, mega_goblin_mage, \
    mega_goblin_shaman, mini_kobold, mini_kobold_harasser, mini_kobold_trickster, mini_kobold_zealot, kobold, \
    kobold_harasser, kobold_trickster, kobold_zealot, mega_kobold, mega_kobold_harasser, mega_kobold_trickster, \
    mega_kobold_zealot, mini_rat, rat, mega_rat, mini_bat, bat, mega_bat, mini_salamander, salamander, mega_salamander,\
    mini_spider, spider, mega_spider, mini_snail, snail, mega_snail, mini_shrimp, shrimp, mega_shrimp, mini_raccoon, \
    raccoon, mega_raccoon, mini_bear, bear, mega_bear, mini_bramblelasher, bramblelasher, mega_bramblelasher


class MobDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_combatant(self):
        combatant = self.__builder.get_combatant()

        return combatant


class MobBuilder:

    def __init__(self, node_power, mob, mob_obj):
        self.node_power = node_power
        self.mob = mob
        self.mob_obj = mob_obj


    def get_combatant(self):
        mobs = {'orc': orc(self.mob_obj),
                'troll': troll(self.mob_obj),
                'mini_goblin': mini_goblin(self.mob_obj),
                'goblin': goblin(self.mob_obj),
                'mega_goblin': mega_goblin(self.mob_obj),
                'mini_goblin_mage': mini_goblin_mage(self.mob_obj),
                'goblin_mage': goblin_mage(self.mob_obj),
                'mega_goblin_mage': mega_goblin_mage(self.mob_obj),
                'mini_goblin_rogue': mini_goblin_rogue(self.mob_obj),
                'goblin_rogue': goblin_rogue(self.mob_obj),
                'mega_goblin_rogue': mega_goblin_rogue(self.mob_obj),
                'mini_goblin_shaman': mini_goblin_shaman(self.mob_obj),
                'goblin_shaman': goblin_shaman(self.mob_obj),
                'mega_goblin_shaman': mega_goblin_shaman(self.mob_obj),
                'mini_kobold': mini_kobold(self.mob_obj),
                'kobold': kobold(self.mob_obj),
                'mega_kobold': mega_kobold(self.mob_obj),
                'mini_kobold_harasser': mini_kobold_harasser(self.mob_obj),
                'kobold_harasser': kobold_harasser(self.mob_obj),
                'mega_kobold_harasser': mega_kobold_harasser(self.mob_obj),
                'mini_kobold_trickster': mini_kobold_trickster(self.mob_obj),
                'kobold_trickster': kobold_trickster(self.mob_obj),
                'mega_kobold_trickster': mega_kobold_trickster(self.mob_obj),
                'mini_kobold_zealot': mini_kobold_zealot(self.mob_obj),
                'kobold_zealot': kobold_zealot(self.mob_obj),
                'mega_kobold_zealot': mega_kobold_zealot(self.mob_obj),
                'mini_rat': mini_rat(self.mob_obj),
                'rat': rat(self.mob_obj),
                'mega_rat': mega_rat(self.mob_obj),
                'mini_bat': mini_bat(self.mob_obj),
                'bat': bat(self.mob_obj),
                'mega_bat': mega_bat(self.mob_obj),
                'mini_salamander': mini_salamander(self.mob_obj),
                'salamander': salamander(self.mob_obj),
                'mega_salamander': mega_salamander(self.mob_obj),
                'mini_spider': mini_spider(self.mob_obj),
                'spider': spider(self.mob_obj),
                'mega_spider': mega_spider(self.mob_obj),
                'mini_snail': mini_snail(self.mob_obj),
                'snail': snail(self.mob_obj),
                'mega_snail': mega_snail(self.mob_obj),
                'mini_shrimp': mini_shrimp(self.mob_obj),
                'shrimp': shrimp(self.mob_obj),
                'mega_shrimp': mega_shrimp(self.mob_obj),
                'mini_raccoon': mini_raccoon(self.mob_obj),
                'raccoon': raccoon(self.mob_obj),
                'mega_raccoon': mega_raccoon(self.mob_obj),
                'mini_bear': mini_bear(self.mob_obj),
                'bear': bear(self.mob_obj),
                'mega_bear': mega_bear(self.mob_obj),
                'mini_bramblelasher': mini_bramblelasher(self.mob_obj),
                'bramblelasher': bramblelasher(self.mob_obj),
                'mega_bramblelasher': mega_bramblelasher(self.mob_obj),
                }
        return mobs[self.mob]
