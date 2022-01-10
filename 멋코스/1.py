#거스름돈 
# coins = [500,100,50,10,1] ; cnt=0
# money= int(input()) 
# pay=1000-money

# for coin in coins:
#     cnt+=pay//coin 
#     pay%=coin 
# print(cnt)

#1931 : 회의실 배정 
# n = int(input())
# time =[]
# for i in range(n):
#     start,end = map(int,input().split())
#     time.append([start,end])

# #정렬진행 x 0,1기준 
# time.sort(key=lambda x:x[0])
# time.sort(key=lambda x:x[1])

# last=0 ; cnt=0

# for x,y in time:
#     if x>=last:
#         cnt+=1
#         last=y
# print(cnt)

# 서강근육
# import sys 
# input = sys.stdin.readline

# n = int(input())
# lost = list(map(int,input().split()))
# maxValue = 0

# lost.sort()

# if n%2==1:
#     for i in range(n//2):
#         maxValue = max(maxValue,lost[i]+lost[n-2-i])
#     maxValue=max(maxValue,lost[-1])
# else : 
#     for i in range(n//2):
#         maxValue = max(maxValue,lost[i]+lost[n-1-i])
# print(maxValue)

# 수리공항승 
# n,l = map(int,input().split())
# places = list(map(int,input().split()))
# places.sort()

# start = places[0] 
# end = places[0]+l ; cnt=1 

# for place in places:
#     if end<=place: #사이에 있지 않는 경우 
#         start = place
#         end = place+l 
#         cnt+=1 
# print(cnt)

# number = input().split("-")

# firstSum = 0 
# otherSum = 0

# for i in number[0].split("+"):
#     firstSum+=int(i)

# for i in number[1:]:
#     for j in i.split("+"):
#         otherSum+=int(j) 

# print(firstSum-otherSum)
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else :
#         return gcd(b,a%b)
# print(gcd(192,162))

# def dfs(graph,v,visted):
#     visted[v]=True 
#     print(v,end=" ")
#     for i in graph[v]:
#         if not visted[i]:
#             dfs(graph,i,visted)
# graph=[
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4]
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visted=[False]*9 
# dfs(graph,1,visted)

#BFS 
# from collections import deque 

# def bfs(graph,start,visted):
#     queue = deque([start])
#     visted[start]=True 
#     while queue:
#         v = queue.popleft()
#         print(v,end=" ")
#         for i in graph[v]:
#             if not visted[i]:
#                 queue.append(i)
#                 visted[i]=True 

# graph=[
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4]
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited=[False]*9 
# bfs(graph,1,visited)

# 얼음 
# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False 
#     if graph[x][y]==0: #0 인근 0 노드 1로 변경 
#         graph[x][y]=1 
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y-1)
#         dfs(x,y+1)
#         return True 
#     return False 


# n,m = map(int,input().split())
# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))

# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(n,m)==True:
#             cnt+=1
# print(cnt)


# 미로탈출 
from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]


n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(0,0))