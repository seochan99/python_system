import pygame, sys, random
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 4  # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption("Chans Slide Puzzle")
    BASICFONT = pygame.font.Font("freesansbold.ttf",BASICFONTSIZE)
    #### 위에까지 가본 설정 ㅇㅇ

    #옵션 버튼과 둘러싸는 사각형은 options에 저장
    RESET_SURF, RESET_RECT = makeText("Reset", TEXTCOLOR,TILECOLOR,WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF,NEW_RECT = makeText("New Game",TEXTCOLOR,TILECOLOR,WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    SOLVE_SURF,SOLVE_RECT = makeText("Solve",TEXTCOLOR,TILECOLOR,WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80) #80번 움직여서 보드를 섞는다.
    SOLVEDBOARD = getStartingBoard() # 다 맞춘 게임판은 처음 게임판의 상태와 동일   
    allMoves = [] 

    while True: # main Game Loop
        slideTo = None # 플레이어가 어느 방향으로 타일을 미뤘는지 기록
        msg = "Click tile or press arrow keys to slide" # 왼쪽 상단 구석에 보여주자
        if mainBoard = SOLVEDBOARD:
            msg = "Solved !!! "

        drawBoard(mainBoard,msg) #DISPLAYSURF surface 객체 상에 반영

        checkForQuit() #종료를 눌렀는지 확인 
        for event in pygame.event.get(): # 이벤트 처리 루프
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard,event.pos[0],event.pos[1]) # mouse를 클릭했다면 함수에 마우스 위치를 넘긴다.
                # 위치를 넘기면 게임판의 좌표계를 반환한다. (메인보드와 게임보드는 다르게 ! )

                if(spotx,spoty) ==(None,None):
                    #게임판 밖의 다른 버튼을 클릭했는지 본다.
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on Reset button
                        allMoves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) # clicked on New Game button
                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button
                        allMoves = []
                else:
                    #클릭한 타일이 빈칸 옆에 있는지 확인한다.

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky :
                        slideTo = LEFT 
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN
       
            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN
        if slideTo:
            slideAnimation(mainBoard,slideTo,"Click tile or press arrow keys to slide.", 8) #화면상에 슬라이드를 보여준다.
            makeMove(mainBoard,slideTo) #실제 게임판 데이터 구조 변경 
            allMoves.append(slideTo) # 슬라이드를 기록한다.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): #QUIT 이벤트 가져온다.
        terminate()
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            terminate() : # esc keyup event end program
        pygame.event.post(event) #다른 keyup 이벤트 객체는 다시 돌려준다. 

def getStartingBoard():
    # 원래대로 정렬된 상태의 게임판 데이터 구조를 반환한다.
    # 예를 들어 BOARDWIDTH BOARDHEIGHT 가 모두 3이면
    # 이 함수는 [[1,4,7],[2,5,8],[3,6,0]] 반환
    counter = 1
    board = []             
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1
    
    board[BOARDWIDTH- 1][BOARDHEIGHT -1] = BLANK
    return board 

def getBlankPosition(board):
    # 빈칸 위치의 개임판 x,y 좌표를 반환한다.
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == BLANK:
                return (x,y)

def makeMove(board,move):
    # 이 함수는 이동이 가능한지 검사하지 않는다. 
    blankx,blanky=getBlankPosition(board)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky+1] = board[blankx][blanky+1],board[blankx][blanky] 
        #빈칸을 위로 올리고 숫자였던 카드를 빈칸으로, 빈칸을 숫자로 바꾼다 .
    elif move = DOWN:
        board[blankx][blanky], board[blankx][blanky-1] = board[blankx][blanky-1],board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]

def isValidMove(board,move):
    blankx,blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0])-1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)

def getRandomMove(board,lastMove=None):
    #가능한 모든 움직임으로부터 시작한다.
    validMoves =[UP,DOWN,LEFT,RIGHT]

    #움직일 수 없는 경우는 제외한다
    if lastMove == UP or not isValidMove(board,DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)
    return random.choice(validMoves)

