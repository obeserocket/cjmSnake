#!/usr/bin/python3
#-Recreation of pong by cjm
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screenx = 800
screeny = 600

def main():
    pygame.init()
    size = (screenx, screeny)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PONG")

    #pygame.key.set_repeat(50, 1) #causes holding a key to send multiple pygame.KEYDOWN events

    padW = 40 #the width of the paddle
    padH = 100 #the height of the paddle

    pos1 = [5,screeny/2-padH/2] #---------------------
    pos2 = [screenx-5-padW, screeny/2-padH/2]#-start the paddles off with a margin of 5, halfway down the screen 
    ball = [screenx/2, screeny/2, ]
    done = False
    clock = pygame.time.Clock()

    #--Main Loop--
    while not done:
        for event in pygame.event.get(): #----Event Processing Loop
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN: #If event was a keypress
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_w:
                    pos1[1] -= 10
                if event.key == pygame.K_s:
                    pos1[1] += 10
                #if event.key == pygame.K_w:
                #    pos1[1] -= 10
                #if event.key == pygame.K_s:
                #    pos1[1] += 10
                if event.key == pygame.K_UP:
                    pos2[1] -= 10 #Move paddle2 up one REMINDER: x starts at top
                if event.key == pygame.K_DOWN:
                    pos2[1] += 10 #Move paddle2 down one
        #-- Game Logic

        #-- Drawing Code
        screen.fill(BLACK)
        pygame.draw.rect(screen, (WHITE), (pos1[0], pos1[1], padW, padH)) #draw the first paddle
        pygame.draw.rect(screen, (WHITE), (pos2[0], pos2[1], padW, padH)) #draw the second paddle
        pygame.display.flip()

        clock.tick(60)
    pygame.quit
    print("Quitting")
main()
