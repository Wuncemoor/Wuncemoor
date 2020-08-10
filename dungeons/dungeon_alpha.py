from ECS.entity import Entity
from ECS.__entity.age import Age
from ECS.__entity.noncombatant import Noncombatant
from config.image_objects import BUNDLE_SAMWISE
from dialogue.get_dialogue import get_samwise_dialogue
from enums.render_order import RenderOrder


class DungeonAlphaMixin:
    """Mixin for DungeonAlphaBuilder, adds functionality unique to starting town"""

    def get_samwise(self):

        dialogue = get_samwise_dialogue()
        noncom = Noncombatant('samwise', BUNDLE_SAMWISE, dialogue)
        age = Age(13, 12, 28, 0, (1, 4))
        samwise = Entity(5, 16, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)
        return samwise
