import tcod as libtcod
from config.constants import TILES_ON_SCREEN, BLACK
from config.image_objects import MESSAGE_BG, TILE_BASE, TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H
from enums.game_states import GameStates, MenuStates
from menus import level_up_menu
from screens.calendar import display_calendar
from screens.character_screen import character_screen
from screens.dialogue_screen import dialogue_screen
from screens.encounter_screen import encounter_screen
from screens.gui_tools import get_surface, print_message, align_and_blit, blit_options
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.reward_screen import reward_screen
from screens.mini_map import minimap_screen
from screens.resources_HUD import player_resource_display
from pygame.font import Font


class ArtistHandler:
    def __init__(self, screen):
        self.screen = screen
        self.world_tiles = None
        self.tilesize = 16

    @property
    def options(self):
        return [option.display for option in self.owner.options.current.options]

    @property
    def choice(self):
        return self.owner.options.current.choice

    @property
    def handler(self):
        return self.owner.state_handler

    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.loot,
            # GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

    def render(self):
        return self.mapping()

    def title(self):
        self.screen.blit(TITLE_SCREEN_BG, (0, 0))

        tfont = Font('screens\\fonts\\lunchds.ttf', 150)
        stfont = Font('screens\\fonts\\lunchds.ttf', 60)
        titletext = tfont.render('WUNCEMOOR', True, (0, 0, 0))
        tsubt = stfont.render('THE ETERNAL DREAM', True, (0, 0, 0))

        align_and_blit(self.screen, titletext, x_ratio=0.5, y_ratio=0.25)
        align_and_blit(self.screen, tsubt, x_ratio=0.5, y_ratio=0.38)
        menu = self.title_menu()
        align_and_blit(self.screen, menu, x_ratio=0.5, y_ratio=0.75)

    def title_menu(self):
        surf = get_surface(TITLE_MENU_BG)
        blit_options(surf, TITLE_MENU_BUTTON, 22, 10, TITLE_MENU_BUTTON.get_height(), self.options, fontsize=40)
        surf.blit(INDICATOR_H, (0, 10 + (self.choice * TITLE_MENU_BUTTON.get_height())))

        return surf

    def life(self):
        (width, height) = TILES_ON_SCREEN

        if self.handler.fov.needs_recompute:
            self.handler.fov.recompute()

        if self.handler.fov.recompute:
            for y in range(height):
                for x in range(width):
                    self.draw_tile(x, y)

        for structure in self.owner.world.current_map.structures:
            self.draw_structure(structure)
        for transition in self.owner.world.current_map.transitions:
            self.draw_entity(transition)
        for noncom in self.owner.world.current_map.noncombatants:
            self.draw_entity(noncom)
        # draw all entities in list
        entities_in_render_order = sorted(self.owner.world.current_map.entities, key=lambda x: x.render_order.value)
        for entity in entities_in_render_order:
            self.draw_entity(entity)
        self.draw_party()

        # Print game messages one line at a time

        message_surface = get_surface(MESSAGE_BG)
        y = 0
        for message in self.owner.log.messages.messages:
            off_x = 30
            off_y = 5
            print_message(message_surface, message, off_x, off_y, y)
            y += 1

        self.screen.blit(message_surface, (300, 592))
        message_surface.fill(BLACK)

        resource_hud = player_resource_display(self.owner.party.p1)
        self.screen.blit(resource_hud, (0 - 10, 540 + 40))

        calendar = display_calendar(self.owner.time.month, self.owner.time.day)

        self.screen.blit(calendar, (self.screen.get_width() - calendar.get_width(), self.screen.get_height() - calendar.get_height()))

    def menus(self):
        if self.handler.state == MenuStates.PARTY:
            character_screen(self)
        elif self.handler.state == MenuStates.JOURNAL:
            journal_screen(self)
        elif self.handler.state == MenuStates.INVENTORY:
            inventory_screen(self)
        elif self.handler.state == MenuStates.MAP:
            minimap_screen(self)

    def render_all(self):
        (width, height) = TILES_ON_SCREEN

        if self.fov.needs_recompute:
            self.fov.recompute()

        # Draw tiles near player
        if self.fov.recompute:
            for y in range(height):
                for x in range(width):
                    self.draw_tile(self.owner.world, x, y, self.tilesize)

        for structure in self.owner.world.current_map.structures:
            self.draw_structure(self.camera.x, self.camera.y, structure, self.fov.map, self.owner.world, self.tilesize)
        for transition in self.owner.world.current_map.transitions:
            self.draw_entity(self.camera.x, self.camera.y, transition, self.fov.map, self.owner.world, self.tilesize)
        for noncom in self.owner.world.current_map.noncombatants:
            self.draw_entity(self.camera.x, self.camera.y, noncom, self.fov.map, self.owner.world, self.tilesize)
        # draw all entities in list
        entities_in_render_order = sorted(self.owner.world.current_map.entities, key=lambda x: x.render_order.value)
        for entity in entities_in_render_order:
            self.draw_entity(self.camera.x, self.camera.y, entity, self.fov.map, self.owner.world, self.tilesize)
        self.draw_party(self.camera.x, self.camera.y, self.owner.party.p1, self.fov.map, self.owner.world, self.tilesize)

        # Print game messages one line at a time

        message_surface = get_surface(MESSAGE_BG)
        y = 0
        for message in self.owner.log.messages:
            off_x = 30
            off_y = 5
            print_message(message_surface, message, off_x, off_y, y)
            y += 1

        self.screen.blit(message_surface, (300, 592))
        message_surface.fill(BLACK)

        resource_hud = player_resource_display(self.owner.party.p1)
        self.screen.blit(resource_hud, (0 - 10, 540 + 40))

        calendar = display_calendar(self.owner.time.month, self.owner.time.day)
        if self.owner.state == GameStates.TITLE:
            self.title_screen()
        if self.owner.state == GameStates.LIFE:
            self.screen.blit(calendar, (self.screen.get_width() - calendar.get_width(), self.screen.get_height() - calendar.get_height()))

        if self.owner.state == GameStates.SHOW_MAP:
            minimap_screen(self.screen, self.world_tiles)
        elif self.owner.state == GameStates.LEVEL_UP:
            level_up_menu(self.screen, self.owner.party.p1)
        elif self.owner.state == GameStates.DIALOGUE:
            dialogue_screen(self.screen, self.owner.party.p1, self.owner.dialogue)
        elif self.owner.state == GameStates.ENCOUNTER:
            encounter_screen(self.screen, self.owner.party.p1, self.owner.encounter, self.owner.log)
        elif self.owner.state == GameStates.REWARD:
            reward_screen(self.screen, self.owner.reward, self.owner.log)
        elif self.owner.state == GameStates.MENUS:
            if self.owner.menus.state == MenuStates.PARTY:
                character_screen(self.screen, self.owner.party.p1)
            elif self.owner.menus.state == MenuStates.JOURNAL:
                journal_screen(self.screen, self.owner.menus)
            elif self.owner.menus.state == MenuStates.INVENTORY:
                inventory_screen(self.screen, self.owner.menus)
        self.fov.needs_recompute = False

    def draw_entity(self, entity):
        cx, cy = self.handler.camera.x, self.handler.camera.y

        surfimg = entity.images.sprite

        if libtcod.map_is_in_fov(self.handler.fov.map, entity.x, entity.y) or (
                entity.transition and self.owner.world.tiles[entity.x][entity.y].explored):
            self.screen.blit(surfimg, ((entity.x - cx) * self.tilesize, (entity.y - cy) * self.tilesize))

    def draw_party(self):
        cx, cy = self.handler.camera.x, self.handler.camera.y
        party = self.owner.party

        surfimg = party.p1.images.sprite

        self.screen.blit(surfimg, ((party.x - cx) * self.tilesize, (party.y - cy) * self.tilesize))

    def draw_structure(self, structure):
        cx, cy = self.handler.camera.x, self.handler.camera.y

        count = 0
        for j in range(structure.rect.y1, structure.rect.y2):
            for i in range(structure.rect.x1, structure.rect.x2):
                visible = libtcod.map_is_in_fov(self.handler.fov.map, i, j)
                if visible:
                    self.screen.blit(structure.file_objs[0][count], ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
                    count += 1
                elif self.owner.world.tiles[i][j].explored:
                    self.screen.blit(structure.file_objs[1][count], ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
                    count += 1
                else:
                    self.screen.blit(TILE_BASE.get('black'), ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
                    count += 1

    def draw_tile(self, x, y):
        cx, cy = self.handler.camera.x, self.handler.camera.y

        visible = libtcod.map_is_in_fov(self.handler.fov.map, cx + x, cy + y)

        tile = self.owner.world.tiles[cx + x][cy + y]

        if visible:
            self.screen.blit(tile.image, (x * self.tilesize, y * self.tilesize))
            tile.explored = True
        elif tile.explored:
            self.screen.blit(tile.image2, (x * self.tilesize, y * self.tilesize))
        else:
            self.screen.blit(TILE_BASE.get('black'), (x * self.tilesize, y * self.tilesize))