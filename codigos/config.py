import pygame

pygame.init()

# Tela global
info = pygame.display.Info()
largura = info.current_w
altura = info.current_h
tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption("The Campus Tales")

# Ícone
icone = pygame.image.load(r"imagens/icone.png")
pygame.display.set_icon(icone)

# Relógio global
clock = pygame.time.Clock()