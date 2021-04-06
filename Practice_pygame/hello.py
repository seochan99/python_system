import pygame, sys
from pygame.locals import *

pygame.init() #pygame 초기화
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("Chans World")
while True: #main game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()