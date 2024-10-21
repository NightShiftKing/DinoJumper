import random
import pygame


pygame.init()

screen_width = 700
screen_height = 500

#creates game screen and caption
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Dino Jumper")

gameover = False
clock = pygame.time.Clock()
DinoX = 50
Dino_width = 20
DinoY = 200
Dino_height = 20 
touchGround = False
Dino_y_velocity = 0
CactusHeights = [32,16,8,32,12] 
CactusXpos = []
CactusImg = pygame.image.load('Cactus.png')
for x in range(1,5):
    CactusXpos.append(random.randrange(200,3000))

#BEGIN GAME LOOP######################################################
while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

    CactusXpos = [x -5 for x in CactusXpos]

    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640,5000)


    for x,y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-x), (30,80))
        b = pygame.Rect((DinoX, DinoY), (30,30))
        if a.colliderect(b) == True:
            gameover = True


    if (DinoY + Dino_height >= 480):
        touchGround = True

    else:
        touchGround = False

    if not touchGround:
        Dino_y_velocity += 1
    else:
        Dino_y_velocity = 0
        



    #keyboard input-----------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and touchGround:
        Dino_y_velocity -=20 


    DinoY += Dino_y_velocity
     


    #render section-----------------------------------vis
    screen.fill((0,0,0))

    
    pygame.draw.rect(screen, (255,255,255), (DinoX,DinoY,20,20))

    for x, y in zip(CactusXpos, CactusHeights):
        screen.blit(CactusImg, (x-15,480-y))

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()