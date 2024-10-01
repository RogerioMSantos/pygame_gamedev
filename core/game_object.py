

from typing import Optional
from core.base import BaseObject
from core.component_manager import ComponentManager
from core.game_math import Vector2d


class GameObject(BaseObject):
    def __init__(self, position: Optional[Vector2d] = None, active=True, name=""):
        super().__init__(active, name)
        self.components = ComponentManager(self)

        if position is not None:
            self.position = position
        else:
            self.position = Vector2d()

    def update(self):
        self.components.update()

    def fixed_update(self):
        self.components.fixed_update()

    def draw(self, screen):
        self.components.draw(screen)
