from imagens import Imagens

class Obstaculo:
    def __init__(self, item, largura_total, altura_total):
        self.rect, self.imagem = Imagens(item, largura_total, altura_total)
        self.velocidade = 5

    def mover(self):
        self.rect.x -= self.velocidade

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)  # Renderizar a imagem na posição do obstáculo
