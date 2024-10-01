import pygame
from components.renderers import SpriteRenderer
from item import Item
from objects.circle import Circle
from powerup_fly import Power_up_fly


class Power_up(Item):
    def __init__(self,screen ,name="", **kwargs) -> None:
        super().__init__(screen, name=name, color=(0,0,255), draw_hitbox=False,**kwargs)
        image = pygame.image.load("./assets/bife.png")
        image = pygame.transform.scale(image,(self.width,self.height))
        self.components.add(SpriteRenderer,image=image)

    def collect(self, player):
        player.components.remove(Power_up_fly)
        player.components.add(Power_up_fly)


