import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Configuração da tela
largura = 640
altura = 400
PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sprites")

# Criando a fonte uma vez, fora do loop
fontegeorge = pygame.font.Font("Press_Start_2P/PressStart2P-Regular.ttf", 32)

class George(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        for i in range(1, 12):
            imagem = pygame.image.load(f'tentandousarpygame/frame{i}.jpeg')
            imagem = pygame.transform.scale(imagem, (int(1024 * 0.4), int(1024 * 0.4)))
            self.sprites.append(imagem)

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.bottomright = (largura, altura)  # Mantém a posição no canto inferior direito

        self.direcao = 1
        self.tempo_anterior = pygame.time.get_ticks()  # Marca o tempo inicial
        self.intervalo_animacao = 50  # Tempo fixo entre frames (100ms)

        self.animar = False

    def atacar(self):
        if not self.animar:  # Só inicia se já não estiver animando
            self.animar = True
            self.atual = 0  # Reinicia a animação

    def update(self):
        if self.animar:
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_anterior > self.intervalo_animacao:
                self.tempo_anterior = tempo_atual

                self.atual += self.direcao

                if self.atual >= len(self.sprites) - 1:
                    self.direcao = -1  # Começa a voltar

                elif self.atual <= 0:
                    self.direcao = 1  # Prepara para próxima animação
                    self.animar = False  # Para a animação

                self.image = self.sprites[self.atual]

# Criando grupo de sprites
todassprites = pygame.sprite.Group()
georgetransformando = George()
todassprites.add(georgetransformando)

# Loop principal
while True:
    tela.fill(PRETO)

    # Renderiza o texto uma vez por frame
    mensagem = 'SUUSII!!'
    textogeorge = fontegeorge.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            georgetransformando.atacar()

    todassprites.update()
    todassprites.draw(tela)

    # Desenha o texto na tela
    tela.blit(textogeorge, (80, 80))

    pygame.display.flip()