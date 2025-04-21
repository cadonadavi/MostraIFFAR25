import pygame
import sys
import config
import os
import start_menu

def executar_creditos():
    tela = config.tela

    # Transição
    frames_menu = []
    caminho_frames = "imagens/gifceu/transicao"
    for nome_arquivo in sorted(os.listdir(caminho_frames)):
        if nome_arquivo.endswith(".png") or nome_arquivo.endswith(".jpg"):
            frame = pygame.image.load(os.path.join(caminho_frames, nome_arquivo))
            frame = pygame.transform.scale(frame, tela.get_size())
            frames_menu.append(frame)

    for frame in frames_menu:
        tela.blit(frame, (0, 0))
        pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    start_menu.mostrar_menu()

        # menu mesmo
        tela.fill((116, 186, 245))

        voltar = pygame.image.load("imagens/botoes/voltar_selected.png")
        botao_voltar = pygame.transform.scale(voltar, (360, 90))
        x_central = (tela.get_width() - botao_voltar.get_width()) // 2
        tela.blit(botao_voltar, (x_central, 760))

        pygame.display.flip()