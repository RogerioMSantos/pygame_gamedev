import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 2000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spritesheet Example")

# Carregar a imagem da sprite sheet
sprite_sheet = pygame.image.load("./assets/bird.png").convert_alpha()

# Dimensões iniciais de cada sprite
sprite_width = 128
sprite_height = 128

# Velocidade de aumento/diminuição do tamanho
size_change_speed = 1

# Lista para armazenar as sprites recortadas
sprites = []

# Offsets iniciais
offset_x = 0
offset_y = 0

# Fonte para exibir o tamanho do corte e a distância entre sprites
font = pygame.font.SysFont(None, 36)

# Nova variável para o offset entre sprites
offset_x_per_frame = 0
offset_y_per_frame = 0
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
    for i in range(6):
        sprite = get_sprite(sprite_sheet, offset_x + 0 * sprite_width+ (offset_x_per_frame * i), offset_y + sprite_height * i + (offset_y_per_frame * i), sprite_width, sprite_height)
        sprites.append(sprite)

# Recortar as sprites inicialmente
recortar_sprites()

# Posição inicial e movimento
x_pos = 100
y_pos = 200
screen_offset = 0  # Para mover a tela lateralmente

# Distância entre as sprites
sprite_spacing = 150
spacing_change_speed = 5

# Controle de incremento contínuo ao manter a tecla pressionada
increase_width = False
decrease_width = False
increase_height = False
decrease_height = False
increase_spacing = False
decrease_spacing = False
move_right = False
move_left = False

# Controle dos offsets
increase_offset_x = False
decrease_offset_x = False
increase_offset_y = False
decrease_offset_y = False

# Controle do offset entre sprites
increase_offset_x_per_frame = False
decrease_offset_x_per_frame = False
increase_offset_y_per_frame = False
decrease_offset_y_per_frame = False


