# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys 
from pygame.locals import *

FPS = 30 # 초당 프레임
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8 # 상자가 보여졌다 가려지는 속도
BOXSIZE = 40 #상자 너비와 높이
GAPSIZE = 10 
BOARDWIDTH = 10
BOARDHEIGHT = 7 #아이콘 가로줄 수 
assert (BOARDWIDTH*BOARDHEIGHT)%2==0, "Board Needs To have an even Number of boxes for pairs of matches."
XMARGIN = int((WINDOWWIDTH -(BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT -(BOARDHEIGHT*(BOXSIZE+GAPSIZE)))/2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

LLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK,DISPLAYSURF #잔역변수 설정 
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0 # 마우스 이벤트 발생시 x좌표
    mousey = 0 # 마우스 이벤트 발생시 y좌표 

    mainBoard = getRandomizedBoard() #게임판의 상태를 나타내는 함수 
    revealedBoxes = generateRevealedBoxesData(False) #여기에 False를 전달하면 모든 구성요소 불리언 값이 False 가된다
    # False 면 닫힌상태 True이면 상자가 열린 상태이다 
    # 이 함수들이 반환할 값은 2차원 리스트이다. 

    firstSelection = None # 첫 번째 상자를 클릭했을 때 (x,y) 저장
    #프로그램은 이 값을 보고 두 번째 아이콘을 찾는 클릭인지 아닌지 알아낸다. 

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard) #미리보여주기 함수 나중에 정의할거 !

    while True: # Game Loop
        mouseClicked = False # 이 값이 true 이면 플레이어가 마우스를 클릭했다고 인식

        DISPLAYSURF.fill(BGCOLOR) #drawing the window
        drawBoard(mainBoard,revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and evnet.key == K_ESCAPE):
                pygame.quit()
                sys.exit() 
            elif event.type == MOUSEMOTION:
                mousex,mousey == event.pos #마우스를 움직였으니 커서위치를 저장 
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos 
                mouseClicked = True #클릭했으니 트루 ~ 
        
        boxx, boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None :
            #마우스가 현재 상자 위에 있다.
            if not revealedBoxes[boxx][boxy]: #False 라면 상자는 닫혀있다
                drawHighlightBox(boxx,boxy) #테두리를 그린당 ~ 
            if not revealedBoxes[boxx][boxy] and mouseClicked: #그 박스를 클릭했을 때 
                revealBoxesAnimation(mainBoard,[(boxx,boxy)]) #상자가 열리는 에니메이션 
                revealedBoxes[boxx][boxy] = True # 상자를 보이는 것으로 설정  열어둔다 !
                if firstSelection == None : # 현재의 상자가 처음 클릭 상자
                    firstSelection = (boxx,boxy)
                else: # 두번째 클릭한 상자 
                    #두 아이콘 짝이 맞는지 체크
                    icon1shape,icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2shape,icon2color = getShapeAndColor(mainBoard,boxx,boxy)
                    #getShapeAndColor 는 그 위치에 있는 아이콘의 색깔과 형태를 알아낸다. 
                    if icon1shape != icon2shape or icon1color != icon2color:
                        #아이콘이 서로 맞지 않다면 두 상자 모두 덮는다.
                        pygame.time.wait(1000) #1sec
                        coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False #상자 닫아 ! 
                        revealedBoxes[boxx][boxy] = False  
                    elif hasWon(revealedBoxes): #모든 아이콘이 열렸는지 확인한다. 
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        #게임판 재설정
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        #잠시 동안 게임판의 상자를 열어서 보여준다.
                         drawBoard(mainBoard,revealedBoxes)
                         pygame.display.update()
                         pygame.time.wait(1000)

                         #게임 시작 에니메이션을 보여준다. 
                         startGameAnimation(mainBoard)
                    firstSelection = None # firstSelection 변수를 리셋 

        #화면을 다시 그린 다음 시간 지연을 기다린다. 
        pygame.display.update()
        FPSCLOCK.tick(FPS)
