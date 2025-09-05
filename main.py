import pygame

# Iniciaalizando o pygame
pygame.init()

# Definindo o tamanho da tela
WIDTH,HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("goma sigma power")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

         # Atualização a tela

        pygame.display.flip()
