import time
from components.physics import Physics
from core.component import Component
from core.game_math import Vector2d
from core.game_object import GameObject
import pygame

class powerup_fly(Component):
    FLY_SPEED = 10

    def __init__(self, owner: GameObject, active=True, name=""):
        super().__init__(owner, active, name)
        self.owner = owner
        self.velocity = Vector2d()
        self.is_flying = False
        self.last_time_get = time.time()
        self.physics = owner.components.get(Physics)
        self.physics.trigger_gravity = False
        self.owner.can_jump = False

    def update(self):
        super().update()

        self.physics.velocity.y = 0
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.physics.velocity.y = -powerup_fly.FLY_SPEED
        
        if pygame.key.get_pressed()[pygame.K_CTRL]:
            self.physics.velocity.y = +powerup_fly.FLY_SPEED

    def fixed_update(self):
        if(time.time() - self.last_time_get >= 10.0):
            self.owner.can_jump = True
            self.owner.trigger_gravity = True
            self.owner.components.remove(self)