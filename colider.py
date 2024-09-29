import pygame

from core.game import Game
from item import Item
from objects.rect import Rect
from obstaculo import Obstaculo
from player import Player
from sceneManager import set_menu_scene


def check_collision(objects):
    for obj in objects._objects:
        if isinstance(obj,Player):
            for obj2 in objects._objects:
                if not isinstance(obj2,Rect):
                    continue
                if obj != obj2:
                    if pygame.Rect.colliderect(obj.as_rect(),obj2.as_rect()) and obj2.active:
                        if isinstance(obj2,Item):
                            obj2.collect(obj)
                            objects._objects.remove(obj2)
                            continue
                        if isinstance(obj2,Obstaculo):
                            #obj2.collide(obj)
                            set_menu_scene()

