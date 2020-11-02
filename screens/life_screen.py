from numpy.core._multiarray_umath import sqrt
import tcod
from pygame.transform import scale

from config.constants import WHITE, TILES_ON_SCREEN
from config.image_objects import RESOURCE_HUD_BASE, RESOURCE_HUD_OVERLAY, HP, MP, TP, VP, TILE_BASE
from screens.gui_tools import get_alpha_surface, get_text_surface, get_surface, align_and_blit


def get_life_left_panel(party):
    PANEL_WIDTH, PANEL_HEIGHT = 264, 1080
    panel = get_alpha_surface(PANEL_WIDTH, PANEL_HEIGHT)
    party_resources_hud = get_life_party_resources(party)
    panel.blit(party_resources_hud, (8, 36))
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
                cropped.set_at((x, y), (128, 175, 120))
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


def get_life_main_screen(self):
    main_screen = get_alpha_surface(1392, 1008)
    (width, height) = TILES_ON_SCREEN

    cx, cy = self.handler.camera.x, self.handler.camera.y

    if self.handler.fov.needs_recompute:
        self.handler.fov.recompute()
        self.handler.fov.needs_recompute = False

    for y in range(height):
        for x in range(width):
            visible = tcod.map_is_in_fov(self.handler.fov.map, cy + y, cx + x)
            tile = self.game.world.tiles[cy + y][cx + x]
            draw_tile_floor(main_screen, tile, x, y, visible)

    for noncom in self.game.world.current_map.noncombatants:
        draw_entity(self, main_screen, noncom)
    entities_in_render_order = sorted(self.game.world.current_map.entities, key=lambda x: x.render_order.value)
    for entity in entities_in_render_order:
        self.draw_entity(entity)

    for y in range(height):
        for x in range(width):
            visible = tcod.map_is_in_fov(self.handler.fov.map, cy + y, cx + x)
            tile = self.game.world.tiles[cy + y][cx + x]
            if tile.blocker and tile.explored:
                draw_tile_blocker(main_screen, tile, x, y, visible)

    draw_party(self, main_screen)
    return main_screen


def draw_entity(self, main_screen, entity):
    cx, cy = self.handler.camera.x, self.handler.camera.y

    surfimg = entity.images.sprite

    if tcod.map_is_in_fov(self.handler.fov.map, entity.y, entity.x):
        main_screen.blit(surfimg, ((entity.x - cx) * self.tilesize, (entity.y - cy) * self.tilesize))


def draw_party(self, main_screen):
    cx, cy = self.handler.camera.x, self.handler.camera.y
    party = self.game.party

    surfimg = party.p1.images.sprite

    main_screen.blit(surfimg, ((party.x - cx) * self.tilesize, (party.y - cy) * self.tilesize))


def draw_tile_floor(main_screen, tile, x, y, vis):
    if vis or (tile.explored and tile.floor.transition):
        main_screen.blit(tile.floor.light_image, (x * 16, y * 16))
        tile.explored = True
    elif tile.explored:
        main_screen.blit(tile.floor.dark_image, (x * 16, y * 16))
    else:
        main_screen.blit(TILE_BASE.get('black'), (x * 16, y * 16))


def draw_tile_blocker(main_screen, tile, x, y, vis):
    if vis:
        main_screen.blit(tile.blocker.light_image, (x * 16, y * 16))
    else:
        main_screen.blit(tile.blocker.dark_image, (x * 16, y * 16))




