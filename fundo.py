import pygame

class Fundo:
    def __init__(self, imagem, largura, altura):
        self.imagem = pygame.transform.scale(imagem, (largura, altura))  # Redimensiona a imagem para cobrir a tela
        self.largura = largura
        self.altura = altura
        self.x1 = 0  # Primeira imagem começa no início da tela
        self.x2 = largura  # Segunda imagem começa imediatamente após a primeira
        self.velocidade = 5  # Velocidade de deslocamento do plano de fundo

    def mover(self):
        # Mover as duas imagens para a esquerda
        self.x1 -= self.velocidade
        self.x2 -= self.velocidade

        # Quando a primeira imagem sair completamente da tela, reposicioná-la
        if self.x1 <= -self.largura:
            self.x1 = self.x2 + self.largura

        # Quando a segunda imagem sair completamente da tela, reposicioná-la
        if self.x2 <= -self.largura:
            self.x2 = self.x1 + self.largura

    def desenhar(self, tela):
        # Desenha as duas imagens
        tela.blit(self.imagem, (self.x1, 0))
        tela.blit(self.imagem, (self.x2, 0))
