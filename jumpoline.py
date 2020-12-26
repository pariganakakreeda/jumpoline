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

while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.blit(background1_png,(0,0))
    #screen.blit(human1_png,(370,70))
    screen.blit(trampoline_png,(200,350))
    screen.blit(g1_png,(g1_pos_x,g1_pos_y))
   # screen.blit(human2_png,(370,70))


    pygame.display.update()
    clock.tick(120)
