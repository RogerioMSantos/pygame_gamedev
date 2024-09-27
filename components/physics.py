
from core.component import Component
from core.game_math import Vector2d
from core.game_object import GameObject
from core.game_time import Time



class Physics(Component):
    def __init__(self, owner: GameObject, active=True, name=""):
        super().__init__(owner, active, name)
        self.velocity = Vector2d()
        self.gravity = 0.8
        self.trigger_gravity = True

    def fixed_update(self):
        self.object.position += self.velocity * Time.fixed_delta_time
        if(self.velocidade.y > 0 and self.trigger_gravity):
            self.velocidade.y -= self.gravity
        
