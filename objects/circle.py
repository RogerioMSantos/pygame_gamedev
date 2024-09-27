
from typing import Optional
from core.game_object import GameObject
from core.game_math import Vector2d
from components.renderers import CircleRenderer


class Circle(GameObject):
    def __init__(self, position: Optional[Vector2d] = None, radius: float = 10, active=True, name=""):
        super().__init__(position, active, name)
        self._radius = radius
        self.components.add(CircleRenderer, radius=radius)
