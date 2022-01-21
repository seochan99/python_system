# #선택 정렬 
# from cmath import pi
# import imp
# from re import L
# import re
# import sys


# arr = [7,5,9,0,3,1,6,2,4,8]

# for i in range(len(arr)):
#     min_index = i 
#     for j in range(i +1,len(arr)):
#         if arr[min_index]>arr[j]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index],arr[i] #swap
# print(arr)

# 삽입 정렬 
# for i in range(1,len(arr)):
#     for j in range(i,0,-1): 
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#         else :
#             break 
# print(arr)

#퀵 정렬 
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr 
#     pivot = arr[0]
#     tail = arr[1:] 

#     left_side = [x for x in tail if x<= pivot]
#     right_side = [x for x in tail if x>pivot]

#     return quick_sort(left_side)+[pivot]+quick_sort(right_side)
# print(quick_sort(arr))


# 계수 정렬 
# count = [0] * (max(arr)+1)
# for i in range(len(arr)):
#     count[arr[i]]+=1 

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i,end=" ")

# 두 배열의 원소 교체 
# n,k = map(int,input().split())
# a= list(map(int,input().split()))
# b= list(map(int,input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i]<b[i]:
#         a[i],b[i] = b[i],a[i] #두 변수 스왑스킬 
#     else :
#         break 
# print(sum(a))


# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n,m = map(int,input().split()) ; cnt=0 

#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     a.sort(reverse=True)
#     b.sort()
#     for i in a:
#         for j in b:
#             if i>j:
#                 cnt+=1 
#             else :
#                 break 

#     print(cnt)

# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**4) 

# #이분탐색 
# def bsr(target,start,end,data): #
#     if start>end:
#         return None
#     mid = (start+end)//2
#     if data[mid]==target:
#         del data[mid]
#         return 1
#     elif data[mid]>target:
#         end = mid - 1
#     else : #data[mid]<target
#         start = mid + 1 
#     return bsr(target,start,end,data)

# n = int(input()) #상근 카드 갯수 
# arr1 = list(map(int,input().split()))

# m = int(input()) #엠
# arr2 = list(map(int,input().split()))

# #상근이가 가지고 있으면 1 아니면 0 출력 
# arr1.sort()
# for i in range(m):
#     if bsr(arr2[i],0,n-1,arr1):
#         print(1,end=" ")
#     else :
#         print(0,end=" ")


# ko = int(input("국어 점수를 입력하세요."))
# math = int(input("수학 점수를 입력하세요."))
# en = int(input("영어 점수를 입력하세요."))

# avg = (ko+math+en)//3 
# if 90<=avg<=100:
#     print("A")
# elif 80<=avg<90:
#     print("B")
# elif 70<=avg<80:
#     print("C")
# elif 60<=avg<70:
#     print("D")
# else:
#     print("F")

# korean = int(input("국어 점수를 입력하세요:"))
# math = int(input("수학 점수를 입력하세요:"))
# english = int(input("영어 점수를 입력하세요:"))
# total = korean + math + english
# avg = total//3

# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# elif avg >= 60:
#     print("D")
# else:
#     print("F")


# score1 = int(input("국어 점수를 입력하세요. "))
# score2 = int(input("수학 점수를 입력하세요. "))
# score3 = int(input("영어 점수를 입력하세요. "))

# average = (score1+score2+score3)/3

# if 90<=average<=100:
#     print("A등급")
# elif(average >= 80) and(average<= 90) :
#     print("B등급")
# elif(average >= 70) and(average<= 80) :
#     print("C등급")
# elif(average >= 60) and(average<= 70) :
#     print("D등급")
# else :
#     print("F등급")

# print("숫자 두개를 입력하세요")
# num1,num2 = map(int,input().split())

# print("----------계산기----------")
# print("1. 더하기")
# print("2. 빼기")
# print("3. 나누기")
# print("4. 곱하기")
# print("5. 나머지")
# print("----원하는 연산의 번호를 선택해주세요----")
# choice = int(input())

