import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background1_png = pygame.image.load('background1.png')
trampoline_png = pygame.image.load('trampoline.png')
g1_png = pygame.image.load('g1.png')
g2_png = pygame.image.load('g2.png')

g1_pos_x = 525
g1_pos_y = 100
g1_top_max_pos = 50

direction=1


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.blit(background1_png,(0,0))
    screen.blit(trampoline_png,(200,350))
    screen.blit(g1_png,(g1_pos_x,g1_pos_y))

    if g1_pos_y < g1_top_max_pos or g1_pos_y > 100:
       direction *= -1

    g1_pos_y = g1_pos_y + direction 

    #if g1_pos_y <=350 and g1_pos_y >= g1_top_max_pos:
    #   g1_pos_y = g1_pos_y -1
    #else:
    #   g1_pos_y = g1_pos_y +1

    #if g1_pos_y >= g1_top_max_pos:



    pygame.display.update()
    clock.tick(120)
