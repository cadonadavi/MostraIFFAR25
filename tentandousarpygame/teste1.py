import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musicafundo = pygame.mixer.music.load('Mr Smith - Pushed.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.02)

barulhomoedinha = pygame.mixer.Sound('smw_coin.wav')
barulhoperdeu = pygame.mixer.Sound('smw_blargg.wav')

largura = 640
altura = 480
xcobra = largura//2
ycobra = altura//2

morreu = False
velocidade = 10

xcontrole = velocidade
ycontrole = 0

xmaca = randint(40, 600)
ymaca = randint(50, 430)

fonte = pygame.font.SysFont("arial", 32, True, False)

pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Joguinho da cobrinha do capiroto")
relogio = pygame.time.Clock()

listacorpo = []

def aumentacobra(listacorpo):
    if len(listacorpo) > pontos + 1:
       del listacorpo[0] 
    for XeY in listacorpo:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciarjogo():
    global pontos, xcobra, ycobra, listacabeca, listacorpo, xmaca, ymaca, morreu
    pontos = 0
    xcobra = largura//2
    ycobra = altura//2
    listacorpo = []
    listacabeca = []
    xmaca = randint(40, 600)
    ymaca = randint(50, 430)
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem1 = f"Pontos: {pontos}"
    textoformatado = fonte.render(mensagem1, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if xcontrole == velocidade:
                    pass
                else:
                    xcontrole = -velocidade
                    ycontrole = 0
            if event.key == K_d:
                if xcontrole == -velocidade:
                    pass
                else:
                    xcontrole = velocidade
                    ycontrole = 0
            if event.key == K_w:
                if ycontrole == velocidade:
                    pass
                else:
                    xcontrole = 0
                    ycontrole = -velocidade
            if event.key == K_s:
                if ycontrole == -velocidade:
                    pass
                else:
                    xcontrole = 0
                    ycontrole = velocidade

    xcobra = xcobra + xcontrole
    ycobra = ycobra + ycontrole

    cobra = pygame.draw.rect(tela, (0, 255, 0), (xcobra,ycobra,20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (xmaca, ymaca, 20, 20))

    pygame.draw.circle(tela, (255, 0, 0), (10, 10,), 5)
    pygame.draw.rect(tela, (0, 160, 0), (20, 5, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (35, 5, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (20, 20, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (5, 20, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (5, 35, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (20, 35, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (35, 35, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (5, 50, 10, 10))
    pygame.draw.rect(tela, (0, 160, 0), (20, 50, 10, 10))

    if cobra.colliderect(maca):
        xmaca = randint(40, 600)
        ymaca = randint(50, 430)
        pontos = pontos + 1
        barulhomoedinha.play()

    listacabeca = []
    listacabeca.append(xcobra)
    listacabeca.append(ycobra)
    
    listacorpo.append(listacabeca)

    if listacorpo.count(listacabeca) > 1:
        fontemorte = pygame.font.SysFont("arial", 20, True, False)
        mensagemmorte = 'Game Over! Pressione R para jogar novamente'
        textomorte = fontemorte.render(mensagemmorte, True, (0, 0, 0))
        barulhoperdeu.play()
        morreu = True
        while morreu:
            tela.fill((255,255,255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarjogo()
            
            tela.blit(textomorte, (100, 220))
            pygame.display.update()

    if xcobra > largura:
        xcobra = 0
    if xcobra < 0:
        xcobra = largura
    if ycobra < 0:
        ycobra = altura
    if ycobra > altura:
        ycobra = 0

    aumentacobra(listacorpo)

    tela.blit(textoformatado, (450, 40))

    pygame.display.update()