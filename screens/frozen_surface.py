import pygame as py


class FrozenSurface(py.Surface):
    """PyGame uses Surface for all view functions including loading image objects. This is a variant to be used to
    give names to image objects. """

    def __init__(self, xy: tuple, name: str):
        super().__init__(xy)
        self.name = name

    @staticmethod
    def load(prefix: str, location: str):
        """prefix is images\\...\\ , location is file_name.file_type"""

        surface = py.image.load(prefix + location)
        fs = FrozenSurface(surface.get_size(), location)
        fs.blit(surface, (0, 0))
        return fs

    def __repr__(self):
        return 'FrozenSurface(' + str(self.get_size()) + ', ' + self.name + ')'
