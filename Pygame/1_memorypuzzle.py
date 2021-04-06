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
BOARDWIDTH = 4
BOARDHEIGHT = 4 #아이콘 가로줄 수 
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

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK,DISPLAYSURF #잔역변수 설정 
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Chans Memory Puzzle")
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
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        #게임 시작 에니메이션을 보여준다. 
                        startGameAnimation(mainBoard)
                    firstSelection = None # firstSelection 변수를 리셋 

        #화면을 다시 그린 다음 시간 지연을 기다린다. 
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#열린 상자에 대한 데이터 구조만들기
def generateRevealedBoxesData(val): #구성요소의 값을 Val로 한다
    revealedBoxes = []   
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT) #불리언 값을 가지는 2차원 리스트를 만든다. 
    return revealedBoxes #revealedBoxes[x][y]가 된다. 

def getRandomizedBoard():
    #모든 가능한 색에서 가능한 모양의 목록을 모두 얻어낸다.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))
    
    random.shuffle(icons)#아이콘 리스트의 순서를 랜덤으로한다.
    numIconsUsed = int(BOARDWIDTH*BOARDHEIGHT/2) # 얼마나 많은 아이콘이 필요한지 계산
    icons = icons[:numIconsUsed] * 2 #각각의 짝을 만든다
    random.shuffle(icons)

    #랜덤하게 아이콘이 놓여 있는 게임판의 데이터 구조를 만든다.
    board = []
    for x in range(BOARDWIDTH):
        column=[]
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # 방금 추가한 아이콘을 지운다.
        board.append(column)
    return board 

def splitIntoGroupsOf(groupSize,theList):
    #리스트를 2차원 리스트로 만든다. 안쪽의 리스트는 최대로 groupSize개만큼의 아이템이 있다.
    result = []
    for i in range(0,len(theList),groupSize):
        result.append(theList[i:i+groupSize])
    return result

def leftTopCoordsOfBox(boxx,boxy):
    #게임판 좌표계를 픽셀 좌표계로 변환한다.
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE )+ YMARGIN
    return (left, top)

#픽셀 좌표계에서 게임판 좌표계로 변환하기
def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)
            if boxRect.collidepoint(x,y): #이 안에 들어가 있으면 True
                return (boxx,boxy)
    return (None,None)

def drawIcon(shape,color,boxx,boxy):
#그리기 함수에서는 대부분 상자의 중간위치와 1/4위치를 필요 하는 경우가 많아서 미리정의
    quarter = int(BOXSIZE*0.25) #syntactic sugar
    half = int(BOXSIZE*0.5) 

    left,top = leftTopCoordsOfBox(boxx,boxy) #보드의 좌표에서 픽셀의 좌표를 얻는다. 
    #형태를 그린다. 
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))

#이런식으로 하면 코드를 읽기 더 쉽당 
def getShapeAndColor(board,boxx,boxy): 
    #x,y 위치의 아이콘 형태의 값은 board[x][y][0]
    #x,y 위치의 아이콘 색의 값은 board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board,boxes,coverage):
    # 닫히거나 열린 상태의 상자를 그린다. 
    # 상자는 아이템 2개짜리 리스트이며 상자의 x,y 위치를 가진다.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,BOXSIZE,BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape,color,box[0],box[1])
        if coverage>0: # 닫힌 상태이면 덮개만 그린다. 
            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,coverage,BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board,boxesToReveal):
    #상자가 열리는 애니메인션 수행
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)
        #coverage가 REVEALSPEED 의 속도에 따라 이뤄진다 ! 

def coverBoxesAnimation(board,boxesToCover):
    #상자가 닫히는 애니메이션 수행
    for coverage in range(0,BOXSIZE+REVEALSPEED,REVEALSPEED):
        drawBoxCovers(board,boxesToCover,coverage)

def drawBoard(board,revealed):
    #모든 상자를 상태에 맞게 그리기
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                #닫힌 상자를 그린다.
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
            else:
                #열린 상자, 즉 아이콘을 그린다.
                shape, color = getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)

def drawHighlightBox(boxx,boxy):
    left,top = leftTopCoordsOfBox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HIGHLIGHTCOLOR,(left-5,top-5,BOXSIZE+10,BOXSIZE+10),4)

def startGameAnimation(board):
    # 무작위로 한 번에 8 개씩 상자를 열어서 보여준다.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8,boxes)
    
    drawBoard(board,coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board,boxGroup)
        coverBoxesAnimation(board,boxGroup)
    
def gameWonAnimation(board):
    #플레이어가 승리하면 배경색을 깜빡인다. ! 
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1,color2 = color2,color1 #색을 바꾼다.
        DISPLAYSURF.fill(color1)
        drawBoard(board,coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

def hasWon(revealedBoxes):
    #모든 상자를 열었으면 True 아니면 False
    for i in revealedBoxes:
        if False in i:
            return False # 닫힌 상자가 있으면 False
    return True

if __name__ == '__main__':
    main()