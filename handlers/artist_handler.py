import tcod as libtcod
from config.constants import TILES_ON_SCREEN, BLACK
from config.image_objects import MESSAGE_BG, TILE_BASE, TITLE_SCREEN_BG, TITLE_MENU_BG, TITLE_MENU_BUTTON, INDICATOR_H, \
    ENCOUNTER_MENU, ENCOUNTER_BUTTON, ENCOUNTER_MESSAGE_BG, INDICATOR_V, LOOT_BG, LOOT_BANNER
from enums.game_states import GameStates, MenuStates, EncounterStates
from abstracts.abstract_mvc import MVC
from handlers.logic.options import encounter_window_options
from screens.calendar import display_calendar
from screens.character_screen import character_screen
from screens.debug_window import debug_window
from screens.dialogue_screen import dialogue_screen
from screens.gui_tools import get_surface, print_message, align_and_blit, blit_options, get_alpha_surface
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.loot_menu import display_loot, display_resources_gain, get_reward_menu
from screens.mini_map import minimap_screen
from screens.resources_HUD import player_resource_display
from pygame.font import Font


class ArtistHandler(MVC):
    def __init__(self, screen):
        self.screen = screen
        self.tilesize = 16


    @property
    def choice(self):
        return self.owner.options.current.choice

    def render(self):
        return self.mapping()

    def debug(self):
        debug_window(self)

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
        text = self.owner.options.current.text
        blit_options(surf, TITLE_MENU_BUTTON, 22, 10, TITLE_MENU_BUTTON.get_height(), text, fontsize=40)
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

            self.blit_resource_hud()

            self.blit_calendar()

    def menus(self):
        if self.handler.state == MenuStates.PARTY:
            character_screen(self)
        elif self.handler.state == MenuStates.JOURNAL:
            journal_screen(self)
        elif self.handler.state == MenuStates.INVENTORY:
            inventory_screen(self)
        elif self.handler.state == MenuStates.MAP:
            minimap_screen(self)

    def encounter(self):

        self.screen.blit(self.handler.background, (0, 0))
        self.blit_resource_hud()
        self.blit_encounter_menu()
        self.blit_message_box(off_x=15, off_y=5)
        self.blit_combat()

    def reward(self):

        self.screen.blit(LOOT_BG, (0, 0))
        self.screen.blit(LOOT_BANNER, (320, 0))

        self.blit_message_box(off_x=15, off_y=5)
        loot_visual = display_loot(self.handler)
        self.screen.blit(loot_visual, (0, 300))

        resources = display_resources_gain(self.handler.loot)
        self.screen.blit(resources, (1000, 180))

        loot_menu = get_reward_menu(self.handler)
        self.screen.blit(loot_menu, (0, 0))

    def blit_message_box(self, off_x, off_y):

        window = get_surface(ENCOUNTER_MESSAGE_BG)

        y = 0
        for message in self.owner.log.messages.messages:
            print_message(window, message, off_x, off_y, y)
            y += 1

        self.screen.blit(window, (940, 490))

    def blit_combat(self):
        w, h = 1280, 300
        window = get_alpha_surface(w, h)
        dim = 160
        count = 0
        for row in self.handler.combat.grid.rows:
            for actor in row:
                window.blit(actor.combatant.images.actor, (count * dim, 70))
            count += 1

        if self.handler.state == EncounterStates.FIGHT_TARGETING:
            window.blit(INDICATOR_V, ((self.handler.combat.grid.x * dim) + (dim / 2) - (INDICATOR_V.get_width() / 2), 30))

        self.screen.blit(window, (0, 180))

    def blit_calendar(self):
        calendar = display_calendar(self.owner.time)
        xy = (self.screen.get_width() - calendar.get_width(), self.screen.get_height() - calendar.get_height())
        self.screen.blit(calendar, xy)

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

    # def draw_structure(self, structure):
    #     cx, cy = self.handler.camera.x, self.handler.camera.y
    #
    #     count = 0
    #     for j in range(structure.rect.y1, structure.rect.y2):
    #         for i in range(structure.rect.x1, structure.rect.x2):
    #             visible = libtcod.map_is_in_fov(self.handler.fov.map, i, j)
    #             if visible:
    #                 self.screen.blit(structure.file_objs[0][count], ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
    #                 count += 1
    #             elif self.owner.world.tiles[i][j].explored:
    #                 self.screen.blit(structure.file_objs[1][count], ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
    #                 count += 1
    #             else:
    #                 self.screen.blit(TILE_BASE.get('black'), ((i - cx) * self.tilesize, (j - cy) * self.tilesize))
    #                 count += 1

    def draw_tile(self, x, y):
        cx, cy = self.handler.camera.x, self.handler.camera.y

        visible = libtcod.map_is_in_fov(self.handler.fov.map, cx + x, cy + y)

        tile = self.owner.world.tiles[cx + x][cy + y]

        if visible:
            self.screen.blit(tile.floor.light_image, (x * self.tilesize, y * self.tilesize))
            tile.explored = True
        elif tile.explored:
            self.screen.blit(tile.floor.dark_image, (x * self.tilesize, y * self.tilesize))
        else:
            self.screen.blit(TILE_BASE.get('black'), (x * self.tilesize, y * self.tilesize))

    def dialogue(self):
        dialogue_screen(self)

    def blit_resource_hud(self):
        resource_hud = player_resource_display(self.owner.party.p1)
        coord_dict = {
            GameStates.LIFE: (0 - 10, 540 + 40),
            GameStates.ENCOUNTER: (0, 0),
        }
        xy = coord_dict.get(self.state)
        self.screen.blit(resource_hud, xy)

    def blit_encounter_menu(self):

        menu = get_alpha_surface(400, 240)

        align_and_blit(menu, ENCOUNTER_MENU)

        buttons_off_x = 130
        buttons_off_y = 60
        text = encounter_window_options().text

        dy = 40
        blit_options(menu, ENCOUNTER_BUTTON, buttons_off_x, buttons_off_y, dy, text, fontsize=24)

        if self.handler.state == EncounterStates.THINKING:
            menu.blit(INDICATOR_H, (buttons_off_x - 50, buttons_off_y - 11 + (dy * self.owner.options.current.choice)))

        self.screen.blit(menu, (0, 480))
