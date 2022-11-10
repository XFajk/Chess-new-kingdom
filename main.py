import pygame
from pygame.locals import *

import random
import time
import math
import sys

pygame.init()

def main():
    ZOOM = 1
    WS = (768,640)
    DS = (WS[0]/ZOOM,WS[1]/ZOOM)
    window = pygame.display.set_mode(WS)
    display = pygame.Surface(DS)

    clock = pygame.time.Clock()

    # constants
    MAX_FPS = 60

    # entities

    # logic vars


    # main loop 
    running = True
    while running:

        display.fill((255,255,255))

        pygame.draw.rect(display,(255,0,0),(40,40,64,64))

        pygame.display.update()

        for event in pygame.event.get():
            if  event.type == QUIT:
                running = False
        
        surf = pygame.transform.scale(display, WS)
        window.blit(display,(0,0))

        clock.tick(MAX_FPS)
        pygame.display.set_caption(f"chess-new-kingdom FPS:{int(clock.get_fps())}")

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()


