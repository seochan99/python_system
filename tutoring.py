# 계산기

print("---계산기---")
print("1. 더하기")
print("2. 빼기")
print("3. 니누기")
print("4. 곱하기")
print("5. 나머지")
print("----------")

choice = int(input("선택지를 입력해주세요 : "))
num1, num2 = map(int, input("정수 두개를 입력해주세요 : ").split())

if choice == 1:
    print(f"더하기 값 : {num1+num2}")
elif choice == 2:
    print(f"빼기 값 : {num1-num2}")
elif choice == 3:
    print(f"나누기 값 : {num1//num2}")
elif choice == 4:
    print(f"곱하기 값 : {num1*num2}")
elif choice == 5:
    print(f"나머지 값 : {num1%num2}")
else:
    print("1~5사이의 숫자를 입력해주세요.")

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
