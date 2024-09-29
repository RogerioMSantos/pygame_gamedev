
from typing import Optional, Tuple

import pygame

from core.game_math import Vector2d
from core.game_object import GameObject
from components.renderers import SpriteRenderer


class Text(GameObject):
    def __init__(self,
                 text: str = "",
                 font: str = None,
                 sys_font: bool = False,
                 font_size: int = 12,
                 position: Optional[Vector2d] = None,
                 color: Tuple[int, int, int] = (128, 128, 128),
                 active=True,
                 name=""):
        super().__init__(position, active, name)
        if sys_font:
            self._text_renderer = pygame.font.SysFont(font, font_size)
        else:
            self._text_renderer = pygame.font.Font(font, font_size)
        self._color = color
        self.image = self._text_renderer.render(text, True, color)
        self.components.add(SpriteRenderer, self.image)

    def set_text(self, text: str):
        self.image = self._text_renderer.render(text, True, self._color)
        self.components.get(SpriteRenderer).image = self.image

