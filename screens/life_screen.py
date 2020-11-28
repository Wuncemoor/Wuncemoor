import math

from numpy.core._multiarray_umath import sqrt
import tcod
from pygame.surface import Surface
from pygame.transform import scale
from config.constants import WHITE, TILES_ON_SCREEN, TILESIZE, BLACK, TRANSPARENT, LIFE_PANEL_WIDTH, LIFE_PANEL_HEIGHT
from config.image_objects import RESOURCE_HUD_BASE, RESOURCE_HUD_OVERLAY, HP, MP, TP, VP, TILE_BASE, \
    PARTY_SETTINGS_FRAME, MINI_MAP, CLOCK, UPCOMING_EVENTS, EVENT_LOG_BG
from screens.displays.calendar import display_calendar
from screens.gui_tools import get_alpha_surface, get_text_surface, get_surface, align_and_blit, print_message


def get_life_left_panel(party):
    panel = get_alpha_surface(LIFE_PANEL_WIDTH, LIFE_PANEL_HEIGHT)
    party_resources_hud = get_life_party_resources(party)
    party_travel_settings = get_life_party_travel_settings(party)
    panel.blit(party_resources_hud, (8, 36))
    panel.blit(party_travel_settings, (8, 36 + party_resources_hud.get_height()))
    return panel


def get_life_party_resources(party):
    party_resources = get_alpha_surface(RESOURCE_HUD_BASE.get_width(), RESOURCE_HUD_BASE.get_height()*4)
    ind = 0
    for member in party.member_slots:
        location_to_blit = (0, ind * RESOURCE_HUD_BASE.get_height())
        party_resources.blit(RESOURCE_HUD_BASE, location_to_blit)
        if member is not None:
            party_resources.blit(get_life_cropped_portrait(member), location_to_blit)
        party_resources.blit(RESOURCE_HUD_OVERLAY, location_to_blit)
        if member is not None:
            party_resources.blit(get_life_member_stats(member), location_to_blit)
        ind += 1

    return party_resources


def get_life_cropped_portrait(entity):
    cropped = get_alpha_surface(83, 83)
    align_and_blit(cropped, entity.images.port_mini)
    center_x, center_y = 42, 42
    for y in range(83):
        for x in range(83):
            out_of_bounds = sqrt((y - center_y)*(y - center_y) + (x - center_x)*(x - center_x)) > 33
            if out_of_bounds:
                cropped.set_at((x, y), TRANSPARENT)
    return cropped


def get_life_member_stats(entity):
    stats = get_alpha_surface(RESOURCE_HUD_BASE.get_width(), RESOURCE_HUD_BASE.get_height())
    name = get_text_surface(entity.combatant.name, fontsize=12, color=WHITE)
    level = get_text_surface(str(entity.combatant.level.current_level), fontsize=12, color=WHITE)
    hp = get_surface(HP)
    mp = get_surface(MP)
    tp = get_surface(TP)
    vp = get_surface(VP)

    percent_hp = entity.combatant.attributes.current_hp/entity.combatant.max_hp
    percent_mp = entity.combatant.attributes.current_mp/entity.combatant.max_mp
    percent_tp = entity.combatant.attributes.current_tp/entity.combatant.max_tp
    percent_vp = entity.combatant.attributes.current_vp/entity.combatant.max_vp

    stats.blit(name, (95, 0))
    stats.blit(level, (65, 60))
    stats.blit(scale(hp, (int(hp.get_width()*percent_hp), hp.get_height())), (86, 22))
    stats.blit(scale(mp, (int(mp.get_width()*percent_mp), mp.get_height())), (86, 34))
    stats.blit(scale(tp, (int(tp.get_width()*percent_tp), tp.get_height())), (86, 46))
    stats.blit(scale(vp, (int(vp.get_width()*percent_vp), vp.get_height())), (86, 58))

    return stats


def get_life_party_travel_settings(party):
    window = get_alpha_surface(248, 186)
    setting_titles = ['Formation', 'Move Speed', 'Rations']
    settings = [party.formation, party.move_speed, party.rations]
    for i in range(3):
        settings_frame = get_surface(PARTY_SETTINGS_FRAME)
        setting_title = get_text_surface(setting_titles[i], color=WHITE)
        align_and_blit(settings_frame, setting_title, y_ratio=0.24)
        setting = get_text_surface(settings[i], fontsize=16)
        align_and_blit(settings_frame, setting, y_ratio=0.68)
        window.blit(settings_frame, (0, i*settings_frame.get_height()))
    return window


