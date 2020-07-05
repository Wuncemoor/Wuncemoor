import pygame as py
import tcod as libtcod
from config.constants import TILES_ON_SCREEN, BLACK
from config.image_objects import TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H, MESSAGE_BG, TILE_BASE
from enums.game_states import GameStates, MenuStates
from menus import level_up_menu
from screens.calendar import display_calendar
from screens.character_screen import character_screen
from screens.dialogue_screen import dialogue_screen
from screens.encounter_screen import encounter_screen
from screens.gui_tools import align_and_blit, get_surface, blit_options, print_message
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.reward_screen import reward_screen
from screens.mini_map import minimap_screen
from screens.resources_HUD import player_resource_display
from handlers.views.fov_handler import FovHandler
from handlers.views.camera import Camera


class ViewHandler:
    def __init__(self, screen):
        self.screen = screen
        self.option = 0
        self.world_tiles = None
        self.camera = Camera()
        self.camera.owner = self
        self.fov = FovHandler()
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

    def render_all(self, player, message_log):
        (width, height) = TILES_ON_SCREEN

        tilesize = 16
        # Draw tiles near player
        if self.fov.recompute:
            for y in range(height):
                for x in range(width):
                    self.draw_tile(self.fov.map, self.owner.world, x, y, self.camera.x, self.camera.y, tilesize)

        for structure in self.owner.world.current_map.structures:
            self.draw_structure(self.camera.x, self.camera.y, structure, self.fov.map, self.owner.world, tilesize)
        for transition in self.owner.world.current_map.transitions:
            self.draw_entity(self.camera.x, self.camera.y, transition, self.fov.map, self.owner.world, tilesize)
        for noncom in self.owner.world.current_map.noncombatants:
            self.draw_entity(self.camera.x, self.camera.y, noncom, self.fov.map, self.owner.world, tilesize)
        # draw all entities in list
        entities_in_render_order = sorted(self.owner.world.current_map.entities, key=lambda x: x.render_order.value)
        for entity in entities_in_render_order:
            self.draw_entity(self.camera.x, self.camera.y, entity, self.fov.map, self.owner.world, tilesize)
        self.draw_entity(self.camera.x, self.camera.y, player, self.fov.map, self.owner.world, tilesize)

        # Print game messages one line at a time

        message_surface = get_surface(MESSAGE_BG)
        y = 0
        for message in message_log.messages:
            off_x = 30
            off_y = 5
            print_message(message_surface, message, off_x, off_y, y)
            y += 1

        self.screen.blit(message_surface, (300, 592))
        message_surface.fill(BLACK)

        resource_hud = player_resource_display(player)
        self.screen.blit(resource_hud, (0 - 10, 540 + 40))

        calendar = display_calendar(self.owner.time.month, self.owner.time.day)

        if self.owner.state == GameStates.PLAYERS_TURN:
            self.screen.blit(calendar, (self.screen.get_width() - calendar.get_width(), self.screen.get_height() - calendar.get_height()))

        if self.owner.state == GameStates.SHOW_MAP:
            minimap_screen(self.screen, self.world_tiles)
        elif self.owner.state == GameStates.LEVEL_UP:
            level_up_menu(self.screen, player)
        elif self.owner.state == GameStates.DIALOGUE:
            dialogue_screen(self.screen, player, self.owner.dialogue)
        elif self.owner.state == GameStates.ENCOUNTER:
            encounter_screen(self.screen, player, self.owner.encounter, message_log)
        elif self.owner.state == GameStates.REWARD:
            reward_screen(self.screen, self.owner.reward, message_log)
        elif self.owner.state == GameStates.MENUS:
            if self.owner.menus.state == MenuStates.PARTY:
                character_screen(self.screen, player)
            elif self.owner.menus.state == MenuStates.JOURNAL:
                journal_screen(self.screen, self.owner.menus)
            elif self.owner.menus.state == MenuStates.INVENTORY:
                inventory_screen(self.screen, self.owner.menus)

    def draw_entity(self, cx, cy, entity, fov_map, game_map, tilesize):

        surfimg = entity.images.sprite

        if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (
                entity.transition and game_map.tiles[entity.x][entity.y].explored):
            self.screen.blit(surfimg, ((entity.x - cx) * tilesize, (entity.y - cy) * tilesize))

    def draw_structure(self, cx, cy, structure, fov_map, game_map, tilesize):

        count = 0
        for j in range(structure.rect.y1, structure.rect.y2):
            for i in range(structure.rect.x1, structure.rect.x2):
                visible = libtcod.map_is_in_fov(fov_map, i, j)
                if visible:
                    self.screen.blit(structure.file_objs[0][count], ((i - cx) * tilesize, (j - cy) * tilesize))
                    count += 1
                elif game_map.tiles[i][j].explored:
                    self.screen.blit(structure.file_objs[1][count], ((i - cx) * tilesize, (j - cy) * tilesize))
                    count += 1
                else:
                    self.screen.blit(TILE_BASE.get('black'), ((i - cx) * tilesize, (j - cy) * tilesize))
                    count += 1

    def draw_tile(self, fov_map, game_map, x, y, cx, cy, tilesize):

        visible = libtcod.map_is_in_fov(fov_map, cx + x, cy + y)

        tile = game_map.tiles[cx + x][cy + y]

        if visible:
            self.screen.blit(tile.image, (x * tilesize, y * tilesize))
            tile.explored = True
        elif tile.explored:
           self.screen.blit(tile.image2, (x * tilesize, y * tilesize))
        else:
            self.screen.blit(TILE_BASE.get('black'), (x * tilesize, y * tilesize))