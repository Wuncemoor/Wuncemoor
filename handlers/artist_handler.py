from pygame.surface import Surface

from config.constants import BLACK, GREY
from config.image_objects import TITLE_SCREEN_BG, INDICATOR_H, ENCOUNTER_MENU, ENCOUNTER_BUTTON, \
    ENCOUNTER_MESSAGE_BG, INDICATOR_V, LOOT_BG, LOOT_BANNER, LIFE_BACKDROP, TURN_ORDER_QUEUE
from enums.game_states import GameStates, MenuStates, EncounterStates
from abstracts.abstract_mvc import MVC
from handlers.logic.options import encounter_window_options
from screens.character_screen import character_screen
from screens.debug_window import debug_window
from screens.dialogue_screen import dialogue_screen
from screens.life_screen import get_life_left_panel, get_life_main_screen, get_life_right_panel
from screens.shop_screen import shop_screen
from screens.gui_tools import get_surface, print_message, align_and_blit, blit_options, get_alpha_surface
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.loot_menu import display_loot, display_resources_gain, get_reward_menu
from screens.map_screen import map_screen
from screens.resources_HUD import player_resource_display

from screens.title_screen import get_title_text, get_title_menu


class ArtistHandler(MVC):
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.frame = 0

    @property
    def choice(self):
        return self.game.options.current.choice

    def render(self):
        self.set_frame()
        return self.mapping()

    def debug(self):
        debug_window(self)

    def title(self):
        self.screen.blit(TITLE_SCREEN_BG, (0, 0))

        text, subtext = get_title_text()
        align_and_blit(self.screen, text, x_ratio=0.5, y_ratio=0.15)
        align_and_blit(self.screen, subtext, x_ratio=0.5, y_ratio=0.28)

        menu = get_title_menu(self.game.options.current)
        align_and_blit(self.screen, menu, x_ratio=0.5, y_ratio=0.75)

    def life(self):

        life_backdrop = get_surface(LIFE_BACKDROP)
        self.screen.blit(life_backdrop, (0, 0))

        left_panel = get_life_left_panel(self.game.party)
        self.screen.blit(left_panel, (0, 0))

        main_screen = get_life_main_screen(self)
        self.screen.blit(main_screen, (264, 36))

        right_panel = get_life_right_panel(self.game)
        self.screen.blit(right_panel, (1654, 0))

    def menus(self):
        self.life()
        self.darken_main_screen()
        if self.handler.state == MenuStates.PARTY:
            character_screen(self)
        elif self.handler.state == MenuStates.JOURNAL:
            journal_screen(self)
        elif self.handler.state == MenuStates.INVENTORY:
            inventory_screen(self)
        elif self.handler.state == MenuStates.MAP:
            map_screen(self)

    def encounter(self):

        self.screen.blit(self.handler.background, (0, 0))
        self.blit_resource_hud()
        self.blit_encounter_menu()
        self.blit_message_box(off_x=15, off_y=5)
        self.blit_turn_order_queue()
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
        for message in self.game.log.messages.messages:
            print_message(window, message, off_x, off_y, y)
            y += 1

        self.screen.blit(window, (1540, 870))

    def blit_combat(self):
        w, h = 1920, 1280
        window = get_alpha_surface(w, h)
        dim = 240
        count = 0
        for row in self.handler.combat.grid.rows:
            for actor in row:
                window.blit(actor.combatant.images.actor, (count * dim, 700))
            count += 1

        if self.handler.state == EncounterStates.FIGHT_TARGETING:
            window.blit(INDICATOR_V, ((self.handler.combat.grid.x * dim) + (dim / 2) - (INDICATOR_V.get_width() / 2), 650))

        self.screen.blit(window, (0, 0))

    def dialogue(self):
        dialogue_screen(self)

    def shop(self):
        shop_screen(self)

    def blit_resource_hud(self):
        resource_hud = player_resource_display(self.game.party.p1)
        coord_dict = {
            GameStates.LIFE: (0 - 10, 540 + 40),
            GameStates.ENCOUNTER: (360, 900),
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
            menu.blit(INDICATOR_H, (buttons_off_x - 50, buttons_off_y - 11 + (dy * self.game.options.current.choice)))

        self.screen.blit(menu, (0, 840))

    def blit_turn_order_queue(self):
        toq = get_surface(TURN_ORDER_QUEUE)
        align_and_blit(self.screen, toq, x_ratio=0.15, y_ratio=0.05)

    def set_frame(self):
        self.frame += 1
        if self.frame >= 12:
            self.frame = 0

    def darken_main_screen(self):
        dark = Surface((1392, 1008))
        dark.fill(BLACK)
        dark.set_alpha(150)
        self.screen.blit(dark, (264, 36))