def get_life_main_screen(self):
    main_screen = get_alpha_surface(1392, 1008)
    (width, height) = TILES_ON_SCREEN

    cx, cy = self.handler.camera.x, self.handler.camera.y
    largest_overhead = 3

    if self.handler.fov.needs_recompute:
        self.handler.fov.recompute()
        self.handler.fov.needs_recompute = False

    is_interior = is_party_on_interior_tile(self.game.party, self.game.world.tiles)
    for y in range(height + largest_overhead):
        for x in range(width):
            try:
                visible = tcod.map_is_in_fov(self.handler.fov.map, cy + y, cx + x)
                tile = self.game.world.tiles[cy + y][cx + x]

                draw_tile(main_screen, self.game.world.tiles, tile, x, y, cx, cy, visible, is_interior)

                if not visible and not tile.floor.transition:
                    draw_darkened_overlay(main_screen, x, y)
            except IndexError:
                pass

    for noncom in self.game.world.current_map.noncombatants:
        draw_entity(self, main_screen, noncom)
    entities_in_render_order = sorted(self.game.world.current_map.entities, key=lambda x: x.render_order.value)
    for entity in entities_in_render_order:
        self.draw_entity(entity)

    draw_party(self, main_screen)
    return main_screen


def is_party_on_interior_tile(party, tiles):
    tile = tiles[party.y][party.x]
    if tile.is_interior:
        return True
    return False


def draw_entity(self, main_screen, entity):
    cx, cy = self.handler.camera.x, self.handler.camera.y
    sprite = entity.images.sprite

    if tcod.map_is_in_fov(self.handler.fov.map, entity.y, entity.x):
        main_screen.blit(sprite[self.frame], ((entity.x - cx) * TILESIZE, (entity.y - cy) * TILESIZE - (TILESIZE/3)))


def draw_party(self, main_screen):
    cx, cy = self.handler.camera.x, self.handler.camera.y
    party = self.game.party

    sprite = party.p1.images.sprite

    main_screen.blit(sprite[self.frame], ((party.x - cx) * TILESIZE, (party.y - cy) * TILESIZE - (TILESIZE/3)))


def draw_tile(main_screen, tiles, tile, x, y, cx, cy, visible, is_interior):

    draw_tile_floor(main_screen, tile, x, y, visible)
    draw_tile_decoration(main_screen, tile, x, y, visible)
    draw_tile_blocker(main_screen, tile, x, y)
    draw_tile_overhead(main_screen, tiles, tile, x, y, cx, cy, is_interior)


def draw_tile_floor(main_screen, tile, x, y, vis):

    if vis:
        main_screen.blit(tile.floor.image, (x * TILESIZE, y * TILESIZE))
        tile.explored = True
    elif tile.explored:
        main_screen.blit(tile.floor.image, (x * TILESIZE, y * TILESIZE))
    else:
        main_screen.blit(TILE_BASE.get('black'), (x * TILESIZE, y * TILESIZE))


def draw_tile_decoration(main_screen, tile, x, y, vis):
    if tile.decoration and (vis or (tile.explored and tile.floor.transition)):
        main_screen.blit(tile.decoration.image, (x * TILESIZE, y * TILESIZE))


def draw_tile_blocker(main_screen, tile, x, y):
    if tile.blocker and tile.explored:
        main_screen.blit(tile.blocker.image, (x * TILESIZE, y * TILESIZE))


def draw_tile_overhead(main_screen, tiles, tile, x, y, cx, cy, interior):
    if tile.overhead:
        for obj in tile.overhead:
            associated_tile = tiles[cy + y - obj.distance_overhead][cx + x]
            if (tile.explored or associated_tile.explored) and interior is False:
                main_screen.blit(obj.image, (x * TILESIZE, ((y - obj.distance_overhead) * TILESIZE)))


def draw_darkened_overlay(main_screen, x, y):
    main_screen.blit(get_darkened_overlay(), (x * TILESIZE, y * TILESIZE))


def get_darkened_overlay():
    overlay = Surface((TILESIZE, TILESIZE))
    overlay.fill(BLACK)
    overlay.set_alpha(100)
    return overlay


def get_life_right_panel(game):
    off_x, off_y = 8, 36
    panel = get_alpha_surface(LIFE_PANEL_WIDTH, LIFE_PANEL_HEIGHT)

    for display in [get_life_minimap(), get_life_clock(), display_calendar(game.time), get_upcoming_events(),
                    get_life_event_log(game.log)]:
        panel.blit(display, (off_x, off_y))
        off_y += display.get_height()

    return panel


def get_life_minimap():
    minimap = get_surface(MINI_MAP)
    return minimap


def get_life_clock():
    clock = get_surface(CLOCK)
    return clock


def get_upcoming_events():
    events = get_surface(UPCOMING_EVENTS)
    return events


def get_life_event_log(log):
    event_log = get_surface(EVENT_LOG_BG)
    y = 0
    for message in log.messages.messages:
        off_x = 5
        off_y = 5
        print_message(event_log, message, off_x, off_y, y)
        y += 1
    return event_log
