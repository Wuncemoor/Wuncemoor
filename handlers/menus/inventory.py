from config.constants import DARK_PURPLE, YELLOW
from handlers.views.messages import Message
from enums.game_states import MenuStates
from enums.equipment_slots import EquipmentSlots


class Inventory:
    def __init__(self):
        self.superstate = MenuStates.INVENTORY
        self.misc = []
        self.weapons = []
        self.armor = []
        self.accessories = []
        self.satchel = []
        self.materials = []
        self.plot = []
        self.money = 0
        self.subgroups = self.initialize_subgroups()
        self.options = None
        self.sub = None

    def initialize_subgroups(self):
        return [self.misc, self.weapons, self.armor, self.accessories, self.satchel, self.materials, self.plot]

    def get_sub(self):
        return self.subgroups[self.options.choice]

    def add_item(self, item):
        results = []
        
        # if len(self.items) >= self.wt_limit:
        #     results.append({'item_added': None, 'message': Message("You're already overburdened! Get rid of some things or get stronger!", libtcod.dark_purple)})
        # else:
        results.extend([{'item_added': item},
                       {'message': Message('You pick up the {0}!'.format(item.name), DARK_PURPLE)}])
        subgroup = self.filter_item(item.item)
        subgroup.append(item)

        return results

    def take_loot(self, loot):
        for item in loot:
            self.add_item(item)

    def filter_item(self, item):

        if item.equippable:
            if item.equippable.slot == EquipmentSlots.MAIN_HAND:
                subgroup = self.weapons
            elif item.equippable.slot in (EquipmentSlots.OFF_HAND, EquipmentSlots.HEAD, EquipmentSlots.BODY,
                                          EquipmentSlots.HANDS, EquipmentSlots.FEET):
                subgroup = self.armor
            else:
                subgroup = self.accessories
        elif item.useable:
            subgroup = self.satchel
        elif item.craftable:
            subgroup = self.materials
        elif item.important:
            subgroup = self.plot
        else:
            subgroup = self.misc
        return subgroup
        
    def use(self, item_entity, **kwargs):
        results = []
        
        item_component = item_entity.item
        
        if item_component.equippable is not None:
            equippable_component = item_entity.item.equippable
            
            if equippable_component:
                results.append({'equip': item_entity})
            else:    
                results.append({'message': Message('The {0} cannot be used'.format(item_entity.name), YELLOW)})
                        
        else:
            if item_component.useable.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting': item_entity})
            else:    
                kwargs = {**item_component.useable.function_kwargs, **kwargs}
                item_use_results = item_component.useable.use_function(self.owner, **kwargs)
                
                for item_use_result in item_use_results:
                    if item_use_result.get('consumed'):
                        self.remove_item(item_entity)
                        
                results.extend(item_use_results)
            
        return results
    
    def remove_item(self, item):
        self.items.remove(item)
        
    def drop_item(self, item):
        results = []
        
        if self.owner.combatant.equipment.main_hand == item or self.owner.combatant.equipment.off_hand == item or self.owner.combatant.equipment.head == item or self.owner.combatant.equipment.body == item or self.owner.combatant.equipment.feet == item or self.owner.combatant.equipment.belt == item or self.owner.combatant.equipment.hands == item or self.owner.combatant.equipment.finger == item or self.owner.combatant.equipment.neck == item or self.owner.combatant.equipment.back == item or self.owner.combatant.equipment.accessory == item:
            self.owner.combatant.equipment.toggle_equip(item)
        
        item.x = self.owner.x
        item.y = self.owner.y
        self.remove_item(item)
        results.append({'item_dropped': item, 'message': Message('You dropped the {0}!'.format(item.name), YELLOW)})
        
        return results
