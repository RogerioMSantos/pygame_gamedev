
from typing import Optional

import pygame

from core.game_object import GameObject
from core.game_math import Vector2d
from components.renderers import SpriteRenderer


class Sprite(GameObject):
    def __init__(self,
                 image,
                 position: Optional[Vector2d] = None,
                 active=True,
                 name=""):
        super().__init__(active, name,position=position)
        self.components.add(SpriteRenderer(self, image))

    @staticmethod
    def load(path: str, width: int = 0, height: int = 0):
        image = pygame.image.load(path)

        if (height > 0) and (width > 0):
            image = pygame.transform.scale(image, (width, height))

        image = image.convert_alpha()
        return image
