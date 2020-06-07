from screens.gui_tools import get_alpha_surface, print_message



def get_message_box(bg, log, off_x, off_y):

    window = get_alpha_surface(bg.get_width(), bg.get_height())
    window.blit(bg, (0, 0))

    y = 0
    for message in log.messages:
        print_message(window, message, off_x, off_y, y)
        y += 1


    return window

