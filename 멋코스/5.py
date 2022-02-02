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