import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background4_png = pygame.image.load('background4.png')
trampoline3_png = pygame.image.load('trampoline3.png')
g1_png = pygame.image.load('g1.png')
g2_png = pygame.image.load('g2.png')
#cloud1_png = pygame.image.load('cloud1.png')
clouds_png = pygame.image.load('clouds.png')
#g4_png = pygame.image.load('g4.png')
t1_pos_x = 10
t1_pos_y = 550

trampoline_rect=(t1_pos_x,t1_pos_y)

g1_pos_x = 160
g1_pos_y = 110
g1_top_max_pos = 50
g1_bottom_max_pos = g1_pos_y

speed= -10


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        trampoline_rect = trampoline3_png.get_rect(center =(x, t1_pos_y))
        #print(x)
        #t1_pos_x = x
    screen.blit(background4_png,(0,0))
    screen.blit(trampoline3_png,(trampoline_rect))
    screen.blit(clouds_png,(0,0))
    screen.blit(g1_png,(g1_pos_x,g1_pos_y))

    if g1_pos_y <= g1_top_max_pos or g1_pos_y > g1_bottom_max_pos :
       speed = speed * -1
    g1_pos_y = g1_pos_y + speed

    #if g1_pos_y > g1_top_max_pos:
       #g1_pos_y = g1_pos_y - 1
    #if g1_pos_y <= g1_top_max_pos:
       #g1_pos_y = g1_pos_y + 1


    pygame.display.update()
    clock.tick(120)