def getLeftTopOfTile(tileX,tileY):
    left =XMARGIN+(tileX*TILESIZE)+(tileX - 1)
    top = YMARGIN + (tileY*TILESIZE) + (tileY - 1)
    return(left,top) 

def getSpotClicked(board,x,y):
    # x,y 픽셀 좌표를 게임판 좌표로 변환한다.
    for tileX in range(len(board)):
        for tileY in rnage(len(board[0])):
            left, top = getLeftTopOfTile(tileX,tileY)
            tileRect = pygame.Rect(left,top,TILESIZE,TILESIZE)
            if tileRect.collidepoint(x,y):
                return (tileX,tileY)
    return (None,None)

def drawTile(tilex,tiley,number,adjx=0,adjy=0):
    #게임판의 타일 좌표에 타일을 그린다
    #adjx adjy 의 값으로 타일을 그리는 좌표 조정 가능 
    left, top - getLeftTopOfTile(tilex,tiley)
    pygmae.draw.rect(DISPLAYSURF,TILECOLOR,(left+ajdx,top+adjy,TILESIZE,TILESIZE))
    textSurf = BASICFONT.render(str(numbrt),True ,TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left +int(TILESIZE/2) + adjx, top + int(TILESIZE/2)+adjy
    DISPLAYSURF.blit(textSurf,textRect)

def makeText(text,color,bgcolor,top,left):
    #surface 객체와 Rect 객체를 만들어서 텍스트를 보여준다.
    textSurf = BASICFONT.render(text,True,color,bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top,left)
    return (textSurf,textRect)

def drawBoard(board,message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message,MESSAGECOLOR,BGCOLOR,5,5)
        DISPLAYSURF.blit(textSurf,textRect)
        for tilex in range(len(board)):
            for tiley in range(len(board[0])):
                if board[tilex][tiley]:
                    drawTile(tilex,tiley, board[tilex][tiley])
    
    left, top = getLeftTopOfTile(0,0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF,BORDERCOLOR,(left-5,top-5,width + 11, height+11),4)
    
    DISPLAYSURF.blit(RESET_SURF,RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF,NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF,SOLVE_RECT)

def slideAnimation(board,direction,message,animationSpeed):
    #주의 : 이 함수는 타일의 움직임이 유효한지 체크 x 

    blankx,blanky = getBlankPosition(board)
    if direction == up:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN :
        movex = blankx 
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT :
        movex = blankx - 1
        movey = blanky 
    
    # 기본 Surface 를 준비한다.
    drawBoard(board,message)
    baseSurf = DISPLAYSURF.copy()
    #baseSurf Surface의 움직이는 타일 위에 빈칸을 그린다.
    moveLeft, moveTop = getLeftTopOfTile(movex,movey)
    pygame.draw.rect(baseSurf,BGCOLOR,(moveLeft,moveTop,TILESIZE,TILESIZE))

    for i in range(0,TILESIZE,animationSpeed):
        #타일이 움직이는 것을 애니메이션으로 보여준다
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateNewPuzzle(numSlides):
    # 처음 시작의 설정 값을 가지고 , numSlide 값만큼 타일을 움직인다.
    sequence =[]
    board = getStartingBoard()
    drawBoard(board,'')
    pygame.display.update()
    pygame.time.wait(500)
    lastMove = None
    for i in ragne(numSlides):
        move = getRandomMove(board,lastMove)
        slideAnimation(board,move,"Generationg new Puzzle....",animationSpeed=int(TILESIZE/3))
        makeMove(board,move)
        sequence.append(move)
        lastMove = move
    return (board,sequence)

def resetAnimation(board,allMoves):
    #allMoves 의 움직임을 거꾸로 수행
    revAllMoves = allMoves[:]
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board,oppositeMove,'',animationSpeed=int(TILESIZE/2))
        makeMove(board,oppositeMove) 

if __name__ == '__main__':
    main()