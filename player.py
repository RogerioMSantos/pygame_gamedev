import time
from components.physics import Physics
from components.renderers import SpriteSheetRenderer
from core.game import Game
import pygame
from objects.rect import Rect

class Player(Rect):
    JUMP_SPEED = 750
    def __init__(self,position,height,width):
        super().__init__(position,height=height,width=width-20,name="player",draw_rect=False)
        self.create_sprites()
        self.components.add(Physics)
        self.physics = self.components.get(Physics)
        self.jumping = False
        self.is_flying = False
        self.start_fly = 0
        self.coin_collected = 0
        self.height = height
        self.width = width


    def update(self):
        super().update()

        if not self.jumping and not self.is_flying and pygame.key.get_pressed()[pygame.K_SPACE]:
            self.physics.velocity.y = -Player.JUMP_SPEED
            print("pulo")
            self.renderer.actual_sprite_name = "jumping"
            self.renderer.actual_sprite = 0
            self.jumping = True
        if self.jumping and pygame.key.get_pressed()[pygame.K_LCTRL]:
            self.physics.velocity.y += 100
        
        if self.position.y + self.height >= Game.screen.get_height():
            self.position.y = Game.screen.get_height() - self.height
            if self.jumping:
                self.renderer.actual_sprite_name = "running"
                self.renderer.actual_sprite = 0
            self.jumping = False

    def create_sprites(self):
        #cria o sprite correndo 
        self.components.add(SpriteSheetRenderer)
        self.renderer = self.components.get(SpriteSheetRenderer)

        self.renderer.actual_sprite_name = "running"
        self.renderer.load_sprites(image=pygame.image.load("image.png"),sprite_width=130, sprite_height=80, offset_x=55 + 130 * 4, offset_y=50, sprite_name="running",quantity_line=1,quantity_column=6)

        #cria o sprite pulando
        self.renderer.load_sprites(image=pygame.image.load("image.png"),sprite_width=145, sprite_height=100, offset_x=116, offset_y=388, sprite_name="jumping",quantity_line=1,quantity_column=8)

        #cria o sprite voando
        self.renderer.load_sprites(image=pygame.image.load("image.png"),sprite_width=247, sprite_height=128, offset_x=65, offset_y=156, sprite_name="flying",quantity_line=1,quantity_column=3)

