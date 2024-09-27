from components.physics import Physics
from core.game import Game
import pygame
from time import time
from objects.rect import Rect

class Player(Rect):
    JUMP_SPEED = 10
    def __init__(self,position,size):
        super().__init__(position,height=size,width=size,name="player")
        self.components.add(Physics)
        self.physics = self.components.get(Physics)
        
        self.jumping = False
        self.size = size
        self.can_jump = True

    def update(self):
        super().update()

        if not self.jumping and self.can_jump and pygame.key.get_pressed()[pygame.K_SPACE]:
            self.physics.velocity.y = -Player.JUMP_SPEED
            self.jumping = True
        
        if self.position.y + self.height >= Game.screen.get_height():
            self.position.y = Game.screen.get_height() - self.height
            self.jumping = False

