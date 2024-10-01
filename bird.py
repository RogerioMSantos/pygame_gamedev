import random
import pygame
from components.physics import Physics
from components.renderers import SpriteSheetRenderer
from core.game_math import Vector2d
from objects.rect import Rect


class Bird(Rect):
    def __init__(self, screen,speed=100):
        position = Vector2d(screen.get_width(), random.randint(50,screen.get_height() - 50))
        width=50
        height=50
        super().__init__(position, width, height,name="bird",draw_rect=False)
        self.components.add(SpriteSheetRenderer)
        self.sprite_renderer = self.components.get(SpriteSheetRenderer)
        image = pygame.image.load("./assets/bird.png")
        image = pygame.transform.flip(image,True,False)
        self.sprite_renderer.load_sprites(image=image, sprite_width=105, sprite_height=80, offset_x=30, offset_y=28, offset_x_per_frame=54, offset_y_per_frame=42, sprite_name="bird",quantity_line=4,quantity_column=5)
        self.sprite_renderer.actual_sprite_name = "bird"
        self.components.add(Physics,trigger_gravity=False)
        self.physics = self.components.get(Physics)
        self.physics.velocity.x = -speed

