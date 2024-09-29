import pygame
from core.game_math import Vector2d

class Background:
    def __init__(self, image_path, screen, speed=1):
        self.image = pygame.image.load(image_path).convert()
        self.screen = screen
        self.speed = speed
        self.position = Vector2d(0, 0)

    def update(self):
        self.position.x -= self.speed

        if self.position.x <= -self.image.get_width():
            self.position.x = 0

    def draw(self):
        
        self.screen.blit(self.image, (self.position.x, self.position.y))

        self.screen.blit(self.image, (self.position.x + self.image.get_width(), self.position.y))

