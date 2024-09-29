import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 1500

screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spritesheet Example")

# Carregar a imagem da sprite sheet
sprite_sheet = pygame.image.load("image.png").convert_alpha()

# Dimensões iniciais de cada sprite
sprite_width = 150
sprite_height = 100

# Offsets iniciais
offset_x = 116
offset_y = 388

# Lista para armazenar as sprites recortadas
sprites = []

# Função para recortar os sprites
def get_sprite(sheet, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite

# Função para recortar todas as sprites considerando os tamanhos e offsets
def recortar_sprites():
    global sprites
    sprites = []
    
    # Recortar os sprites da primeira linha (sprites uniformes)
    for i in range(8):  # Aqui você pode ajustar quantas sprites deseja recortar
        sprite = get_sprite(sprite_sheet, offset_x + i * sprite_width, offset_y, sprite_width, sprite_height)
        sprites.append(sprite)

# Recortar as sprites inicialmente
recortar_sprites()

# Posição inicial na tela
x_pos = 100
y_pos = 200

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((50, 50, 50))  # Cor de fundo da tela

    # Desenhar os sprites na tela
    for idx, sprite in enumerate(sprites):
        screen.blit(sprite, (x_pos + idx * sprite_width, y_pos))

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
