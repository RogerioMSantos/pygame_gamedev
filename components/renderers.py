
import pygame

from core.game_object import GameObject
from core.component import Component


class CircleRenderer(Component):
    def __init__(self, owner: GameObject, radius: int = 5, color=(128, 128, 128), active=True, name=""):
        super().__init__(owner, active, name)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.object.position.as_tuple(), self.radius)


class RectangleRenderer(Component):
    def __init__(self, owner: GameObject, height: int = 10, width: int = 10, color=(128, 128, 128), active=True, name=""):
        super().__init__(owner, active, name)
        self.height = height
        self.width = width
        self.color = color

    def draw(self, screen):
        rect = (self.object.position.x, self.object.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)


class SpriteRenderer(Component):
    def __init__(self, owner: GameObject, image, active=True, name=""):
        super().__init__(owner, active, name)
        self.image = image

    def draw(self, screen):
        rect = (self.object.position.x, self.object.position.y, self.image.get_width(), self.image.get_height())
        screen.blit(self.image, rect)


