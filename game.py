import pygame
import random
from time import time
from MenuScene import MenuScene
from core.game import Game
from core.game_math import Vector2d
from core.scene import Scene
from player import Player
from obstaculo import Obstaculo
from background import Background
from MainScene import MainScene

pygame.init()
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Subway Surfers 2D")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

# Clock
clock = pygame.time.Clock()

# Carregar a imagem da caixa
caixa_img = pygame.image.load('caixa.png')
tamanho_caixa = (50, 50)  # Ajuste o tamanho conforme necessário
caixa_img = pygame.transform.scale(caixa_img, tamanho_caixa)


class PowerUp:
    def __init__(self):
        self.rect = pygame.Rect(LARGURA, random.randint(ALTURA - 150, ALTURA - 100), 30, 30)
        self.velocidade = 5

    def mover(self):
        self.rect.x -= self.velocidade

class Jogo:
    def __init__(self):
        self.player = Player(ALTURA, LARGURA)
        self.obstaculos = []
        self.moedas = []
        self.power_ups = []
        self.pontuacao = 0
        self.moedas_coletadas = 0
        self.tempo_inicio = time()
        self.fonte = pygame.font.Font(None, 35)
        self.fonte_titulo = pygame.font.Font("Gemstone.ttf", 60)

    def reiniciar(self):
        self.player = Player(ALTURA, LARGURA)
        self.obstaculos = []
        self.moedas = []
        self.power_ups = []
        self.pontuacao = 0
        self.moedas_coletadas = 0
        self.tempo_inicio = time()



    def gerar_obstaculos(self):
        if len(self.obstaculos) == 0 or self.obstaculos[-1].rect.right < LARGURA // 2:
            tipo_obstaculo = random.randint(1, 3)
            novo_obstaculo = Obstaculo(tipo_obstaculo, LARGURA, ALTURA)
            self.obstaculos.append(novo_obstaculo)

    #def gerar_moedas(self):
    #    if len(self.obstaculos) == 0 or self.obstaculos[-1].rect.right < LARGURA // 2:
   #         if random.random() < 0.5:
    #            self.moedas.append(Moeda())

    def gerar_power_ups(self):
        if random.random() < 0.005:
            self.power_ups.append(PowerUp())

    def verificar_colisoes(self):
        for obstaculo in self.obstaculos[:]:
            if self.player.rect.colliderect(obstaculo.rect):
                print(f"Fim de jogo! Pontuação: {self.pontuacao}")
                return False

        for moeda in self.moedas[:]:
            if self.player.rect.colliderect(moeda.rect):
                self.moedas.remove(moeda)
                self.pontuacao += 10
                self.moedas_coletadas += 1

        for power_up in self.power_ups[:]:
            if self.player.rect.colliderect(power_up.rect):
                self.power_ups.remove(power_up)
                self.player.voando = True
                self.player.time_flying = time()
                self.player.gravidade = 0
                self.player.pode_pular = False
                self.player.velocidade_vertical = 0
                self.inicio_voo = time()

        return True

    def atualizar_jogo(self):
        self.player.pular()
        self.player.atualizar_voo()

        for obstaculo in self.obstaculos:
            obstaculo.mover()

        for moeda in self.moedas:
            moeda.mover()

        for power_up in self.power_ups:
            power_up.mover()

    def desenhar(self, fundo):
        fundo.mover()
        fundo.desenhar(tela)
    
        pygame.draw.rect(tela, BRANCO, self.player.rect)

        for obstaculo in self.obstaculos:
            obstaculo.desenhar(tela)

        for moeda in self.moedas:
            pygame.draw.ellipse(tela, AMARELO, moeda.rect)

        for power_up in self.power_ups:
            pygame.draw.rect(tela, (0, 0, 255), power_up.rect)

        # Mostrar pontuação, moedas e tempo
        tempo_vivo = time() - self.tempo_inicio
        texto_pontuacao = self.fonte.render(f"Pontuação: {self.pontuacao}", True, BRANCO)
        texto_moedas = self.fonte.render(f"Moedas: {self.moedas_coletadas}", True, AMARELO)
        texto_tempo = self.fonte.render(f"Tempo: {tempo_vivo:.0f}s", True, BRANCO)
        if self.player.voando:
            tempo_de_voo = self.player.time_flying + 10 - time()
            texto_tempo_voo = self.fonte.render(f"Tempo de voo: {tempo_de_voo:.0f}s", True, BRANCO)
            tela.blit(texto_tempo_voo, (10, 130))
        tela.blit(texto_pontuacao, (10, 10))
        tela.blit(texto_moedas, (10, 50))
        tela.blit(texto_tempo, (10, 90))
        

        pygame.display.flip()


def main():
    Game.start(1000, 500)
    Game.set_scene(MenuScene(Game.screen))
    Game.run()


if __name__ == "__main__":
    main()
