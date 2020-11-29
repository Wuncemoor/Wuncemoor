from pygame.surface import Surface


class ImageBundle:
    """A collection of images for Entities who need it"""

    def __init__(self, sprite_dict: dict = None, sprite: list = None, portrait: Surface = None,
                 port_mini: Surface = None, actor: Surface = None) -> None:
        self.sprite_dict = sprite_dict
        self.sprite = sprite
        self.portrait = portrait
        self.port_mini = port_mini
        self.actor = actor
