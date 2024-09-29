
import pygame

from core.game_object import GameObject
from core.component import Component


class CircleRenderer(Component):
    def __init__(self, owner: GameObject, radius: int = 5, color=(128, 128, 128), active=True, name=""):
        super().__init__(owner, active, name)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        draw_position = (self.object.position.x + self.radius, self.object.position.y + self.radius)
        pygame.draw.circle(screen, self.color, draw_position, self.radius)


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

class SpriteSheetRenderer(Component):
    def __init__(self, owner: GameObject, active=True, name="",time_per_sprite=0.09):
        super().__init__(owner, active, name)
        self.sprite_dict = {}
        self.actual_sprite_name = None
        self.actual_sprite = 0
        self.time_per_sprite = time_per_sprite
        self.last_update = 0
        self.owner = owner


    def load_sprites(self,image ,sprite_width=10, sprite_height=10, offset_x=0, offset_y=0, sprite_name="",quantity_line=None,quantity_column=None):
        self.sprite_dict[sprite_name] = []
        if quantity_line is None:
            quantity_line = image.get_width() / sprite_width
        if quantity_column is None:
            quantity_column = image.get_height() / sprite_height
        for i in range(0, quantity_column):
            for j in range(0, quantity_line):
                sprite = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
                sprite.blit(image, (0, 0), (offset_x + i*sprite_width, offset_y + j*sprite_height, sprite_width, sprite_height))
                self.sprite_dict[sprite_name].append(sprite)


    def draw(self, screen):
        if self.actual_sprite_name is not None:
            sprite = self.sprite_dict[self.actual_sprite_name][self.actual_sprite]
            sprite = pygame.transform.scale(sprite, (self.owner.width, self.owner.height))
            screen.blit(sprite, (self.object.position.x, self.object.position.y))

    def fixed_update(self):
        super().fixed_update()
        if self.actual_sprite_name is not None:
            if pygame.time.get_ticks() - self.last_update > self.time_per_sprite * 1000:
                self.actual_sprite += 1
                if self.actual_sprite >= len(self.sprite_dict[self.actual_sprite_name]):
                    self.actual_sprite = 0
                self.last_update = pygame.time.get_ticks()

