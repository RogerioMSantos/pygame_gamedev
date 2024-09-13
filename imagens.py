import pygame

def Imagens(tamanho: int, largura_total = 640, altura_total = 480):
    if(tamanho == 1):
        caixa_img = pygame.image.load('caixa.png')
        tamanho_caixa = (50, 50)
        caixa_img = pygame.transform.scale(caixa_img, tamanho_caixa)
        rect = pygame.Rect(largura_total, altura_total - 40, tamanho_caixa[0], tamanho_caixa[1])
        return rect, caixa_img
    
    elif(tamanho == 2):
        tamanho_imagem = (30, 50)
        imagem = pygame.image.load('hidrante.png')
        imagem = pygame.transform.scale(imagem, tamanho_imagem)
        rect = pygame.Rect(largura_total, altura_total - 40, tamanho_imagem[0], tamanho_imagem[1])
        return rect, imagem
    
    else:
        tamanho_imagem = (30, 50)
        imagem = pygame.image.load('cone.png')
        imagem = pygame.transform.scale(imagem, tamanho_imagem)
        rect = pygame.Rect(largura_total, altura_total - 40, tamanho_imagem[0], tamanho_imagem[1])

        return rect, imagem
