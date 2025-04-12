import pygame
import sys
import os
import config
import jogo
import creditos

def mostrar_menu():
    tela = config.tela
    clock = config.clock

    # Fundo animado
    frames = []
    caminho_frames = "imagens/gifceu"
    for nome_arquivo in sorted(os.listdir(caminho_frames)):
        if nome_arquivo.endswith(".png") or nome_arquivo.endswith(".jpg"):
            frame = pygame.image.load(os.path.join(caminho_frames, nome_arquivo))
            frame = pygame.transform.scale(frame, tela.get_size())
            frames.append(frame)

    # Logo
    logo = pygame.transform.scale(pygame.image.load("imagens/logo.png"), (640, 322))

    # Botões
    def carregar_botao(normal_path, selecionado_path):
        normal = pygame.image.load(normal_path)
        selecionado = pygame.image.load(selecionado_path)
        return pygame.transform.scale(normal, (240, 60)), pygame.transform.scale(selecionado, (360, 90))

    botao_start, botao_start_sel = carregar_botao("imagens/start.png", "imagens/start_selected.png")
    botao_cred, botao_cred_sel = carregar_botao("imagens/creditos.png", "imagens/creditos_selected.png")
    botao_sair, botao_sair_sel = carregar_botao("imagens/sair.png", "imagens/sair_selected.png")

    botoes = [
        {"normal": botao_start, "sel": botao_start_sel, "nome": "Start"},
        {"normal": botao_cred, "sel": botao_cred_sel, "nome": "Créditos"},
        {"normal": botao_sair, "sel": botao_sair_sel, "nome": "Sair"}
    ]

    indice = 0
    frame_index = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    indice = (indice - 1) % len(botoes)
                elif evento.key == pygame.K_s:
                    indice = (indice + 1) % len(botoes)
                elif evento.key == pygame.K_RETURN:
                    if botoes[indice]["nome"] == "Start":
                        jogo.executar()
                    elif botoes[indice]["nome"] == "Créditos":
                        creditos.executar_creditos()
                    elif botoes[indice]["nome"] == "Sair":
                        pygame.quit()
                        sys.exit()

        tela.blit(frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(frames)

        tela.blit(logo, (80, 135))

        y_base = 480
        for i, botao in enumerate(botoes):
            img = botao["sel"] if i == indice else botao["normal"]
            tela.blit(img, (112, y_base))
            y_base += img.get_height() + 20

        pygame.display.flip()
        clock.tick(10)
    
if __name__ == "__main__":
    mostrar_menu()