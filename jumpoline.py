import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background4_png = pygame.image.load('background4.png')
trampoline3_png = pygame.image.load('trampoline3.png')
g1_png = pygame.image.load('g1.png')
g1falling_png = pygame.image.load('g1falling.png')
g2_png = pygame.image.load('g2.png')
#cloud1_png = pygame.image.load('cloud1.png')
clouds_png = pygame.image.load('clouds.png')
#g4_png = pygame.image.load('g4.png')

game_font = pygame.font.Font(None,60)
text_surface = game_font.render('GAME OVER',True,(0,240,170))
text_rect = text_surface.get_rect(center = (640,360))

t1_pos_x = 550
t1_pos_y = 550

trampoline_rect=(t1_pos_x,t1_pos_y)

g1_pos_x = 550
g1_pos_y = 300
g1_rect=(g1_pos_x,g1_pos_y)

g1_top_max_pos = 50
g1_bottom_max_pos = g1_pos_y

speed= -20

collided = True
started = False

while True:
    g1_rect=g1_png.get_rect(center =(g1_pos_x,g1_pos_y))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        trampoline_rect = trampoline3_png.get_rect(center =(x, t1_pos_y))
        #print(x,g1_pos_x)
        #if g1_rect.collidepoint(x,t1_pos_y):
        if x - g1_pos_x >-50 and x - g1_pos_x <20 :
           #print("collide")
           collided = True
        elif started:
           collided = False
      if event.type == pygame.MOUSEBUTTONDOWN:
       started = True

        #print(x)
        #t1_pos_x = x
    screen.blit(background4_png,(0,0))
    screen.blit(trampoline3_png,(trampoline_rect))
    screen.blit(clouds_png,(0,0))
    if collided and started:
       screen.blit(g1_png,g1_rect)
    else:
       screen.blit(g1falling_png,(550,200))
       started = False

    if g1_pos_y <= g1_top_max_pos or g1_pos_y > g1_bottom_max_pos :
       speed = speed * -1
    g1_pos_y = g1_pos_y + speed

    #if g1_pos_y > g1_top_max_pos:
       #g1_pos_y = g1_pos_y - 1
    #if g1_pos_y <= g1_top_max_pos:
       #g1_pos_y = g1_pos_y + 1


    pygame.display.update()
    clock.tick(120)
