# ## 프로그래머스 level 1 : x만큼 간격

# # #내풀이
# # def solution(x,n):
# #     answer = []
# #     for i in range(n):
# #         answer.append(x*(i+1))
# #     return answer

# # #다른사람풀이
# # def solution(x,n):
# #     return [i*x+x for i in range(n)]

# # 핸드폰 번호 가리기

# # def solution(phone_number):
# #     return "*"*(len(phone_number)-4) + phone_number[-4:]

# # print(solution("01023624076"))

# #행렬의 덧셈
# # def solution(arr1, arr2):
# #     answer = [[]]
# #     answer.append(arr1[0]+arr2[0])
# #     return answer

# # num1,num2 = map(int,input().split())
# # print("덧셈 :",num1+num2)
# # print("뺄셈 :",num1-num2,"이것은 뺄셈입니다.")
# # print(f"뺄셈 : {num1-num2} 이것은 뺄셈입니다. ")
# # print("곱셈 :",num1*num2)
# # print("나눗셈 :",num1//num2)
# # print("나머지 :",num1%num2)


# #문자열 압축

# # def solution(arr):
# #     ans = len(arr)  # 처음 길이
# #     for step in range(1,len(arr)//2+1): #문자열 길이의 절반만큼만 잘라서 확인 ! 그 이후부터는 잘라도 다음 조각이 없음
# #         com = "" #빈문자열
# #         comArr = arr[0:step]
# #         cnt = 1
# #         for j in range(step,len(arr),step):
# #             if comArr == arr[j:j+step]: #문자열이 동일하다면
# #                 cnt+=1
# #             else: #다른 문자열 나오면 com완성하고 상태초기화
# #                 com += str(cnt) + comArr if cnt>=2 else comArr #2이상일때마다, 1은 생략하니깐 !
# #                 comArr = arr[j:j+step]
# #                 cnt = 1  #
# #         #남아 있는 문자열 붙이기
# #         com += str(cnt)+ comArr if cnt>=2 else comArr
# #         ans = min(ans,len(com))
# #     return ans
# # arr = input()

# # print(solution(arr))

# #자물쇠..
# #완전 탐색

# #matrix 90도 회전 함수
# # def rotate_90(a):
# #     n = len(a)
# #     m = len(a[0])
# #     result = [[0]*n for _ in range(m)]
# #     for i in range(n):
# #         for j in range(m):
# #             result[j][n-i-1] = a[i][j]
# #     return result
# # #모두 1인지 확인 함수
# # def check(new_lock):
# #     lock_length = len(new_lock) // 3
# #     for i in range(lock_length,lock_length * 2):
# #         for j in range(lock_length,lock_length*2):
# #             if new_lock[i][j] != 1:
# #                 return False
# #     return True
# # def solution(key,lock):
# #     n = len(lock)
# #     m = len(key)
# #     new_lock = [[0]*(n*3) for _ in range(n*3)] #새로운 매트릭스 생성
# #     #새 매트릭스 가운데 넣기
# #     for i in range(n):
# #         for j in range(m):
# #             new_lock[i+n][j+n] = lock[i][j]

# #     for rotation in range(4):
# #         key = rotate_90(key)
# #         for x in range(n*2):
# #             for y in range(n*2):
# #                 for i in range(m):
# #                     for j in range(m):
# #                         #열쇠 넣기
# #                         new_lock[x+i][y+j]+=key[i][j]
# #                 #확인하기
# #                 if check(new_lock) == True :
# #                     return True
# #                 # False 이면 열쇠다시빼기
# #                 for i in range(m):
# #                     for j in range(m):
# #                         new_lock[x+i][y+j] -= key[i][j]
# #     return False

# #3190 : 뱀
# # from collections import deque

# # #상 우 하 좌
# # dy = [-1,0,1,0]
# # dx = [0,1,0,-1]
# # def change(direct,c):
# #     # 상 0
# #     # 우 1
# #     # 하 2
# #     # 좌 3
# #     # 시계방향 회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
# #     # 반시꼐 방향 회전 : 상(0) -> 좌(3) ...
# #     if c == "L":
# #         direct = (direct - 1) % 4
# #     else :
# #         direct = (direct + 1) % 4
# #     return direct

# # def start():
# #     direct = 1 #초기 방향
# #     time = 1 #게임시간
# #     y,x = 0,0 #초기 뱀 위치
# #     visted = deque([[y,x]])
# #     matrix[y][x] = 2
# #     while True :
# #         y,x = y+dy[direct], x+dx[direct]
# #         if 0<=y<n and 0<=x<n and matrix[y][x] != 2:
# #             if not matrix[y][x] == 1: #apple X
# #                 temp_y,temp_x = visted.popleft()
# #                 matrix[temp_y][temp_x] = 0 # del tail
# #             matrix[y][x] = 2
# #             visted.append([y,x])
# #             if time in times.keys(): #시간초에 도달하면
# #                 direct = change(direct,times[time]) #방향과 바꿔야하는 방향 전달
# #             time += 1
# #         else : #벽에 부딪힘 ㅜㅜ
# #             return time


# # n = int(input()) #보드크기
# # k = int(input()) #사과 개수

# # matrix = [[0]*n for _ in range(n)]
# # kXY =[]
# # for _ in range(k):
# #     x,y = map(int,input().split())
# #     matrix[x-1][y-1] = 1 #save apple

# # l = int(input()) #방향전환

# # times = {}

# # for _ in range(l):
# #     x,c = input().split()
# #     times[int(x)] = c

# # print(start())

# # def search_binary(list, value):
# #     low = 0
# #     high = len(list)-1

