# def fibo(x):
#     if x==1 or x==2:
#         return 1 
#     return fibo(x-1)+fibo(x-2)
# print(fibo(4))

# d = [0]*100 

# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if d[x] !=0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
# print(fibo(99))

# d = [0] * 100
# d[1] = 1 
# d[2] = 1 
# n = 99
# for i in range(3,n+1):
#     d[i] = d[i-1]+d[i-2]

# print(d[n])

# n = int(input())
# arr = list(map(int,input().split()))

# d = [0]*100 

# d[0] = arr[0]
# d[1] = max(arr[0],arr[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+arr[i]) 
# print(d[n-1])

# x = int(input())
# d=[0]*30001 

# for i in range(2,x+1):
#     d[i] = d[i-1]+1 
#     if i%2==0:
#         d[i] = min(d[i],d[i//2]+1)
#     if i%3==0:
#         d[i] = min(d[i],d[i//3]+1)
#     if i%5==0:
#         d[i] = min(d[i],d[i//5]+1)
# print(d[i])

# n,m = map(int,input().split())
# coin = []
# for _ in range(n):
#     coin.append(int(input()))

# d = [0]*10001 

# n,m = map(int,input().split())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# d = [10001] * (m+1)

# d[0] = 0 
# for i in range(n):
#     for j in range(arr[i],m+1):
#         if d[j-arr[i]] != 10001 : #만들수있는 방법 존재 
#             d[j] = min(d[j],d[j-arr[i]]+1)
# if d[m]==10001:
#     print(-1)
# else :
#     print(d[m])


#금광 
# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     arr = list(map(int,input().split()))

#     dp = []
#     idx = 0 
#     #2차원 dp테이블 초기화 
#     for i in range(n):
#         dp.append(arr[idx:idx+m])
#         idx += m 

#     for j in range(1,m):
#         for i in range(n):
#             if i==0:
#                 left_up =0 
#             else :
#                 left_up = dp[i-1][j-1]
#             if i == n-1 :
#                 left_down = 0
#             else :
#                 left_down = dp[i+1][j-1]
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up,left_down,left)
#     result = 0
#     for i in range(n):
#         result = max(result,dp[i][m-1])
#     print(result)

# n = int(input())
# arr = list(map(int,input().split()))

# arr.reverse()
# dp = [1]*n 

# #LIS 알고리즘 수행 
# for i in range(1,n):
#     for j in range(0,i):
#         if arr[j]<arr[i]:
#             dp[i] = max(dp[i],dp[j]+1)
# print(n-max(dp))



# for i in range (1,10) :
#     print()
#     for j in range (1,10) :
#         print(f"{i} X {j} = {i*j}")

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,"X",j,"=",i*j)
#     print()

#for문 작성 코드 
# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")
#     print()

# #while문 작성 코드 
# i=1
# True
# False = 0
# while 0:
#     j=1 
#     while j<10:
#         print(f"{i} X {j} = {i*j}")
#         j+=1 

#     print()
#     i+=1 


# print(bool(""))
# print(bool("abc"))
# print(bool([]))
# print(bool([1,23,4]))

# x = int(input())
# d=[0]*30001 

# for i in range(2,x+1):
#     d[i] = d[i-1]+1 
#     if i%2==0:
#         d[i] = min(d[i],d[i//2]+1)
#     if i%3==0:
#         d[i] = min(d[i],d[i//3]+1)
#     if i%5==0:
#         d[i] = min(d[i],d[i//5]+1)
# print(d[i])

# n = int(input())
# d = [0]*(n+1) 
# t=[] ; p = []
# for _ in range(n):
#     t,p = map(int,input().split())
#     tpList.append([t,p])

# for i in range(2,n+1):
#     d[i] = d[i-1]+tp

# 평범한 배낭 : 12865 
# n 물건 갯수
# k 최대무게 
# n,k = map(int,input().split())
# wvList =[[0,0]]
# dp = [[0]*(k+1) for _ in range((n+1))]

# for _ in range(n):
#     wvList.append(list(map(int,input().split())))


# #dp[n][k]는 n번째 물건까지 봤을때 무게가 k인 배낭의 최대가치 
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         w = wvList[i][0]
#         v = wvList[i][1] 

#         # 배낭 허용 무게보다 더 큰 무게를 가진아이는 넣지 않는다
#         if j<w: 
#             dp[i][j] = dp[i-1][j]
#         # 배낭허용무게보다 더 작은 무게를 가진 아이라면 ? 
#         else :
#             # 현재 넣을 무게 만큼 배낭에서 빼고 그 물건을 넣는다
#             # 물건 넣지 않고 그대로 가져간다 
#             # 둘중에 큰 가치를 가진 아이 
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v) 
# print(dp[n][k])            


# 만약 상담이 끝나는 날이 n넘어가면 ㅃㅇ 
# 그 외에는 비교 
# 현재 일할때 보상 + 현재 끝낸 다음날 보상 
# 일 안했을때 보상 

# n = int(input())

# tList = []  #time
# pList = []  #pay 
# dp = [0]*(n+1) #dp생성 

# for i in range(n): 
#     t,p = map(int,input().split())
#     tList.append(t)
#     pList.append(p)

# for i in range(n-1,-1,-1): #뒤에서 부터 검사 
#     if tList[i]+i>n: 
#         dp[i]=dp[i+1]
#     else :
#         dp[i] = max(dp[i+1],pList[i]+dp[i+tList[i]])
# print(dp[0])


# n = int(input())
# score = [0 for _ in range(301)]
# dp = [0 for _ in range(301)]

# for i in range(n):
#     score[i] = int(input())

# dp[0] = score[0]
# dp[1] = score[0] + score[1]
# dp[2] = max(score[0] + score[2],score[1]+score[2]) 

# for i in range(3,n):
#     #마지막 계딴의 전계단을 밟음
#     #마지막 계단 전계단을 안밟음 
#     dp[i] = max(dp[i-2]+score[i],dp[i-3]+score[i-1]+score[i])


#1. 계단 한개씩 또는 두개씩 
#연속 세 계단 x 
#마지막 계단 밟기 
# import sys 
# input = sys.stdin.readline
# n = int(input())

# score = [0 for _ in range(301)]
# dp = [0 for _ in range(301)]

# for i in range(n):
#     score[i] = int(input())

# #첫번째 계단 
# dp[0] = score[0]
# #두번째 계딴 
# dp[1] = score[0]+score[1]
# #세번째 계단 
# dp[2] = max(score[0]+score[2],score[1]+score[2])

# #전계단을 밟을 경우 :
# #전계단을 밟지 않을 경우 :
# for i in range(3,n):
#     dp[i] = max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])


# print(dp[n-1])


# list1 = [1,2,3]
# print(list1)
# list1[0] = 2
# print(list1)


# tuple1 = (201203,2,3)
# print(tuple1)
# tuple1[0] = 2
# print(tuple1)

# def hi(name):
#     print(f"{name}님 안녕하세요!")
#     print("반갑습니다!")

# hi("서희찬")
# hi("김민경")
# hi("양지현")

def add(a,b):
    ar = a+b 
    return ar  
print(add(3,4))
