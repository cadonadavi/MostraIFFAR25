import pygame

pygame.init()
pygame.font.init()

# Tela global
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("The Campus Tales")

# Ícone
icone = pygame.image.load(r"imagens/icone.png")
pygame.display.set_icon(icone)

# Relógio global
clock = pygame.time.Clock()