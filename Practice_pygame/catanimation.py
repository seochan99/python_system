import pygame,sys 
from pygame.locals import *

pygame.init()

FPS = 30 #초당 프레임 
fpsClock = pygame.time.Clock() #Clock 객체는 게임 루프를 돌 때 약간씩 간격을 줘서 프로그램이 너무 빨리 수행되지 않도록 한다. 

#setting Window
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Animation")

WHITE =(255,255,255)
catImg = pygame.image.load("cat.png")
catx = 10
caty = 10 #x,y좌표 
direction = "right"

while True : 
    DISPLAYSURF.fill(WHITE)

    if direction == "right": #와따까따
        catx += 5
        if catx == 280:
            direction = "down"
    elif direction == "down":
        caty+=5
        if caty==220:
            direction = "left"
    elif direction =="left":
        catx-=5
        if catx ==10:
            direction=="up"
    elif direction=="up":
        caty -=5
        if caty==10:
            direction == "right"

    DISPLAYSURF.blit(catImg,(catx,caty)) #화면에 그리기 

    for event in pygame.event.get(): #종료키 만들기 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update() 
    fpsClock.tick(FPS) #일정속도로 게임 유지 틱 ㅇㅇ updatae 다음에 언급