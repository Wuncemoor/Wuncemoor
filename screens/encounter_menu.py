from screens.gui_tools import get_alpha_surface, get_text_surface


def get_encounter_menu(images, options, current_option):

    menu = get_alpha_surface(400, 240)

    menu_off_x = 60
    menu_off_y = 0
    menu.blit(images.get('encounter_menu'), (menu_off_x, menu_off_y))

    buttons_off_x = 130
    buttons_off_y = 30

    dy = 40
    num = 3
    blit_options(menu, images.get('button'), buttons_off_x, buttons_off_y, dy, num, options)

    indicator_y = buttons_off_y - 11 + (dy * current_option)

    blit_indicator(menu, images.get('indicator'), off_x=buttons_off_x - 50, off_y=indicator_y)

    return menu


def blit_options(menu, image, off_x, off_y, dy, num, options):

    for i in range(num):
        text = get_text_surface(options, i, fontsize=24)
        menu.blit(image, (off_x, off_y + (i * dy)))

        mid = image.get_width() / 2
        half = text.get_width() / 2
        menu.blit(text, (off_x + mid - half, off_y + (i * dy) - 5))


def blit_indicator(menu, image, off_x, off_y):
    menu.blit(image, (off_x, off_y))
