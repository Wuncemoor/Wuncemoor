from pygame.surface import Surface

from config.constants import BLACK
from config.image_objects import INDICATOR_H, ENCOUNTER_MENU, ENCOUNTER_BUTTON, ENCOUNTER_MESSAGE_BG, INDICATOR_V,\
    REWARD_BG, LOOT_BANNER, LIFE_BACKDROP, TURN_ORDER_QUEUE
from enums.game_states import GameStates, MenuStates, EncounterStates
from abstracts.abstract_mvc import MVC
from screens.character_screen import character_screen
from screens.debug_window import debug_window
from screens.dialogue_screen import dialogue_screen
from screens.life_screen import get_life_left_panel, get_life_main_screen, get_life_right_panel
from screens.shop_screen import shop_screen
from data_structures.gui_tools import get_surface, print_message, align_and_blit, blit_options, get_alpha_surface
from screens.inventory_screen import inventory_screen
from screens.journal_screen import journal_screen
from screens.reward_screen import display_loot, display_resources_gain, get_reward_thinking_menu
from screens.map_screen import map_screen
from screens.resources_HUD import player_resource_display

from screens.title_screen import title_screen


class ArtistHandler(MVC):
    def __init__(self, game, screen, clock):
        super().__init__(game)
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
        title_screen(self)

    def life(self):

        life_backdrop = get_surface(LIFE_BACKDROP)
        self.screen.blit(life_backdrop, (0, 0))

        left_panel = get_life_left_panel(self.game.model.party)
        self.screen.blit(left_panel, (0, 0))

        main_screen = get_life_main_screen(self)
        self.screen.blit(main_screen, (264, 36))

        right_panel = get_life_right_panel(self.game)
        self.screen.blit(right_panel, (1654, 0))

    def menus(self):
        self.life()
        self.darken_main_screen()
        if self.handler.state == MenuStates.CHAR_SHEET:
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
        self.screen.blit(self.handler.menu.get_window_image(), (0, 840))
        window = self.get_message_box(off_x=15, off_y=5)
        self.screen.blit(window, (1540, 870))
        self.blit_turn_order_queue()
        self.blit_combat()

    def reward(self):

        align_and_blit(self.screen, self.handler.menu.get_window_image())

        # menu = get_surface(REWARD_BG)
        # menu.blit(LOOT_BANNER, (320, 0))
        #
        # window = self.get_message_box(off_x=15, off_y=5)
        # align_and_blit(menu, window, x_ratio=0.8, y_ratio=0.8)
        #
        # loot_visual = display_loot(self.handler)
        # menu.blit(loot_visual, (0, 300))
        #
        # resources = display_resources_gain(self.handler.loot)
        # menu.blit(resources, (1000, 180))
        #
        # loot_menu = get_reward_thinking_menu(self.handler)
        # menu.blit(loot_menu, (0, 0))


    def get_message_box(self, off_x, off_y):

        window = get_surface(ENCOUNTER_MESSAGE_BG)

        y = 0
        for message in self.game.model.log.messages.messages:
            print_message(window, message, off_x, off_y, y)
            y += 1
        return window

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
        self.life()
        self.darken_main_screen()
        dialogue_screen(self)

    def shop(self):
        shop_screen(self)

    def blit_resource_hud(self):
        resource_hud = player_resource_display(self.game.model.party.p1)
        coord_dict = {
            GameStates.LIFE: (0 - 10, 540 + 40),
            GameStates.ENCOUNTER: (360, 900),
        }
        xy = coord_dict.get(self.state)
        self.screen.blit(resource_hud, xy)

    def blit_turn_order_queue(self):
        toq = get_surface(TURN_ORDER_QUEUE)
        align_and_blit(self.screen, toq, x_ratio=0.15, y_ratio=0.05)

    # make property?
    def set_frame(self):
        self.frame = (self.frame + 1) % 12

    def darken_main_screen(self):
        dark = Surface((1392, 1008))
        dark.fill(BLACK)
        dark.set_alpha(150)
        self.screen.blit(dark, (264, 36))

