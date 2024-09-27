from components.physics import Physics
from components.renderers import SpriteRenderer
from objects.rect import Rect

import pygame

class Obstaculo(Rect):
    def __init__(self, position, size):
        image = pygame.image.load('hidrante.png')
        image = pygame.transform.scale(image, size.as_tuple())
        super().__init__(position,height=size,width=size,name="obstaculo")
        self.components.add(Physics)
        self.components.add(SpriteRenderer,image)
        self.physics = self.components.get(Physics)
        self.physics.velocity.x = -5

