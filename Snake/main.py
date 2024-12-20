import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake")
largura, altura = (1200, 800)
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores RGB

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)


#parametros snake
tamanho_quadrado = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])
    
def desenhar_snake(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])
        
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helverica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)
    tela.blit(texto, [4, 4])
    
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0  
        
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0    
        
    return velocidade_x, velocidade_y
    

def rodar_jogo():
    fim_jogo = False
    
    x = largura /2
    y = altura/2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_snake = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    

    while not fim_jogo:
        tela.fill(preto)   
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        #desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        
        
        #atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        x += velocidade_x
        y += velocidade_y
        
        #desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_snake:
            del pixels[0]
            
        for pixel in pixels[:-1]:
            if pixel ==[x, y]:
                fim_jogo = True    
        
        desenhar_snake(tamanho_quadrado, pixels)
        
        #desenhar pontuacao
        desenhar_pontuacao(tamanho_snake - 1)
        
       
        
        #atualizacao da tela
        pygame.display.update()
        
        #criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_snake += 1
            comida_x, comida_y = gerar_comida()
             
        relogio.tick(velocidade_jogo)
        
rodar_jogo()
        
        