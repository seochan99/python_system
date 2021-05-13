import random, time, pygame, sys
from pygame.locals import *

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5 

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption("Chans Tetromino")

    showTextScreen('Tetromino')
    while True: #game loop
        if random.randint(0,1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.play(-1,0.0)
        runGame()
        pygame.mixer.music.stop()
        showTextScreen('Game Over')

def runGame():
    # setup variables for the start of the game
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False # note: there is no movingUp variable
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True: # game loop
        if fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, fallingPiece):
                return # can't fit a new piece on the board, so game over

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == KEYUP:
                if (event.key == K_p):
                    # Pausing the game
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Paused') # pause until a key press
                    pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1

        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not isValidPosition(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
   

def makeTextObjs(text,font,color):
    surf = font.render(text,True,color)
    return surf, surf.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def checkForKeyPress():
    # KeyUp ㅇㅣ벤트가 발생했는지 이벤트 큐를 찾는다.
    # 키다운 이벤트를 찾아서 이벤트 큐에서 제거한다.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN,KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None 

def showTextScreen(text):
    # 이 함수는 플레이어가 키를 누를때 까지 화면 중간에 커다란 글씨를 그려서 보여준다.

    # 텍스트의 그림자 효과를 그린다.
    titleSurf, titleRect = makeTextObjs(text,BIGFONT,TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH/2),int(WINDOWHEIGHT/2))
    DISPLAYSURF.blit(titleSurf,titleRect)

    # drawing text
    titleSurf,titleRect = makeTextObjs(text,BIGFONT,TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH/2)-3,int(WINDOWHEIGHT/2)-3)
    DISPLAYSURF.blit(titleSurf,titleRect)

    # drawing "Press a Key to Play"
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play',BASICFONT,TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH/2),int(WINDOWHEIGHT)+100)
    DISPLAYSURF.blit(pressKeySurf,pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event) 

def calculateLevelAndFallFreq(score):
    #점수에 따라 플레이어의 레벨을 계산해서 반환한다.
    #그리고 피스가 얼마나 빨리 떨어져야하는지 계산한다.
    level = int(score/3) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level,fallFreq

def getNewPiece():
    # 무작위로 회전시키고 무작위 색깔을 가진 새 피스를 반환한다.
    shape = random.choice(list(PIECES.keys()))
    newPiece ={
        'shape':shape,
        'rotation':random.randint(0,len(PIECES[shape])-1),
        'x':int(BOARDWIDTH/2) - int(TEMPLATEWIDTH/2),
        'y':-2, # 보드의 위쪽에서 시작한다(좌표는 0 보다 작다)
        'color':random.randint(0,len(COLORS)-1)
    }
    return newPiece

def addToBoard(board,piece):
    # 피스의 위치, 형태, 회전 여부에 따라 보드를 채운다.
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def getBlankBoard():
    #비어 있는 새 보드 데이터 구조를 만들어 반환한다.
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK]*BOARDHEIGHT)
    return board 

def isOnBoard(x,y):
    return x>=0 and x< BOARDWIDTH and y<BOARDHEIGHT

def isValidPosition(board,piece,adjX=0,adjY=0):
    #피스가 보드에 있고 충동하지 않았으면 True 를 반환한다.
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY<0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x+piece['x']+adjX,y+piece['y']+adjY):
                return False
            if board[x+piece['x']+adjX][y+piece['y']+adjY] != BLANK:
                return False
    return True 

def isCompleteLine(board,y):
    #상자로 채워진 줄에 빈칸이 없으면 True를 반환한다.
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False 
    return True 

def removeCompleteLines(board):
    #보드에서 완전하게 완성된 줄을 제거한다. 그리고 다른 줄을 모두 아래로 내리고 몇 개의 행이 완성되었는지 반환한다.
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1 #보드 맨 아랫부분의 y부터 시작한다.
    while y >=0:
        if isCompleteLine(board,y):
            #행을 한 줄 없애고 상자를 모두 한 줄 아래로 내린다.
            for pullDownY in range(y,0,-1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            #맨 위의 줄을 빈칸으로 설정한다.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved +=1
            #반복문에서 처음에 y는 그대로인데 한 칸 아래로 내린 줄 또한 완성된 줄이라면 그 줄도 없애야한다
        else :
            y -=1 #한 줄씩 위로 올라가면서 검사한다.
    return numLinesRemoved

def convertToPixelCoords(boxx,boxy):
    #주어진 보드 좌표계를 픽셀 좌표계로 변환한다.
    return(XMARGIN +(boxx*BOXSIZE)),(TOPMARGIN+(boxy*BOXSIZE))

def drawBox(boxx,boxy,color,pixelx=None,pixely=None):
    # 보드 좌표계 x,y 좌표에 상자 하나를 그린다 (테트로미노는 4개의 상자로 구성된다)
    #만약 pixelx,pixely 값을 주면 픽셀 좌표계에 상자를 그린다
    if color == BLANK:
        return
    if pixelx == None and pixely == None :
        pixelx,pixely = convertToPixelCoords(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,COLORS[color],(pixelx+1,pixely+1,BOXSIZE-1,BOXSIZE-1))
    pygame.draw.rect(DISPLAYSURF,LIGHTCOLORS[color],(pixelx+1,pixely+1,BOXSIZE - 4,BOXSIZE-4))

def drawBoard(board):
    #보드 주면에 테두리를 그린다.
    pygame.draw.rect(DISPLAYSURF,BORDERCOLOR,(XMARGIN-3,TOPMARGIN-7,(BOARDWIDTH*BOXSIZE)+8,(BOARDHEIGHT*BOXSIZE)+8),5)

    # 보드의 배경색을 채운다.
    pygame.draw.rect(DISPLAYSURF,BGCOLOR,(XMARGIN,TOPMARGIN,BOXSIZE*BOARDWIDTH,BOXSIZE*BOARDHEIGHT))
    #보드의 각 상자를 그린다.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])

def drawStatus(score,level):
    #스코어 텍스트를 그린다.
    scoreSurf = BASICFONT.render("Score : %s" %score,True,TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf,scoreRect)

    #draw level text 
    levelSurf = BASICFONT.render("Level : %s" %level,True,TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150,50)
    DISPLAYSURF.blit(levelSurf,levelRect)

def drawPiece(piece,pixelx=None,pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None :
        #특정값으로 지정되지 않았으면 피스 데이터 구조에 저장된 위치를 사용한다.
        pixelx,pixely = convertToPixelCoords(piece['x'],piece['y'])

    # 피스를 구성하는 각 상자들을 그린다.
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None,None,piece['color'],pixelx+(x*BOXSIZE),pixely+(y*BOXSIZE))


def drawNextPiece(piece):
    nextSurf = BASICFONT.render("NEXT : ",True,TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH-120,80)
    DISPLAYSURF.blit(nextSurf,nextRect)
    drawPiece(piece,pixelx=WINDOWWIDTH - 120, pixely=100)

if __name__ == '__main__':
    main()