# #     while low <= high:
# #         middle = (low+high)//2
# #         print(f"low : {low}  middle : {middle} high : {high} list[middle] : {list[middle]}")

# #         if list[middle] > value:
# #             high = middle-1
# #         elif list[middle] < value:
# #             low = middle+1
# #         else:
# #             return middle
# #     return -1

# # myList = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
# # print("인덱스=", search_binary(myList, 34))

# # from random import *
# # from math import sqrt

# # n = int(input("반복횟수를 입력하시오 : "))

# # inside = 0
# # for i in range(0,n):
# #     x = random() # 0~1.0
# #     y = random()
# #     if sqrt(x*x+y*y)<=1: # 거리 1.0이하
# #         # print(f"x : {x} y : {y} 는 원 내부의 점 입니다.")
# #         inside+=1
# #     # else :
# #         # print(f"x : {x} y : {y} 는 원 외부의 점 입니다.")
# # pi = 4 * inside / n
# # print(f"inside : {inside} / n : {n}")
# # print(pi)

# # print( 5/10 *4)

# # # from random import *
# # # from math import sqrt

# # # n = int(input("반복횟수를 입력하시오: "))
# # # # n은 전체 점의 개수이다.

# # # inside=0
# # # for i in range(0, n):
# # #     x=random()
# # #     y=random()
# # #     if sqrt(x*x+y*y)<=1:
# # #         inside+=1
# # # pi=4*inside/n
# # # print( pi)

# maze = {
#     '00' : ['01','10'],
#     '01' : ['00','02'],
#     '02' : ['01','12'],
#     '03' : ['04','13'],
#     '04' : ['03','05'],
#     '05' : ['04','15'],
#     '06' : ['16','07'],
#     '07' : ['06','08'],
#     '08' : ['07','09'],
#     '09' : ['08','19'],
#     '10' : ['00','20'],
#     '11' : ['12'],
#     '12' : ['11','02'],
#     '13' : ['03','14'],
#     '14' : ['13','24'],
#     '15' : ['05','16'],
#     '16' : ['06','15','26'],
#     '17' : ['27'],
#     '18' : ['19','28'],
#     '19' : ['09','18'],
#     '20' : ['10','21'],
#     '21' : ['20','31'],
#     '22' : ['23','32'],
#     '23' : ['22'],
#     '24' : ['14','25','34'],
#     '25' : ['24','35'],
#     '26' : ['16','27'],
#     '27' : ['17'],
#     '28' : ['18','38'],
#     '29' : ['39'],
#     '30' : ['31','40'],
#     '31' : ['30','32'],
#     '32' : ['22','31'],
#     '33' : ['34','43'],
#     '34' : ['24','33','44'],
#     '35' : ['25','36'],
#     '36' : ['35'],
#     '37' : ['38','47'],
#     '38' : ['28','37','39'],
#     '39' : ['29','38'],
#     '40' : ['30','41'],
#     '41' : ['40','42'],
#     '42' : ['41','43'],
#     '43' : ['33','42'],
#     '44' : ['34','45'],
#     '45' : ['44'],
#     '46' : ['47'],
#     '47' : ['37','46','48'],
#     '48' : ['47','49'],
#     '49' : ['48'],
# }

# a = 5
# b = 3
# result = a+b

# print(f"더하기 결과는 : {a+b}")

# print("빼기 결과는 : ", a-b)

# print(f"곱하기 결과는 : {a*b}")

# print(f"/ 나누기 결과는 : {a/b}")
# print(f"// 나누기 결과는 : {a//b}")

# print(f"나머지 결과는 :{a%b}")

# print(f"제곱 결과는 : {a**2}")

from ast import Or
from cmath import pi


a = 4
b = 6

# 비교연산자
# a랑 b비교 출력 코드
# == : 동일한가?
# != : 동일하지않는가?
# >= <= < >
# print(a >= b)
# print(a >= b)
# print(a <= b)

# 할당연산자
# a = a + 1
# a++
# ++a
# a+=1
# a /= 1

# 논리연산자
# a = True
# b = False
# AND : and
# &&
# OR : or
# ||

# print(a and b)
# print(a or b)

# \n : 개행
# \t : 탭


# print("hello", "world", "world", "world",
#       "world", "world", "world", end=" ", sep="#")


# 산술연산자


# print("더하기 계산 결과의 값은 : ", a+b)

# print("빼기 계산 결과의 값은 : ", a-b)

# print("곱하기 계산 결과의 값은 : ", a*b)

# # print("나누기 계산 결과의 값은 : ",a/b)
# print("나누기 계산 결과의 값은 : ", a//b)

# print("나머지 계산 결과의 값은 : ", a % b)

# 비교연산자
# ==
# !=
# print(a != b)

# 할당연산자
# a = a + b
# a += b
# print(a)


# AND : 모두 참인 경우에만 참
# &&
# OR : 모두 거짓인 경우멘 거짓
# ||
# NOT : 참->거짓, 거짓->참
# a = 4
# b = 7

# print(a <= b)
# # =<
# # <=

# print(a >= b)

# 0 : False
# 1,2,3,4,5 : True


# print(bool(not a))

# in, not in
# a = [1, 3, 5, 6]
# b = 4 in a
# print(b)

# a = 8
# b = 4
# c = a & b
# d = a ^ b
# print(c)
# print(d)

# identity
# is, is not
# a = "sdsad"
# b = a
# print(2 is not a)

# \n : 개행
# \t : 탭 띄우기
# name = "chan"
# \\
# "
# '
# \t
# print("good", name, "morning")
# print(f"good {name} morning")
