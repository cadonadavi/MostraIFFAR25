import pygame
import sys
import config

def executar():
    tela = config.tela
    clock = config.clock

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        tela.fill((50, 50, 50))
        pygame.display.flip()
        clock.tick(10)