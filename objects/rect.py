
from typing import Optional

import pygame

from core.game_object import GameObject
from core.game_math import Vector2d
from components.renderers import RectangleRenderer


class Rect(GameObject):
    def __init__(self, position: Optional[Vector2d] = None,
                 height: float = 10,
                 width: float = 10,
                 color=(128, 128, 128),
                 active=True,
                 name=""):
        super().__init__(position, active, name)
        self.height = height
        self.width = width
        self.components.add(RectangleRenderer, height=height, width=width, color=color)

    def as_tuple(self):
        return (self.position.x,
                self.position.y,
                self.width,
                self.height)

    def as_rect(self):
        return pygame.Rect(self.position.x,
                           self.position.y,
                           self.width,
                           self.height)
