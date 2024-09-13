import pygame
from time import time

class Jogador:
    def __init__(self, altura, largura):
        self.rect = pygame.Rect(50, altura - 60, 40, 60)
        self.velocidade = 5
        self.pulando = False
        self.velocidade_vertical = 0
        self.gravidade = 0.8
        self.voando = False
        self.tempo_voo = 0
        self.largura = largura
        self.altura = altura
        self.pode_pular = True
        
    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < self.largura:
            self.rect.x += self.velocidade

    def pular(self):
        if self.pulando and self.velocidade_vertical == 0 and self.pode_pular:
            self.velocidade_vertical = -13

        self.rect.y += self.velocidade_vertical
        self.velocidade_vertical += self.gravidade

        if self.rect.bottom >= self.altura:
            self.rect.bottom = self.altura
            self.pulando = False
            self.velocidade_vertical = 0

    def aplicar_voo(self, teclas):
        if self.voando:
            if teclas[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.velocidade
            if teclas[pygame.K_DOWN] and self.rect.bottom < self.altura:
                self.rect.y += self.velocidade

    def atualizar_voo(self):
        if self.voando and time() - self.tempo_voo > 10:  # 10 segundos de voo
            self.voando = False
            self.rect.bottom = self.altura
            self.gravidade = 0.8
            self.pode_pular = True

