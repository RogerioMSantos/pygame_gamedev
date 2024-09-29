
from core.component import Component
from core.game_math import Vector2d
from core.game_object import GameObject
from core.game_time import Time



class Physics(Component):
    def __init__(self, owner: GameObject, active=True, name="", trigger_gravity=True, acceleration=Vector2d(0,0), max_velocity=1000, gravity=10):
        super().__init__(owner, active, name)
        self.velocity = Vector2d()
        self.gravity = gravity
        self.trigger_gravity = trigger_gravity
        self.acceleration = acceleration
        
    def fixed_update(self):
        self.object.position += self.velocity * Time.fixed_delta_time
        
        self.velocity.x += self.acceleration.x * Time.fixed_delta_time
        self.velocity.y += self.acceleration.y * Time.fixed_delta_time

        if(self.trigger_gravity):
            self.velocity.y += self.gravity
            if(self.velocity.y > self.max_velocity):
                self.velocity.y = self.max_velocity
