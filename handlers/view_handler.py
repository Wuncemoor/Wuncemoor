import pygame as py
from config.constants import TILES_ON_SCREEN
from config.image_objects import TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H, MESSAGE_BG
from enums.game_states import GameStates, MenuStates
from menus import level_up_menu
from render_functions import draw_tile, draw_structure, draw_entity
from screens.calendar import display_calendar
from screens.character_screen import character_screen
from screens.dialogue_screen import dialogue_screen
from screens.encounter_screen import encounter_screen
from screens.gui_tools import align_and_blit, get_surface, blit_options, print_message
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.loot_screen import loot_screen
from screens.mini_map import minimap_screen
from screens.resources_HUD import player_resource_display


class ViewHandler:
    def __init__(self, screen):
        self.screen = screen
        self.option = 0
        self.world_tiles = None
        self.camera = None
        self.fov = None

    def take_ownership(self):
        self.camera.owner = self
        self.fov.owner = self

    def title_screen(self):
        self.screen.blit(TITLE_SCREEN_BG, (0, 0))

        tfont = py.font.Font('screens\\fonts\\lunchds.ttf', 150)
        stfont = py.font.Font('screens\\fonts\\lunchds.ttf', 60)
        titletext = tfont.render('WUNCEMOOR', True, (0, 0, 0))
        tsubt = stfont.render('THE ETERNAL DREAM', True, (0, 0, 0))

        align_and_blit(self.screen, titletext, x_ratio=0.5, y_ratio=0.25)
        align_and_blit(self.screen, tsubt, x_ratio=0.5, y_ratio=0.38)
        menu = self.title_menu()
        align_and_blit(self.screen, menu, x_ratio=0.5, y_ratio=0.75)

    def title_menu(self):
        surf = get_surface(TITLE_MENU_BG)
        options = ['Start A New Game', 'Continue Previous Game', 'Quit']
        blit_options(surf, TITLE_MENU_BUTTON, 22, 10, TITLE_MENU_BUTTON.get_height(), options, fontsize=40)
        surf.blit(INDICATOR_H, (0, 10 + (self.option * TITLE_MENU_BUTTON.get_height())))

        return surf

    def render_all(self, camera_surface, message_surface, player, message_log, menu_handler, time_handler, encounter, loot, dialogue):
        (width, height) = TILES_ON_SCREEN


        tilesize = 16
        # Draw tiles near player
        if self.fov.recompute:
            for y in range(height):
                for x in range(width):
                    draw_tile(camera_surface, self.fov.map, self.owner.world, x, y, self.camera.x, self.camera.y, tilesize)

        for structure in self.owner.world.current_map.structures:
            draw_structure(camera_surface, self.camera.x, self.camera.y, structure, self.fov.map, self.owner.world, tilesize)
        for transition in self.owner.world.current_map.transitions:
            draw_entity(camera_surface, self.camera.x, self.camera.y, transition, self.fov.map, self.owner.world, tilesize)
        for noncom in self.owner.world.current_map.noncombatants:
            draw_entity(camera_surface, self.camera.x, self.camera.y, noncom, self.fov.map, self.owner.world, tilesize)
        # draw all entities in list
        entities_in_render_order = sorted(self.owner.world.current_map.entities, key=lambda x: x.render_order.value)
        for entity in entities_in_render_order:
            draw_entity(camera_surface, self.camera.x, self.camera.y, entity, self.fov.map, self.owner.world, tilesize)
        draw_entity(camera_surface, self.camera.x, self.camera.y, player, self.fov.map, self.owner.world, tilesize)

        self.screen.blit(camera_surface, (0, 0))

        # Print game messages one line at a time
        message_surface.blit(MESSAGE_BG, (0, 0))
        y = 0
        for message in message_log.messages:
            off_x = 30
            off_y = 5
            print_message(message_surface, message, off_x, off_y, y)
            y += 1

        self.screen.blit(message_surface, (300, 592))
        message_surface.fill((0, 0, 0))

        resource_hud = player_resource_display(player)
        self.screen.blit(resource_hud, (0 - 10, 540 + 40))

        calendar = display_calendar(time_handler.month, time_handler.day)

        if self.owner.state == GameStates.PLAYERS_TURN:
            self.screen.blit(calendar, (self.screen.get_width() - calendar.get_width(), self.screen.get_height() - calendar.get_height()))

        if self.owner.state == GameStates.SHOW_MAP:
            minimap_screen(self.screen, self.world_map)
        elif self.owner.state == GameStates.LEVEL_UP:
            level_up_menu(self.screen, player)
        elif self.owner.state == GameStates.DIALOGUE:
            dialogue_screen(self.screen, player, dialogue)
        elif self.owner.state == GameStates.ENCOUNTER:
            encounter_screen(self.screen, player, encounter, message_log)
        elif self.owner.state == GameStates.LOOTING:
            loot_screen(self.screen, loot, message_log)
        elif self.owner.state == GameStates.MENUS:
            if menu_handler.state == MenuStates.PARTY:
                character_screen(self.screen, player)
            elif menu_handler.state == MenuStates.JOURNAL:
                journal_screen(self.screen, menu_handler)
            elif menu_handler.state == MenuStates.INVENTORY:
                inventory_screen(self.screen, menu_handler)
