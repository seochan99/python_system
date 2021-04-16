# Simulate (a Simon clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 #버튼을 누르지 않으면 4초후 게임 종료 
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Chans Simulate")

    BASICFONT = pygame.font.Font("freesansbold.ttf",16)
    infoSurf = BASICFONT.render("Match the Patter by Clicking on the button or using the Q,W,A,S keys.",1,DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10,WINDOWHEIGHT - 25)

    #사운드파일 업로드 
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')

    #새게임에서 사용할 변수를 초기화한다.
    pattern =[] #색깔 패턴을 저장한다.
    currentStep = 0  #플레이어가 다음에 눌러야 하는 색깔 
    lastClickTime = 0 # 플레이어가 이전 버튼을 누른 시간 
    score = 0 
    #이 밑에 값이 False면 현재 시뮬레이트가 패턴을 보여주고 있는 상태이다.
    #True 면 버튼 클릭 기다리고 있다.
    waitingForInput = False 

    while True :
        clickedButton= None
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render("Socre : "+str(score),1,WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH- 100,10)
        DISPLAYSURF.blit(scoreSurf,scoreRect)

        DISPLAYSURF.blit(infoSurf,infoRect)

        checkForQuit()
        for event in pygame.event.get(): # event loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex,mousey)
            elif event.type == KEYDOWN :
                if event.key == K_q:
                    clickedButton == YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN
        
        if not waitingForInput: #False 일때 
            #패턴을 자동으로 보여준다.
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW,BLUE,RED,GREEN)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True 
        else : 
            #wait for the player to enter button
            if clickedButton and clickedButton == pattern[currentStep]:
                #맞는 버튼을 클릭(버튼클릭 && 옳은 버튼 클릭 )
                flashButtonAnimation(clickedButton)
                #클릭한 버튼 색 반쨕~ 
                currentStep += 1
                lastClickTime = time.time() # 시간 초기화 

                if currentStep == len(pattern):
                    #패턴의 마지막 버튼을 클릭하였다.
                    changeBackgroundAnimation()
                    score += 1 
                    waitingForInput = False 
                    currentStep = 0 #게임 턴이 종료되고 맨 처음으로 리셋한다
            
            elif (clickedButton  and clickedButton != pattern[currentStep]) or (currentStep!=0 and time.time()-TIMEOUT > lastClickTime):
                #버튼을 잘못눌렀거나 시간 초과
                gameOverAnimation()
                #reset for new game
                pattern=[]
                currentStep= 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()
 
def checkForQuit():
    for event in pygame.event.get(QUIT): # 모든 QUIT 이벤트 가져온다.
        terminate() # QUIT 발생시 종료
    for event in pygame.event.get(KEYUP): #모든 키업 이벤트 가져온다.
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event) #다른 KEYUP EVENT 객체는 이벤트 큐에 돌려놓는다.

def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT

    origSurf =DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE,BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in((0,255,1),(255,0,-1)): #애니메이션 루프
        for alpha in range(start,end,animationSpeed*step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf,(0,0))
            flashSurf.fill((r,g,b,alpha))
            DISPLAYSURF.blit(flashSurf,rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf,(0,0))

def drawButtons():
    pygame.draw.rect(DISPLAYSURF,YELLOW,YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)

def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    newBgSurf = pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0,255,animationSpeed): # animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r,g,b,alpha))
        DISPLAYSURF.blit(newBgSurf,(0,0))

        drawButtons() #색 위에 버튼은ㄹ 다시 그린다.

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor

def gameOverAnimation(color=WHITE,animationSpeed=50):
    #모든 비프음을 한꺼번에 플레이 하며 배경색을 깜박거리게 한다.
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play()
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color 
    for i in range(3): #3번 깜박인ㄷ.
        for start, end, step in ((0,255,1),(255,0,-1)):
            for alpha in range(start,end,animationSpeed*step):
                checkForQuit()
                flashSurf.fill((r,g,b,alpha))
                DISPLAYSURF.blit(origSurf,(0,0))
                DISPLAYSURF.blit(flashSurf,(0,0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def getButtonClicked(x,y):
    if YELLOWRECT.collidepoint((x,y)):
        return YELLOW
    elif BLUERECT.collidepoint( (x, y) ):
        return BLUE
    elif REDRECT.collidepoint( (x, y) ):
        return RED
    elif GREENRECT.collidepoint( (x, y) ):
        return GREEN
    return None

if __name__ == "__main__":
    main()