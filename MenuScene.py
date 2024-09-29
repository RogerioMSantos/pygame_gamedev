import pygame
from MainScene import MainScene
from core.game import Game
from core.scene import Scene
from objects.circle import Circle
from objects.rect import Rect
from objects.text import Text
from core.game_math import Vector2d
#from background import Background
from player import Player
from sceneManager import set_main_scene

class MenuScene(Scene):
    def __init__(self, screen):
        image = pygame.image.load("background.png").convert()
        image = pygame.transform.scale(image,(screen.get_width(),screen.get_height()))
        super().__init__(screen,image=image)
        self.screen = screen
        text = Text(text="Subway Surfers 2D", font="Gemstone.ttf", font_size=30, color=(0,0,0), sys_font=False)
        text.position = Vector2d(screen.get_width() / 2 - text.image.get_width() / 2, screen.get_height() / 2 - text.image.get_height() / 2)
        #self.fundo = Background("background.png", screen, speed=2)
        self.objects.add(Player(Vector2d(screen.get_width() / 2 - 130 / 2, screen.get_height() / 2 - 80 / 2),130,80))

        self.objects.add(text)

    def game_loop_step(self):
        super().game_loop_step()
        
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            set_main_scene()
