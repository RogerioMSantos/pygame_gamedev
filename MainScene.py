import random
import time

import pygame
from bird import Bird
from colider import check_collision
from core.game_math import Vector2d
from core.scene import Scene
from moedas import Moeda
from objects.text import Text
from obstaculo import Obstaculo
from player import Player
from powerup import Power_up


class MainScene(Scene):
    def __init__(self, screen):

        image = pygame.image.load("./assets/background.png").convert()
        image = pygame.transform.scale(image,(screen.get_width(),screen.get_height()))
        super().__init__(screen,image=image)

        self.player = Player(position=Vector2d(20.0,screen.get_height()), height=80, width=120)
        self.objects.add(self.player)

        self.time_start = time.time()

        self.screen = screen

        obstacle = Obstaculo(self.screen)
        self.objects.add(obstacle)

        self.obstacle = [obstacle]

        self.create_score_board()

        self.game_speed = 500

        self.game_speed_text = Text(text="Game Speed: 500", font_size=35, color=(0, 0, 0), sys_font=True)

        self.game_speed_text.position = Vector2d(screen.get_width() - self.game_speed_text.image.get_width(),0)

        self.objects.add(self.game_speed_text)

        self.birds = []

    def create_score_board(self):
        self.score_board = {"pontuacao" :(Text(text="Pontuação: 0", font_size=35, color=(0, 0, 0), sys_font=True,position=Vector2d(10,10)),0),
                            "moedas" : (Text(text="Moedas: 0", font_size=35, color=(0, 0, 0), sys_font=True,position=Vector2d(10,50)),0),
                            "tempo" : (Text(text="Tempo: 0", font_size=35, color=(0, 0, 0), sys_font=True,position=Vector2d(10,90)),0),
                            "tempo_voo" : (Text(text="Tempo de voo: 0", font_size=35, color=(0, 0, 0), sys_font=True,position=Vector2d(10,130)),0)}
        
        for text in self.score_board.values():
            self.objects.add(text[0])

        self.score_board["tempo_voo"][0].active = False


    def update_score_board(self):
        self.score_board["pontuacao"][0].set_text(f"Pontuação: {self.player.coin_collected + time.time() - self.time_start:.0f}")
        self.score_board["tempo"][0].set_text(f"Tempo: {time.time() - self.time_start:.0f}s")
        self.score_board["tempo_voo"][0].set_text(f"Tempo de voo: {10 - (time.time() - self.player.start_fly):.0f}s")
        self.score_board["moedas"][0].set_text(f"Moedas: {self.player.coin_collected}")

        if(self.player.is_flying):
            self.score_board["tempo_voo"][0].active = True
        else:
            self.score_board["tempo_voo"][0].active = False

    def game_loop_step(self):
        super().game_loop_step()

        check_collision(self.objects)

        if len(self.birds) > 0 and self.birds[0].position.x < 0:
            self.objects.remove(self.birds[0])
            self.birds.pop(0)

        if self.obstacle[0].position.x < 0:
            self.objects.remove(Obstaculo)
            self.obstacle.pop(0)

            if(self.game_speed < 1000 and not self.player.is_flying):
                self.game_speed += 10

            self.game_speed_text.set_text(f"Game Speed: {self.game_speed}")

        if self.obstacle[-1].position.x < self.screen.get_width()/2:
            obstacle = Obstaculo(self.screen,self.game_speed)
            self.objects.add(obstacle)
            self.obstacle.append(obstacle)
            if self.player.is_flying:
                if(random.choices([False, True], weights=[50, 50], k=1)[0]):
                    self.objects.add(Bird(self.screen,speed=self.game_speed))
                    self.birds.append(Bird(self.screen,speed=self.game_speed))

                obstacle.active = False
                max_height = self.screen.get_height()
                if(random.choices([False, True], weights=[0, 80], k=1)[0]):
                    self.objects.add(Moeda(self.screen,speed=self.game_speed, max_height = max_height))
            else:
                obstacle.active = True
                if(random.choices([False, True], weights=[20, 80], k=1)[0]):
                    self.objects.add(Moeda(self.screen,speed=self.game_speed))
                elif(random.choices([False, True], weights=[50, 50], k=1)[0]):
                    self.objects.add(Power_up(self.screen,name="fly",speed=self.game_speed))

        self.update_score_board()

    def game_loop_fixed_step(self):
        super().game_loop_fixed_step()
        


