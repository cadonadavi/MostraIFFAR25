import pygame
import sys
import config

def executar_creditos():
    tela = config.tela
    clock = config.clock

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return

        tela.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(10)
