import re

# 계산기

# print("---계산기---")
# print("1. 더하기")
# print("2. 빼기")
# print("3. 니누기")
# print("4. 곱하기")
# print("5. 나머지")
# print("----------")

# num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())
# choice = int(input("선택지를 입력해주세요 : "))

# if choice == 1:
#     print(f"더하기 값 : {num1+num2}")
# elif choice == 2:
#     print(f"빼기 값 : {num1-num2}")
# elif choice == 3:
#     print(f"나누기 값 : {num1//num2}")
# elif choice == 4:
#     print(f"곱하기 값 : {num1*num2}")
# elif choice == 5:
#     print(f"나머지 값 : {num1%num2}")
# else:
#     print("1~5사이의 숫자를 입력해주세요.")

# val = 5
# while val > 0:
#     print(val)
#     # 탈출 조건을 무조건 작성해줘야한다!
#     val -= 1

# for _ in range(5):
#     print(val)
#     val -= 1

# 추가
# from asyncio.sslproto import _DO_HANDSHAKE
# from tkinter import DISABLED
# from numpy import blackman


# color = ["red", "blue", "black"]

# print(color)
# append : 덧붙인다
# color.append("white")

# extend :확장
# color.extend(["orange", "green"])

# insert : 삽입
# color.insert(1, "white")

# 2번 : red white blue black


# 삭제
# remove
# color.remove("black")

# del
# del color[-1]

# print(color)

# a = [1, 5, 3, 4, 2]

# print(a)

# index
# print(a.index(2))

# count
# print(a.count(2))

# merge sort

# sort
# a.sort(reverse=True)

# a.reverse()

# print(a)

# val = int(input("숫자를 입력해주세요 : "))

# if 5 < val <= 10:
#     print("5보다 크고 10보다 작습니다.")
# elif 3 < val <= 5:
#     print("5보다 작고 3보다 큽니다.")
# else:
#     print("3보다작습니다.")

# val = 5

# while val > 0:
#     print(val)
#     val -= 1

# for i in range(1, 10):
#     print()
# 0 : False
# 1 2 3 ... : True

# def menu():
#     print("---계산기---")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 나누기")
#     print("4. 곱하기")
#     print("5. 나머지")
#     print("6. 종료")
#     print("----------")


# def adder(num1, num2):
#     return num1+num2


# def sub(num1, num2):
#     return num1-num2


# def div(num1, num2):
#     return num1//num2


# def mul(num1, num2):
#     return num1*num2


# def rest(num1, num2):
#     return num1 % num2


# while True:
#     menu()
#     num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())
#     choice = int(input("선택지를 입력해주세요 : "))

#     if choice == 1:
#         print(f"더하기 값 : {adder(num1, num2)}")
#     elif choice == 2:
#         print(f"빼기 값 : {sub(num1, num2)}")
#     elif choice == 3:
#         print(f"나누기 값 : {div(num1, num2)}")
#     elif choice == 4:
#         print(f"곱하기 값 : {mul(num1, num2)}")
#     elif choice == 5:
#         print(f"나머지 값 : {rest(num1, num2)}")
#     elif choice == 6:
#         print("프로그램을 종료합니다.")
#         break
#     else:
#         print("1~5사이의 숫자를 입력해주세요.")

# while True:

#     print("---계산기---")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 나누기")
#     print("4. 곱하기")
#     print("5. 나머지")
#     print("6. 종료")
#     print("----------")

#     num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())
#     choice = int(input("선택지를 입력해주세요 : "))
#     if choice == 1:
#         print(f"더하기 값 : {num1+num2}")
#     elif choice == 2:
#         print(f"빼기 값 : {num1-num2}")
#     elif choice == 3:
#         print(f"나누기 값 : {num1//num2}")
#     elif choice == 4:
#         print(f"곱하기 값 : {num1*num2}")
#     elif choice == 5:
#         print(f"나머지 값 : {num1%num2}")
#     elif choice == 6:
#         print("프로그램을 종료합니다.")
#     else:
#         print("1~5사이의 숫자를 입력해주세요.")


# # 1
# def adder(num1, num2):
#     return num1+num2


# def sub(num1, num2):
#     return num1-num2


# def div(num1, num2):
#     return num1//num2


# def mul(num1, num2):
#     return num1*num2


# def rest(num1, num2):
#     return num1 % num2


# def menu(choice):
#     if choice == 1:
#         print(f"더하기 값 : {adder(num1, num2)}")
#     elif choice == 2:
#         print(f"빼기 값 : {sub(num1, num2)}")
#     elif choice == 3:
#         print(f"나누기 값 : {div(num1, num2)}")
#     elif choice == 4:
#         print(f"곱하기 값 : {mul(num1, num2)}")
#     elif choice == 5:
#         print(f"나머지 값 : {rest(num1, num2)}")
#     else:
#         print("잘못된 값을 입력하셨씁니다.")


# while True:
#     print("---계산기---")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 나누기")
#     print("4. 곱하기")
#     print("5. 나머지")
#     print("6. 종료")
#     print("----------")
#     num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())
#     choice = int(input("선택지를 입력해주세요 : "))
#     menu(choice)


# 2
# while True:
#     print("---계산기---")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 나누기")
#     print("4. 곱하기")
#     print("5. 나머지")
#     print("6. 종료")
#     print("----------")


# def adder(num1, num2, choice):
#     num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())
#     choice = int(input("선택지를 입력해주세요 : "))
#     if choice == 1:
#         print(f"더하기 값 : {num1+num2}")
#     elif choice == 2:
#         print(f"빼기 값 : {num1-num2}")
#     elif choice == 3:
#         print(f"나누기 값 : {num1//num2}")
#     elif choice == 4:
#         print(f"곱하기 값 : {num1*num2}")
#     elif choice == 5:
#         print(f"나머지 값 : {num1%num2}")
#     elif choice == 6:
#         print("프로그램을 종료합니다.")
#     else:
#         print("1~5사이의 숫자를 입력해주세요.")
#     return


# print(adder)


# for 구구단
# for j in range(1, 10):
#     for i in range(1, 10):
#         print(f"{j} x {i} = {j*i}")
#     print()

# # while 구구단
# val = 1
# while val < 10:
#     val2 = 1
#     while val2 < 10:
#         print(f"{val} x {val2} = {val2*val}")
#         val2 += 1
#     print()
#     val += 1

# arr1 = [1, 2, 3]
# tu = (1, 2, 3)

# print(arr1)
# print(tu)

# arr1[2] = 5
# tu[1] = 5

# print(arr1)
# print(tu)

# friends = [["동수", 13123], ["희찬", 123123], ["찬", 3132]]

# for i in range(3):
#     print(friends[i][0])

# print(list(range(10, 2, -1)))
# p


n = int(input())

han = 0

# for i in range(1, n + 1):
#     if i < 100:
#         han += 1
#     else:
#         ns = list(map(int, str(i)))
#         print(ns)
#         if ns[0] - ns[1] == ns[1] - ns[2]:
#             han += 1
# print(han)
