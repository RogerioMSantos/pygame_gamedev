import time
from components.physics import Physics
from core.component import Component
from core.game_math import Vector2d
from core.game_object import GameObject
import pygame

class Power_up_fly(Component):
    FLY_SPEED = 300

    def __init__(self, owner: GameObject, active=True, name=""):
        super().__init__(owner, active, name)
        self.owner = owner
        self.velocity = Vector2d()
        self.is_flying = False
        self.owner.start_fly = time.time()
        self.physics = owner.components.get(Physics)
        self.physics.trigger_gravity = False
        self.owner.is_flying = True
        self.owner.renderer.actual_sprite_name = "flying"
        self.owner.renderer.actual_sprite = 0


    def update(self):
        super().update()

        self.physics.velocity.y = 0
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.physics.velocity.y = -Power_up_fly.FLY_SPEED
        
        if pygame.key.get_pressed()[pygame.K_LCTRL]:
            self.physics.velocity.y = +Power_up_fly.FLY_SPEED

    def fixed_update(self):
        if(time.time() - self.owner.start_fly >= 10.0):
            self.owner.is_flying = False
            self.physics.trigger_gravity = True
            self.owner.components.remove(self)
            self.owner.renderer.actual_sprite_name = "running"