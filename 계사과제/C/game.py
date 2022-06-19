# -*- coding: utf-8 -*-
from tkinter import *
import time

# 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.


class Sprite:
    # 생성자
    def __init__(self, image, x, y):
        self.img = image  # 스프라이트가 가지고 있는 이미지
        self.x = x		# 현재 위치의 x좌표
        self.y = y		# 현재 위치의 y좌표
        self.dx = 0		# 단위시간에 움직이는 x방향 거리
        self.dy = 0      # 단위시간에 움직이는 y방향 거리

    # 스프라이트의 가로 길이 반환
    def getWidth(self):
        return self.img.width()

    # 스프라이트의 세로 길이 반환
    def getHeight(self):
        return self.img.height()

    # 스프라이트를 화면에 그리기
    def draw(self, g):
        g.create_image(self.x, self.y, anchor=NW, image=self.img)

    # 스프라이트를 움직이는 메소드
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # dx를 설정하는 설정자 메소드
    def setDx(self, dx):
        self.dx = dx

    # dy를 설정하는 설정자 메소드
    def setDy(self, dy):
        self.dy = dy

    # dx를 반환하는 접근자 메소드
    def getDx(self):
        return self.dx

    # dy를 반환하는 접근자 메소드
    def getDy(self):
        return self.dy

    # x를 반환하는 접근자 메소드
    def getX(self):
        return self.x

    # y를 반환하는 접근자 메소드
    def getY(self):
        return self.y

    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.
    # 3장의 Lab 문제를 참조한다.
    def checkCollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x+self.getWidth()
        p2y = self.y+self.getHeight()
        p3x = other.x
        p3y = other.y
        p4x = other.x+other.getWidth()
        p4y = other.y+other.getHeight()

        overlapped = not(p4x < p2x or
                         p3x > p2x or
                         p2y < p3y or
                         p1y > p4y)
        return overlapped

    # 충돌을 처리한다. 현재는 아무 일도 하지 않는다. 자식 클래스에서 오버라이드된다.
    def handleCollision(self, other):
        pass
# 우리의 우주선을 나타내는 클래스


class StarShipSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 0

    # 우주선을 움직인다. 만약 윈도우의 경계를 넘으려고 하면 움직이지 않는다.
    def move(self):
        if ((self.dx < 0) and (self.x < 10)):
            return
        if ((self.dx > 0) and (self.x > 800)):
            return
        super().move()
        self.dx = 0

    # 충돌을 처리한다. 외계인 우주선과 충돌하면 게임이 종료된다.
    def handleCollision(self, other):
        if type(other) is AlienSprite:
            self.game.endGame()

# 외계인 우주선을 나타내는 클래스


class AlienSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -10		# x 방향으로만 움직인다.

    # 외계인 우주선을 움직이는 메소드
    # 윈도우에 경계에 도달하면 한칸 아래로 이동한다.
    def move(self):
        if (((self.dx < 0) and (self.x < 10)) or ((self.dx > 0) and (self.x > 750))):
            self.dx = -self.dx
            self.y += 50
            if (self.y > 600):
                game.endGame()
        super().move()
# 포탄을 나타내는 클래스


class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dy = -20

    # 화면을 벗어나면 객체를 리스트에서 삭제한다.
    def move(self):
        super().move()
        if (self.y < -100):
            self.game.removeSprite(self)

    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다.
    def handleCollision(self, other):
        if type(other) is AlienSprite:
            self.game.removeSprite(self)
            self.game.removeSprite(other)

# 게임을 나타내는 클래스


class GalagaGame():

    # 왼쪽 화살표 키 이벤트를 처리하는 함수
    def keyLeft(self, event):
        self.starship.setDx(-10)
        return

    # 오른쪽 화살표 키 이벤트를 처리하는 함수
    def keyRight(self, event):
        self.starship.setDx(+10)
        return

    # 스페이스 키 이벤트를 처리하는 함수
    def keySpace(self, event):
        self.fire()
        return

    # 게임에 필요한 스프라이트를 생성하는 메소드
    def initSprites(self):
        self.starship = StarShipSprite(self, self.shipImage, 370, 550)
        self.sprites.append(self.starship)
        for y in range(0, 2):
            for x in range(0, 12):
                alien = AlienSprite(self, self.alienImage,
                                    100 + (x * 50), (50) + y * 30)
                self.sprites.append(alien)

    # 생성자 메소드
    def __init__(self, master):
        self.master = master
        self.sprites = []
        self.canvas = Canvas(master, width=800, height=600)
        self.canvas.pack()
        self.shotImage = PhotoImage(
            file="/Users/seochan/Documents/GitHub/python_system/계사과제/C/fire.png")
        self.shipImage = PhotoImage(
            file="/Users/seochan/Documents/GitHub/python_system/계사과제/C/starship.png")
        self.alienImage = PhotoImage(
            file="/Users/seochan/Documents/GitHub/python_system/계사과제/C/alien.png")
        self.running = True
        self.initSprites()
        master.bind("<Left>",  self.keyLeft)
        master.bind("<Right>", self.keyRight)
        master.bind("<space>", self.keySpace)

    # 게임을 시작하는 메소드
    def startGame(self):
        self.sprites.clear()
        initSprites()

    # 게임을 종료하는 메소드
    def endGame(self):
        self.running = False
        pass

    # 스프라이트를 리시트에서 삭제한다.
    def removeSprite(self, sprite):
        if(sprite in self.sprites):
            self.sprites.remove(sprite)
            del sprite

    # 포탄을 발사하는 메소드
    def fire(self):
        shot = ShotSprite(self, self.shotImage,
                          self.starship.getX() + 10,	self.starship.getY() - 30)
        self.sprites.append(shot)

    # 화면을 그리는 메소드
    def paint(self, g):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 600, fill="black")
        for sprite in self.sprites:
            sprite.draw(self.canvas)

    # 게임 루프
    def gameLoop(self):
        for sprite in self.sprites:
            sprite.move()

        # 스프라이트 리스트 안의 객체끼리의 충돌을 검사한다.
        for me in self.sprites:
            for other in self.sprites:
                if me != other:
                    if (me.checkCollision(other)):
                        me.handleCollision(other)
                        other.handleCollision(me)
        self.paint(self.canvas)
        if(self.running):
            self.master.after(10, self.gameLoop)


root = Tk()
g = GalagaGame(root)
root.after(10, g.gameLoop())
root.mainloop()
