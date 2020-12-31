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


g1_pos_x = 170
g1_pos_y = 150
g1_top_max_pos = 50
g1_bottom_max_pos = g1_pos_y

speed= -5


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.blit(background4_png,(0,0))
    screen.blit(trampoline3_png,(25,265))
    #screen.blit(cloud1_png,(40,30))
    #screen.blit(cloud1_png,(900,10))
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
