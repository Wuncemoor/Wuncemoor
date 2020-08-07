class ImageBundle:
    """A collection of images for Entities who need it"""

    def __init__(self, sprite=None, portrait=None, port_mini=None, actor=None):
        self.sprite = sprite
        self.portrait = portrait
        self.port_mini = port_mini
        self.actor = actor