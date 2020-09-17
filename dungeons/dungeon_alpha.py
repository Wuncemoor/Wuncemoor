from ECS.entity import Entity
from ECS.__entity.age import Age
from ECS.__entity.noncombatant import Noncombatant
from config.image_objects import BUNDLE_SAMWISE
from dialogue.get_dialogue import get_samwise_dialogue
from enums.render_order import RenderOrder
from map_objects.majorroad import MajorRoad
from map_objects.rect import Rect
from prefabs.alpha_prefabs import TownAlphaInn


class DungeonAlphaMixin:
    """Mixin for DungeonAlphaBuilder, adds functionality unique to starting town"""

    @staticmethod
    def get_samwise():

        dialogue = get_samwise_dialogue()
        noncom = Noncombatant('samwise', BUNDLE_SAMWISE, dialogue)
        age = Age(13, 12, 28, 0, (1, 4))
        samwise = Entity(5, 16, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
        return samwise

    def get_major_road(self):
        rect = Rect(0, int(self.height / 2) - 2, self.width, 4)
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        return road

    def get_structures(self):
        structures = [TownAlphaInn]
        return structures

    def get_rects(self):
        rects = [Rect(25, 25, 9, 7)]
        return rects



