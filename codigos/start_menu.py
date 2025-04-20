import pygame
import sys
import os
import config
import creditos
from pathlib import Path
from config import largura, altura

fonte_titulo = pygame.font.SysFont("Arial", 48)

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

    botao_start, botao_start_sel = carregar_botao("imagens/botoes/start.png", "imagens/botoes/start_selected.png")
    botao_cred, botao_cred_sel = carregar_botao("imagens/botoes/creditos.png", "imagens/botoes/creditos_selected.png")
    botao_sair, botao_sair_sel = carregar_botao("imagens/botoes/sair.png", "imagens/botoes/sair_selected.png")
    botao_continue, botao_continue_sel = carregar_botao("imagens/botoes/continue.png", "imagens/botoes/continue_selected.png")
    botao_novo, botao_novo_sel = carregar_botao("imagens/botoes/novo.png", "imagens/botoes/novo_selected.png")
    botao_voltar, botao_voltar_sel = carregar_botao("imagens/botoes/voltar.png", "imagens/botoes/voltar_selected.png")

    botoes_menu = [
        {"normal": botao_start, "sel": botao_start_sel, "nome": "Start"},
        {"normal": botao_cred, "sel": botao_cred_sel, "nome": "Créditos"},
        {"normal": botao_sair, "sel": botao_sair_sel, "nome": "Sair"}
    ]

    botoes_saving = [
        {"normal": botao_continue, "sel": botao_continue_sel, "nome": "Continuar"},
        {"normal": botao_novo, "sel": botao_novo_sel, "nome": "Novo Jogo"},
        {"normal": botao_voltar, "sel": botao_voltar_sel, "nome": "Voltar"}
    ]

    indicevertical = 0
    indicehorizontal = 0
    frame_index = 0
    save = Path("save.txt")
    estado_menu = "menu"  # 'menu' ou 'continuar'

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

                elif evento.key == pygame.K_a  or evento.key == pygame.K_LEFT:
                    indicehorizontal = (indicehorizontal - 1) % (len(botoes_menu) if estado_menu == "menu" else len(botoes_saving))

                elif evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
                    indicehorizontal = (indicehorizontal + 1) % (len(botoes_menu) if estado_menu == "menu" else len(botoes_saving))

                elif evento.key == pygame.K_ESCAPE:
                    estado_menu = "menu"
                    indicevertical = 0

                elif evento.key == pygame.K_RETURN:
                    if estado_menu == "menu":
                        if botoes_menu[indicevertical]["nome"] == "Start":
                            if save.exists():
                                estado_menu = "continuar"
                                indicevertical = 0
                            else:
                                with open("save.txt", "a") as arquivo_save:
                                    arquivo_save.write("")
                                return "jogo"

                        elif botoes_menu[indicevertical]["nome"] == "Créditos":
                            creditos.executar_creditos()
                            return "menu"

                        elif botoes_menu[indicevertical]["nome"] == "Sair":
                            pygame.quit()
                            sys.exit()

                    elif estado_menu == "continuar":
                        if botoes_saving[indicehorizontal]["nome"] == "Continuar":
                            return "jogo"
                        
                        elif botoes_saving[indicehorizontal]["nome"] == "Novo Jogo":
                            with open("save.txt", "w") as arquivo_save:
                                arquivo_save.write("")
                            return "jogo"
                        
                        elif botoes_saving[indicehorizontal]["nome"] == "Voltar":
                            estado_menu = "menu"                      

        # Desenho da tela
        tela.blit(frames[frame_index], (0, 0))
        frame_index = (frame_index + 1) % len(frames)

        tela.blit(logo, (80, 135))

        if estado_menu == "menu":
            y_base = 480
            for i, botao in enumerate(botoes_menu):
                img = botao["sel"] if i == indicevertical else botao["normal"]
                tela.blit(img, (112, y_base))
                y_base += img.get_height() + 20

        elif estado_menu == "continuar":
            x_base = 360

            mensagem = fonte_titulo.render("Pronto para continuar seu conto\nou começar um novo?", False, (255, 255, 255))
            rect_texto = mensagem.get_rect(center=(largura // 2, altura // 2))
            tela.blit(mensagem, rect_texto)            

            tela.blit(frames[frame_index], (0, 0))
            frame_index = (frame_index + 1) % len(frames)
            for i, botao in enumerate(botoes_saving):
                img = botao["sel"] if i == indicehorizontal else botao["normal"]
                tela.blit(img, (x_base, 600))
                x_base += img.get_width() + 20

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    mostrar_menu()