
import sys

import pygame

from core.manager import Manager
from core.game_time import Time
from core.events import Events


class Scene:
    def __init__(self, screen, bg_color=(255, 255, 255), image=None):
        self.objects = Manager()
        self._screen = screen
        self._bg_color = bg_color
        self._image = image

    def _physics_step(self):
        while Time.has_physics_time():
            self.objects.fixed_update()
            self.game_loop_fixed_step()
            Time.fixed_update()

    def _handle_exit_events(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE] or \
           Events.get(lambda e: e.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    def game_loop_step(self):
        Events.update()
        self._handle_exit_events()
        Time.update()
        self._physics_step()
        self.objects.update()
        self._screen.fill(self._bg_color)
        if self._image:
            self._screen.blit(self._image, (0, 0))
        self.objects.draw(self._screen)
        pygame.display.flip()
        Time.wait_fps()

    def game_loop_fixed_step(self):
        pass
