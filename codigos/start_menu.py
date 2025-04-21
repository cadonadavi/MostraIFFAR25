import pygame
import sys
import os
import config
import creditos
from pathlib import Path

def criar_save():
    save_path = Path("save.txt")
    with open(save_path, "w") as f:
        f.write("save iniciado\n")

def charcater_select_menu(tela):
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
                if evento.key == pygame.K_ESCAPE:
                    return

        # menu mesmo
        tela.fill((116, 186, 245))

        pygame.display.flip()

def mostrar_menu():
    tela = config.tela
    clock = config.clock

    # Fundo animado
    frames = []
    caminho_frames = "imagens/gifceu/menu"
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

    botao_start, botao_start_sel = carregar_botao("imagens/botoes/start.png", "imagens/botoes/start_selected.png")
    botao_cred, botao_cred_sel = carregar_botao("imagens/botoes/creditos.png", "imagens/botoes/creditos_selected.png")
    botao_sair, botao_sair_sel = carregar_botao("imagens/botoes/sair.png", "imagens/botoes/sair_selected.png")
    botao_continue, botao_continue_sel = carregar_botao("imagens/botoes/continue.png", "imagens/botoes/continue_selected.png")

    botoes_menu = [
        {"normal": botao_start, "sel": botao_start_sel, "nome": "Start"},
        {"normal": botao_cred, "sel": botao_cred_sel, "nome": "Créditos"},
        {"normal": botao_sair, "sel": botao_sair_sel, "nome": "Sair"}
    ]

    botoes_saving = [
        {"normal": botao_start, "sel": botao_start_sel, "nome": "Start"},
        {"normal": botao_continue, "sel": botao_continue_sel, "nome": "Continuar"},
        {"normal": botao_cred, "sel": botao_cred_sel, "nome": "Créditos"},
        {"normal": botao_sair, "sel": botao_sair_sel, "nome": "Sair"}
    ]

    indicevertical = 0
    frame_index = 0
    save = Path("save.txt")

    if save.exists():
        estado_menu = "continuar"
    else:
        estado_menu = "menu"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w or evento.key == pygame.K_UP:
                    indicevertical = (indicevertical - 1) % (len(botoes_menu) if estado_menu == "menu" else len(botoes_saving))

                elif evento.key == pygame.K_s or evento.key == pygame.K_DOWN:
                    indicevertical = (indicevertical + 1) % (len(botoes_menu) if estado_menu == "menu" else len(botoes_saving))

                elif evento.key == pygame.K_RETURN:
                    if botoes_menu[indicevertical]["nome"] == "Start":
                        if estado_menu == "menu":
                            charcater_select_menu(tela)
                            return "jogo"
                        else:
                            return "jogo"

                    elif botoes_menu[indicevertical]["nome"] == "Créditos":
                        creditos.executar_creditos()
                        return "creditos"

                    elif botoes_menu[indicevertical]["nome"] == "Sair":
                        pygame.quit()
                        sys.exit()

                    elif botoes_saving[indicevertical]["nome"] == "Continuar":
                        return "jogo"                                         

        # Desenho da tela
        tela.blit(frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(frames)

        logo_rect = logo.get_rect(center=(tela.get_width() // 2, 280))
        tela.blit(logo, logo_rect)

        y_base = 480

        if estado_menu == "menu":
            for i, botao in enumerate(botoes_menu):
                img = botao["sel"] if i == indicevertical else botao["normal"]
                x_central = (tela.get_width() - img.get_width()) // 2
                tela.blit(img, (x_central, y_base))
                y_base += img.get_height() + 20

        elif estado_menu == "continuar":        
            for i, botao in enumerate(botoes_saving):
                img = botao["sel"] if i == indicevertical else botao["normal"]
                x_central = (tela.get_width() - img.get_width()) // 2
                tela.blit(img, (x_central, y_base))
                y_base += img.get_height() + 20

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    mostrar_menu()