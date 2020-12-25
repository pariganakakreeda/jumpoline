import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background1_png = pygame.image.load('background1.png')
human1_png = pygame.image.load('human1.png')
trampoline_png = pygame.image.load('trampoline.png')



while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.blit(background1_png,(0,0))
    screen.blit(human1_png,(70,70))
    pygame.display.update()
    clock.tick(120)
