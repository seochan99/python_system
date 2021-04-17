import random, pygame, sys
from pygame.locals import *

FPS = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20 
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 #신태틱 슈가 : 벌레의 머리부분의 인덱스 표시 

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font("freesansbold.ttf",18)
    pygame.display.set_caption("Chans Wormy")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    # 무작위로 시작하는 위치 정하기 
    startx = random.randint(5,CELLWIDTH - 6)
    starty = random.randint(5,CELLHEIGHT - 6)
    wormCoords=[
        {
            "x":startx,
            "y":starty
        },
        {
            "x":startx - 1,
            "y":starty
        },
        {
            "x":startx -2,
            "y":starty
        }
    ]
    direction = RIGHT

    #사과를 무작위로 정한 위치에 놓기 
    apple = getRandomLocation()

    while True: #메인 게임 루프
        for event in pygame.event.get(): #이벤트 핸들 
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT :
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
        
        #벌레가 자기 자신이나 벽과 충돌했는지 검사한다.
        if wormCoords[HEAD]["x"] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT :
            return #end game
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return # end game 
        
        #벌레가 사과를 먹었는지 검사한다.
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            #벌레의 꼬리 부분을 지우지 말 것 
            apple = getRandomLocation() # new APple
        else :
            del wormCoords[-1] # 벌레의 꼬리부분을 지운다?
        
        # 움직이는 방향으로 마디를 더해서 벌레를 움직인다.
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0,newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords)-3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render("Press a Key to play",True,DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200,WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf,pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0 :
        terminate()
    
    KeyUpEvents = pygame.event.get(KEYUP)
    if len(KeyUpEvents) == 0 :
        return None 
    if KeyUpEvents[0].key == K_ESCAPE:
        terminate()
    return KeyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font("freesansbold.ttf",100)
    titleSurf1 = titleFont.render("Wormy!",True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render("Wormy!",True, GREEN)

    degrees1 = 0
    degress2 = 0
    while True : 
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1,degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1,rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2,degress2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center =(WINDOWWIDTH/2,WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2,rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return 
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degress2 += 7

def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation():
    return {'x':random.randint(0,CELLWIDTH-1),'y':random.randint(0,CELLHEIGHT-1)}

def showGameOverScreen():
    gameOverFont = pygame.font.Font("freesansbold.ttf",150)
    gameSurf = gameOverFont.render("Game",True,WHITE)
    overSurf = gameOverFont.render("Over",True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2,80)
    overRect.midtop = (WINDOWWIDTH/2,gameRect.height + 85 + 25)

    DISPLAYSURF.blit(gameSurf,gameRect)
    DISPLAYSURF.blit(overSurf,overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # 이벤트 큐에 들어있는 모든 키 입력을 삭제한다.

    while True :
        if checkForKeyPress():
            pygame.event.get() #clear event queue
            return 

def drawScore(score):
    scoreSurf = BASICFONT.render('Score : %s' %(score),True,WHITE)
    scoreRect = scoreSurf.get_rect() 
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf,scoreRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(DISPLAYSURF,DARKGREEN,wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x+4,y+4,CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF,GREEN,wormInnerSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF,RED,appleRect)

def drawGrid():
    for x in range(0,WINDOWWIDTH,CELLSIZE): #세로선을 그린다. 
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(x,0),(x,WINDOWHEIGHT))
    for y in range(0,WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(0,y),(WINDOWWIDTH,y))

if __name__ == "__main__":
    main()