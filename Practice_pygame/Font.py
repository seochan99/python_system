import pygame, sys
from pygame.locals import *

pygame.init() #pygame 초기화
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("Chans World")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

fontObj = pygame.font.Font("freesansbold.ttf",32)
textSurfaceObj = fontObj.render("Chans World!",True,GREEN,RED)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)


while True: #main game Loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()