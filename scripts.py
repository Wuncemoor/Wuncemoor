from data_structures.gui_tools import get_text_surface, string_to_font_style_dict
import pygame


def glyph_dimensions():
    pygame.init()
    keys = STRING_TO_FONT_STYLE_DICT.keys()
    with open('script_outputs/glyph_dimensions.py', 'w') as opened_file:
        opened_file.write('glyph_dim_dict = {\n')
        for unicode in [x for x in range(32, 127)]:
            for fontsize in range(3, 72):
                for fontstyle in keys:
                    glyph = chr(unicode)
                    surf = get_text_surface(glyph)

                    if unicode == 39: # Must use double quotes to store single quote
                        opened_file.write('    ("' + glyph + '", ' + str(fontsize) + ", '" + fontstyle + "'): (" +
                                          str(surf.get_width()) + ", " + str(surf.get_height()) + "),\n")
                    elif unicode == 92:  # Must use double slash to deal with special backslashes
                        opened_file.write("    ('" + glyph + glyph + "', " + str(fontsize) + ", '" + fontstyle + "'): (" +
                                          str(surf.get_width()) + ", " + str(surf.get_height()) + "),\n")
                    else:
                        opened_file.write("    ('" + glyph + "', " + str(fontsize) + ", '" + fontstyle + "'): (" +
                                          str(surf.get_width()) + ", " + str(surf.get_height()) + "),\n")
        opened_file.write('}\n')


if __name__ == '__main__':
    glyph_dimensions()