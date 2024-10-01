
import pygame

from core.scene import Scene

class Game:
    screen = None
    scene = None

    @staticmethod
    def start(screen_width: int, screen_height: int):
        pygame.init()
        Game.screen = pygame.display.set_mode((screen_width, screen_height))

    @staticmethod
    def set_scene(scene: Scene):
        Game.scene = scene

    @staticmethod
    def run():
        while True:
            Game.scene.game_loop_step()
