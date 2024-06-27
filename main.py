import pygame
import random
import os
import time
from tkinter import simpledialog
from funcoes import limpar
limpar()

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("recursos/GatoFrente.png")
gatinho = pygame.image.load("recursos/GatoFrente.png")
fundoJogo = pygame.image.load("recursos/FundoChuva.png")
fundoInicio = pygame.image.load("recursos/FundoSolInicio.png")
fundoPerdeu = pygame.image.load("recursos/FundoChuvaPerdeu.png")

inimigoAgua = pygame.image.load("recursos/inimigoAgua.png")
inimigoRaio = pygame.image.load("recursos/inimigoRaio.png")
estrela = pygame.image.load("recursos/estrela.png")
tamanho = (600,400)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Gatinho na Chuva")
pygame.display.set_icon(icone)
inimigoAguaSound = pygame.mixer.Sound("recursos/inimigoAgua.wav")
inimigoRaioSound = pygame.mixer.Sound("recursos/inimigoRaio.wav")
miauSound = pygame.mixer.Sound("recursos/gatoMiado.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteInicio = pygame.font.SysFont("comicsans",55)
fontePerdeu = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("recursos/chuvaSoundtrack.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )
amarelo = (241, 242, 112)


def jogar(nome):
    pygame.mixer.Sound.play(inimigoAguaSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 300
    movimentoXPersona  = 0
    posicaoXinimigoAgua = 400
    posicaoYinimigoAgua = -240
    posicaoXEstrela = 0
    posicaoYEstrela = 50
    velocidadeinimigoAgua = 1
    pontos = 0
    larguraPersona = 40
    alturaPersona = 40
    velocidadeEstrela = 1.5
    largurainimigoAgua  = 8
    alturainimigoAgua  = 10
    dificuldade  = 2


    pygame.mixer.Sound.play(inimigoRaioSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 300
    movimentoXPersona  = 0
    posicaoXinimigoRaio = 100
    posicaoYinimigoRaio = -200
    velocidadeinimigoRaio = 1
    pontos = 0
    larguraPersona = 40
    alturaPersona = 40
    largurainimigoRaio = 8
    alturainimigoRaio = 10
    dificuldade  = 2
    tamanhoSol = 60
    tamanhoSolMaximo = 70
    tamanhoSolMinimo = 50
    velocidadeSol = 0.2

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 5
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -5
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona                     
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >550:
            posicaoXPersona = 540
            
        tela.fill(branco)
        tela.blit(fundoJogo, (0,0) )
        
        pygame.draw.circle(tela, amarelo, (525, 60), tamanhoSol )
        #tamanhoSol = tamanhoSol + 1
        tamanhoSol += velocidadeSol
        if tamanhoSol >= tamanhoSolMaximo or tamanhoSol <= tamanhoSolMinimo:
            velocidadeSol =- velocidadeSol
        

      

        tela.blit( gatinho, (posicaoXPersona, posicaoYPersona) )
        
        posicaoYinimigoAgua = posicaoYinimigoAgua + velocidadeinimigoAgua
        if posicaoYinimigoAgua > 600:
            posicaoYinimigoAgua = -40
            pontos = pontos + 1
            velocidadeinimigoAgua = velocidadeinimigoAgua + 1
            posicaoXinimigoAgua = random.randint(0,600)
            pygame.mixer.Sound.play(inimigoAguaSound)

        posicaoYinimigoRaio = posicaoYinimigoRaio + velocidadeinimigoRaio
        if posicaoYinimigoRaio > 600:
            posicaoYinimigoRaio = -40
            pontos = pontos + 1
            velocidadeinimigoRaio = velocidadeinimigoRaio + 1
            posicaoXinimigoRaio = random.randint(0,600)
            pygame.mixer.Sound.play(inimigoRaioSound)
            
        posicaoXEstrela= posicaoXEstrela + velocidadeEstrela
        if posicaoXEstrela > 600:
            posicaoXEstrela = 600
            posicaoXEstrela = 0

        tela.blit( estrela, (posicaoXEstrela, posicaoYEstrela))
        tela.blit( inimigoAgua, (posicaoXinimigoAgua, posicaoYinimigoAgua) )
        tela.blit( inimigoRaio, (posicaoXinimigoRaio, posicaoYinimigoRaio) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsinimigoAguaX = list(range(posicaoXinimigoAgua, posicaoXinimigoAgua + largurainimigoAgua))
        pixelsinimigoAguaY = list(range(posicaoYinimigoAgua, posicaoYinimigoAgua + alturainimigoAgua))
        pixelsinimigoRaioX = list(range(posicaoXinimigoRaio, posicaoXinimigoRaio + largurainimigoRaio))
        pixelsinimigoRaioY = list(range(posicaoYinimigoRaio, posicaoYinimigoRaio + alturainimigoRaio))
        
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsinimigoAguaY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsinimigoAguaX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                fim(nome, pontos)
        if  len( list( set(pixelsinimigoRaioY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsinimigoRaioX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                fim(nome, pontos)
        
    
        
        pygame.display.update()
        relogio.tick(60)

def fim(nome, pontos): 
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(miauSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoPerdeu, (0,0)) 
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteInicio.render("Reiniciar", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Pressione Enter para continuar...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)

def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteInicio.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)

def start():
    nome = simpledialog.askstring("Gatinho na Chuva","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoInicio, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (175,282,235,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteInicio.render("START", True, branco)
        tela.blit(textoStart, (200,282))

        
        
        pygame.display.update()
        relogio.tick(120)


start()