# Função para desenhar o tamanho do corte e a distância entre as sprites na tela
def draw_text(text, x, y):
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((50, 50, 50))  # Cor de fundo da tela

    # Desenhar os sprites na tela e adicionar o quadrado vermelho ao redor de cada sprite
    for idx, sprite in enumerate(sprites):
        sprite_x_pos = x_pos + screen_offset + (idx * (sprite_spacing + sprite.get_width()))
        
        # Desenhar o sprite na tela
        screen.blit(sprite, (sprite_x_pos, y_pos))

        # Desenhar o quadrado vermelho ao redor da área de cada sprite
        pygame.draw.rect(screen, (255, 0, 0), (sprite_x_pos, y_pos, sprite.get_width(), sprite.get_height()), 2)

    # Mostrar o tamanho atual dos cortes, offsets e a distância entre sprites
    draw_text(f"Width: {sprite_width}, Height: {sprite_height}", 10, 10)
    draw_text(f"Offset X: {offset_x}, Offset Y: {offset_y}", 10, 50)
    draw_text(f"Spacing: {sprite_spacing}", 10, 90)
    draw_text(f"Offset X per Frame: {offset_x_per_frame}", 10, 130)  # Exibir o valor do offset_x_per_frame
    draw_text(f"Offset Y per Frame: {offset_y_per_frame}", 10, 170)  # Exibir o valor do offset_y_per_frame

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Aumentar/Diminuir largura com setas esquerda e direita
            if event.key == pygame.K_LEFT:
                decrease_width = True
            elif event.key == pygame.K_RIGHT:
                increase_width = True
            
            # Aumentar/Diminuir altura com [ e ]
            elif event.key == pygame.K_LEFTBRACKET:  # [
                decrease_height = True
            elif event.key == pygame.K_RIGHTBRACKET:  # ]
                increase_height = True
            
            # Aumentar/Diminuir espaçamento
            elif event.key == pygame.K_SPACE:
                increase_spacing = True
            elif event.key == pygame.K_LCTRL:
                decrease_spacing = True

            # Aumentar/Diminuir offset X com C e V
            elif event.key == pygame.K_c:
                decrease_offset_x = True
            elif event.key == pygame.K_v:
                increase_offset_x = True
            
            # Aumentar/Diminuir offset Y com D e F
            elif event.key == pygame.K_d:
                decrease_offset_y = True
            elif event.key == pygame.K_f:
                increase_offset_y = True

            # Aumentar/Diminuir offset entre sprites com A e S
            elif event.key == pygame.K_a:
                decrease_offset_x_per_frame = True
            elif event.key == pygame.K_s:
                increase_offset_x_per_frame = True

            elif event.key == pygame.K_z:
                decrease_offset_y_per_frame = True
            elif event.key == pygame.K_x:
                increase_offset_y_per_frame = True

            # Mover a tela para a esquerda ou direita
            elif event.key == pygame.K_a:  # Mover para a esquerda
                screen_offset -= 5
            elif event.key == pygame.K_d:  # Mover para a direita
                screen_offset += 5

        elif event.type == pygame.KEYUP:
            # Parar controle de largura
            if event.key == pygame.K_LEFT:
                decrease_width = False
            elif event.key == pygame.K_RIGHT:
                increase_width = False

            # Parar controle de altura
            elif event.key == pygame.K_LEFTBRACKET:
                decrease_height = False
            elif event.key == pygame.K_RIGHTBRACKET:
                increase_height = False

            # Parar controle de espaçamento
            elif event.key == pygame.K_SPACE:
                increase_spacing = False
            elif event.key == pygame.K_LCTRL:
                decrease_spacing = False

            # Parar controle de offset X
            elif event.key == pygame.K_c:
                decrease_offset_x = False
            elif event.key == pygame.K_v:
                increase_offset_x = False

            # Parar controle de offset Y
            elif event.key == pygame.K_d:
                decrease_offset_y = False
            elif event.key == pygame.K_f:
                increase_offset_y = False

            # Parar controle do offset entre sprites
            elif event.key == pygame.K_a:
                decrease_offset_x_per_frame = False
            elif event.key == pygame.K_s:
                increase_offset_x_per_frame = False

            elif event.key == pygame.K_z:
                decrease_offset_y_per_frame = False
            elif event.key == pygame.K_x:
                increase_offset_y_per_frame = False

    # Atualizar o tamanho das sprites ao manter a tecla pressionada
    if increase_width:
        sprite_width += size_change_speed
        recortar_sprites()  # Atualizar o recorte com os novos tamanhos
    if decrease_width:
        sprite_width = max(10, sprite_width - size_change_speed)
        recortar_sprites()  # Atualizar o recorte com os novos tamanhos

    if increase_height:
        sprite_height += size_change_speed
        recortar_sprites()  # Atualizar o recorte com os novos tamanhos
    if decrease_height:
        sprite_height = max(10, sprite_height - size_change_speed)
        recortar_sprites()  # Atualizar o recorte com os novos tamanhos

    # Atualizar a distância entre as sprites
    if increase_spacing:
        sprite_spacing += spacing_change_speed
    if decrease_spacing:
        sprite_spacing = max(0, sprite_spacing - spacing_change_speed)

    # Atualizar os offsets ao manter a tecla pressionada
    if increase_offset_x:
        offset_x += size_change_speed
        recortar_sprites()
    if decrease_offset_x:
        offset_x = max(0, offset_x - size_change_speed)
        recortar_sprites()

    if increase_offset_y:
        offset_y += size_change_speed
        recortar_sprites()
    if decrease_offset_y:
        offset_y = max(0, offset_y - size_change_speed)
        recortar_sprites()

    # Atualizar o offset entre sprites
    if increase_offset_x_per_frame:
        offset_x_per_frame += spacing_change_speed
        recortar_sprites()
    if decrease_offset_x_per_frame:
        offset_x_per_frame = max(0, offset_x_per_frame - spacing_change_speed)
        recortar_sprites()
    
    if increase_offset_y_per_frame:
        offset_y_per_frame += spacing_change_speed
        recortar_sprites()
    if decrease_offset_y_per_frame:
        offset_y_per_frame = max(0, offset_y_per_frame - spacing_change_speed)
        recortar_sprites()

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
