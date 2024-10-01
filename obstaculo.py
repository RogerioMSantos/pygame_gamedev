import random
from components.physics import Physics
from components.renderers import SpriteRenderer
from core.game_math import Vector2d
from objects.rect import Rect

import pygame

class Obstaculo(Rect):
    SPEED = 500
    def __init__(self,screen, speed=SPEED):
        image,size = Obstaculo.get_random_image()
        image = pygame.image.load(image)
        
        position= Vector2d(screen.get_width(),screen.get_height() - size[1] + 10)

        super().__init__(position,height=size[1] * 0.8,width=size[0] * 0.9 ,name="obstaculo",draw_rect=False)
        
        image = pygame.transform.scale(image, size)

        self.components.add(SpriteRenderer,image)
        
        self.components.add(Physics, trigger_gravity=False)
        self.physics = self.components.get(Physics)
        self.physics.velocity.x = -speed
        self.physics.triger_gravity = False


    def update(self):
        super().update()


    @staticmethod
    def get_random_image() -> tuple:
        images = [('./assets/cone.png',(60,100)), ('./assets/caixa.png',(100,100)), ('./assets/hidrante.png',(60,100))]
        return random.choice(images)