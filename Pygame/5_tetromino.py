# Tetromino (a Tetris clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

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
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    BIGFONT = pygame.font.Font('freesansbold.ttf',100)
    pygame.display.set_caption("Chans Tetromino")

    showTextScreen('Tetromino')
    while True: #game loop
        if random.randint(0,1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.load(-1,0.0)
        runGame()
        pygame.mixer.music.stop()
        showTextScreen('Game Over')

def runGame():
    #게임 시작 부분에서 변수 설정
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False 
    movingLeft = False
    movingRight = False 
    score = 0 
    level, fallFreq = calculateLevelAndFallFreq(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True: #game loop
        if fallingPiece == None:
            #떨어지고 있는 피스가 없으면 새 피스가 위에서 떨어지도록 한다.
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time #reset lastFallTime 

            if not isValidPosition(board,fallingPiece):
                return # end game 
        
        checkForQuit()
        for event in pygame.event.get(): #Event loop
            if event.tpye == KEYUP:
                if(event.key == K_p):
                    #게임을 잠시 멈춘다. 
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Paused') # 키를 누를 때까지 멈춘다.
                    pygame.mixer.music.play(-1,0.0)
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
                if(event.key == K_LEFT or event.key == K_a) and isValidPosition(board,fallingPiece,adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False 
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()
                #회전
                elif(event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation']+1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation']-1 % len(PIECES[fallingPiece['shape']]))
                elif(event.key == K_q): #반대방향 회전 
                    fallingPiece['rotation'] = (fallingPiece['rotation']-1)%len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board,fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation']+1)%len(PIECES[fallingPiece['shape']])
                
                #피스를 빨리 떨어뜨린다
                elif(event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board,fallingPiece,adjY=1):
                        fallingPiece['y']+=1
                    lastMoveDownTime = time.time()
                
                # 현재 피스를 바닥으로 떨어뜨린다.
                elif event.key = K_SPACE:
                    movingDown = False
                    movingRight = False
                    movingLeft = False
                    for i in range(1,BOARDHEIGHT):
                        if not isValidPosition(board,fallingPiece,adjY=1):
                            break
                    fallingPiece['y']+=i-1
        # 사용자의 입력에 따라 피스 움직이기
        if(movingLeft or movingRight) and time.time()-lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board,fallingPiece,adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board,fallingPiece,adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()
        
        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        #떨어질 시간이 되면 피스를 떨어뜨린다.
        if time.time() -lastFallTime>fallFreq:
            #피스가 착지했는지 검사한다.
            if not isValidPosition(board,fallingPiece,adjY=1):
                #떨어지는 피스가 칙지했으면 보드에 둔다.
                addToBoard(board,fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None 
            else :
                #피스가 아직 착지하지 않았으면 피스를 아래로 움직인다.
                fallingPiece['y'] += 1
                lastFallTime = time.time()
        #모두 그리쟈
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score,level)
        drawNextPiece(nextPiece)
        if fallingPiece != None :
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)