# if choice==1:
#     print("더하기 :",num1+num2)
# elif choice==2:
#     print("빼기 : ",num1-num2)
# elif choice==3:
#     print("나누기 : ", num1//num2)
# elif choice==4:
#     print("곱하기 : ", num1*num2)
# elif choice==5:
#     print("나머지 :",num1%num2)
# else:
#     print("잘못된 번호를 입력하셨습니다.")



# option = int(input("1:더하기, 2:빼기, 3:나누기, 4:곱하기, 5:나머지"))
# # num1 = int(input()) ;num2 = int(input())
# num1,num2 = map(int,input().split())
# if option == 1:
#     print(num1 + num2)
# elif option ==2:
#     print(num1 - num2)
# elif option ==3:
#     print(num1 // num2)
# elif option ==4:
#     print(num1 * num2)
# elif option ==5:
#     print(num1 % num2)
# else:
#     print("프로그램이 종료되었습니다.")


# print("1번 : 덧셈, 2번 : 뺼셈, 3번 곱셈, 4번 나눗셈, 5번 나머지")
# print("숫자 2개와 원하는 프로그램 적으시오.")
# num1, num2, menu = map(int,input().split())
# if menu == 1 :
#     print("덧셈 : " + (num1+num2))
# elif menu == 2 :
#     print("뺼셈 : " + (num1-num2))
# elif menu == 3 :
#     print("곱셈 : " + (num1*num2)) 
# elif menu == 4 :
#     print("나눗셈 : " + (num1/num2))
# elif menu == 5 :
#     print("나머지 : " + (num1%num2))
# else :
#     print("잘못된 프로그램 선택입니다.")

# year = int(input())
# if (year%4==0 and year//100!=0) or (year//400==0):
#     print(1)
# else :
#     print(0)

# year = int(input())
# if (year%4==0 and year%100 != 0) or (year %400 == 0) :
#     print("1")
# else :
#     print("0")

# year = int(input())
# if (year%4 == 0 and year%100!= 0) or (year%400==0):
#     print(1)
# else:
#     print(0)


#1413 : 시리얼 번호 

#길이 짧은게 먼저 
#길이 같으면 숫자의 합 중 작은 것이 먼저 
#숫자마져 같으면 사전 순 

# import sys 
# input = sys.stdin.readline

# n = int(input())
# codes = [0 for _ in range(n)]

# def total(code):
#     score=0
#     for x in code:
#         if x.isdigit():
#             score+=int(x)
#     return score
            
            
# for i in range(n):
#     codes[i]  = input().rstrip() #시리얼번호 입력받기 

# codes.sort(key = lambda x:(len(x),total(x),x))#길이,합,사전순

# for code in codes:
#     print(code)

# def total(code):
#     score=0
#     for x in code:
#         if x.isdigit():
#             score+=int(x)
#     return score


# n = int(input())
# codes = [0 for _ in range(n)]
# for i in range(n):
#     codes[i] = input()

# codes.sort(key=lambda x:(len(x),total(x),x))

# for code in codes:
#     print(code)

#1181 
# n = int(input())
# word = []
# for _ in range(n):
#     word.append(input())

# word = list(set(word)) #집합으로 중복제것 스킬 

# word.sort(key=lambda x:(len(x),x))
# for words in word:
#     print(words)

# # 2910 : 빈도정렬
# n,c = map(int,input().split()) #메세지 길이,최대수 

# arr = list(map(int,list(input().split()))) #수열을 받는다 
# cnt = {} ; idx = 1 
# for i in range(n):

# n = int(input())
# age =[]
# for i in range(n):
#     age.append(list(input().split()))
# age.sort(key = lambda x:int(x[0]))
# for i in range(n):
#     print(' '.join(age[i]))
#빈도, 들어온 순서 
n,c = map(int,input().split())
arr = list(map(int,input().split()))

bindo = {} #빈도, 처음 등장위치 

for i in range(n):
    if arr[i] in bindo:
        bindo[arr[i]][0]+=1 
    else :
        bindo[arr[i]]=[1,i] #빈도,위치 

sortBindo = sorted(bindo.items(),key = lambda x : (-x[1][0],x[1][1]))

result = []
for i in sortBindo:
    for j in range(i[1][0]):
        result.append(str(i[0]))
print(" ".join(result))
