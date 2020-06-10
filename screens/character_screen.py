from screens.gui_tools import get_alpha_surface
def character_screen(screen, images, player):
    surf = get_alpha_surface(1280, 720)
    surf.blit(images.get('gui').get('character_screen'), (215, 136))
    surf.blit(images.get('gui').get('character_screen'), (640, 136))
    screen.blit(surf, (0, 0))