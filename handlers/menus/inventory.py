from config.constants import YELLOW
from data_structures.menu_tools import LogicList
from handlers.logic.menus_logic import menus_goto_submenu, menus_goto_entity_options
from handlers.views.messages import Message
from enums.game_states import MenuStates, InventoryStates
from enums.equipment_slots import EquipmentSlots


class Inventory:
    def __init__(self):
        self.superstate = MenuStates.INVENTORY
        self.state = InventoryStates.BASE
        self.weapons = LogicList([], menus_goto_entity_options)
        self.armor = LogicList([], menus_goto_entity_options)
        self.accessories = LogicList([], menus_goto_entity_options)
        self.rations = LogicList([], menus_goto_entity_options)
        self.satchel = LogicList([], menus_goto_entity_options)
        self.materials = LogicList([], menus_goto_entity_options)
        self.plot = LogicList([], menus_goto_entity_options)
        self.money = 0
        self.menu = self.initialize_menu()
        self.submenu = None

    @property
    def mass(self):
        total = 0
        for subgroup in self.menu:
            for entity in subgroup:
                total += entity.mass
        return total

    def initialize_menu(self):
        return LogicList([self.weapons, self.armor, self.accessories, self.rations, self.satchel, self.materials,
                             self.plot], menus_goto_submenu)

    def change_state(self, state, options):
        self.state = self.state.__class__(state)
        if state == 1:
            self.submenu = None
            self.menu.unlock()
            options.current = self.menu
        elif state == 2:
            self.menu.lock()
            self.submenu = self.menu.pointer_data
            self.submenu.unlock()
            options.current = self.submenu
            if len(options.current) == 0:
                self.change_state(1, options)
        elif state == 3:
            self.submenu.lock()
            entity = self.submenu.pointer_data
            options.current = options.get(component=entity.item)

    def add_item(self, item):

        # if len(self.items) >= self.wt_limit:
        #     results.append({'item_added': None, 'message': Message("You're already overburdened! Get rid of some things or get stronger!", libtcod.dark_purple)})

        subgroup = self.filter_item(item.item)
        subgroup.append(item)

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
