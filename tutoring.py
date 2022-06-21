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

# sentence = "A picture is worth a thousand words."

# table = {"alphas": 0, "digits": 0, "spaces": 0}

# for i in sentence:
#     if i.isalpha():
#         table["alphas"] += 1
#     if i.isdigit():
#         table["digits"] += 1
#     if i.isspace():
#         table["spaces"] += 1
# print(table)

# letter = "attacktonight"
# encodeLetter = ""
# for ch in letter:
#     num = ord(ch)
#     encodeLetter += chr(num+3)

# print("PlainText : ", letter)
# print("ChiperText : ", encodeLetter)


# p = re.compile('(1|2)9*\d')
# print(p.findall("I was born in Seoul at 10 A.M. on 29th October 1992"))

# p2 = re.compile('xy*')
# print(p.findall("I was born in Seoul at 10 A.M. on 29th October 1992"))


# def find_o(search_str):
#     idx = 0
#     while:
#         idx += 1

#     retun idx


# print find_o("eeyore")
