import random

from components.physics import Physics
from components.renderers import CircleRenderer
from core.game_math import Vector2d
from objects.rect import Rect


class Item(Rect):
    SPEED = 500


    def __init__(self,screen,radius: int = 20, color = (255, 255, 0), min_height: int = 130, max_height: int = 160, name: str = "", speed: int = SPEED):
        height = screen.get_height() - random.uniform(min_height,max_height)
        position = Vector2d(screen.get_width() + 10, height)
        super().__init__(position=position,width=radius*2,height=radius*2,name=name,draw_rect=False)

        self.components.add(Physics,trigger_gravity=False)
        
        self.components.add(CircleRenderer,radius=radius,color=color)

        self.physics = self.components.get(Physics)
        self.physics.velocity.x = -speed
        self.physics.triger_gravity = False


    def collect(self,player):
        """ update function called once per player colision trigger """

