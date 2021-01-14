from abstracts.abstract_menu import TopLevelMenu
from mixins.menu_mixins.menu_composites.simple_composites import DescendingFancyTextData, DescendingStaticImagePointer
from mixins.menu_mixins.menu_primitives.dependent_primitives import StandardBlittables


class FancyMenu(DescendingFancyTextData, DescendingStaticImagePointer, StandardBlittables, TopLevelMenu):
    """A custom Menu built through multiple inheritance. As a TopLevelMenu, it has a bg_image and it displays a list of
    Blittables on top of the background as a single image. This image is then returned to the ArtistHandler."""
