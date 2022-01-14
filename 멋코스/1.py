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
# from collections import deque 

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue=deque()
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             cx = x + dx[i]
#             cy = y + dy[i]

#             if cx<0 or cx>=n or cy<0 or cy>=m or graph[cx][cy]==0:
#                 continue
#             if graph[cx][cy] ==1:
#                 graph[cx][cy]=graph[x][y]+1 
#                 queue.append((cx,cy))
#     return graph[n-1][m-1]

# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

# print(bfs(0,0))

# n=1260 
# cnt =0 
# arr = [500,100,50,10]

# for coin in arr:
#     cnt+=n//coin
#     n%=coin 
# print(cnt)

# n,k = map(int,input().split())

# result = 0
# while True:
#     target = (n//k)*k
#     result += (n-target)
#     n = target 
#     if n<k:
#         break 
#     result+=1
#     n//=k 
# result+=(n-1)
# print(result)

#곱 하 혹ㅡㄴ 더기 
# data = input()

# result = int(data[0])
# for i in range(1,len(data)):
#     num = int(data[i])
#     if num<=1 or result<=1:
#         result+=num 
#     else :
#         result *= num 
# print(result)

#모험가 길드 
# n= int(input())
# data = list(map(int,input().split()))
# data.sort()

# result = 0
# cnt = 0
# for i in data:
#     cnt+=1
#     if cnt>=i:
#         result+=1
#         cnt=0 
# print(result)

#1080 : 행렬 
# cnt=0
# n,m = map(int,input().split())
# matrixA = [list(map(int,list(input()))) for _ in range(n)]
# matrixB = [list(map(int,list(input()))) for _ in range(n)]

# def change(x,y):
#     for i in range(x,x+3):
#         for j in range(y,y+3):
#             matrixA[i][j]=1-matrixA[i][j] #1->0 0->1 skill 

# def check():
#     for i in range(n):
#         for j in range(m):
#             if matrixA[i][j]!=matrixB[i][j]:
#                 return False 
#     return True 

# for i in range(n-2):
#     for j in range(m-2):
#         if matrixA[i][j] != matrixB[i][j]:
#             change(i,j)
#             cnt+=1 
# if check():
#     print(cnt)
# else:
#     print(-1)

######## DFS&BFS 


#2606 : 바이러스
#컴퓨터의 수 
# n = int(input())

# #컴퓨터의 쌍 
# m = int(input())

# def dfs(v):
#     global cnt 
#     visted[v] = 1
#     for i in range(1,n+1):
#         if visted[i]==0 and graph[v][i]==1: #방문여부와 graph[v]와 연결된 선 모두 찾기 
#             dfs(i)
#             cnt+=1 #cnt추가 

# #그래프 
# graph = [[0]*(n+1) for _ in range(n+1)] #우선, 0으로 초기화 
# visted=[0 for _ in range(n+1)] #방문 체크 감염시 -> 1로변경  
# cnt = 0

# print(graph)
# print(visted)

# #default 1번 컴퓨터가 웜바이러스 걸려있음 
# #1번을 통해서 걸리게 되는것들 

# for _ in range(m):
#     x,y = map(int,input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1 

# dfs(1) #1부터 시작 


#1260 : DFS BFS 

# n : 정점 
# m : 간선 
# v : 탐색 시작할 정점의 번호 
# from collections import deque
# import sys 
# input = sys.stdin.readline

# n,m,v = map(int,input().split())

# matrix = [[0]*(n+1) for _ in range(n+1)]
# visted = [0 for _ in range(n+1)]

# #BFS 
# def bfs(v):
#     queue = deque() 
#     queue.append(v)
#     visted[v]=0 
#     while(queue):
#         v = queue[0]
#         print(queue.popleft(),end=" ")

#         for i in range(1,n+1):
#             if visted[i]==1 and matrix[v][i]==1:
#                 queue.append(i)
#                 visted[i]=0 


# #DFS 
# def dfs(v):
#     print(v,end=" ")
#     visted[v]=1 
#     for i in range(1,n+1):
#         if visted[i]==0 and matrix[v][i]==1:
#             dfs(i)

# for _ in range(m):
#     x,y = map(int,input().split())
#     matrix[x][y]=1 
#     matrix[y][x]=1  #표시 

# dfs(v)
# print()
# bfs(v)

#dfs 
#bfs 
# import sys 
# input = sys.stdin.readline
# from collections import deque

# def bfs(v):
#     queue = deque()
#     queue.append(v)
#     visted[v] == 0 

#     while queue:
#         v = queue[0]
#         print(queue.popleft(),end=" ")
#         for i in range(n+1):
#             if visted[i]==1 and matrix[v][i]==1:
#                 queue.append(i)
#                 visted[i]=0 



# def dfs(v):
#     print(v,end=" ")
#     visted[v]=1 
#     for i in range(1,n+1):
#         if visted[i]==0 and matrix[v][i]==1:
#             dfs(i)


# n,m,v = map(int,input().split())
# matrix = [[0]*(n+1) for _ in range(n+1)]
# visted = [0 for _ in range(n+1)]

# for _ in range(m):
#     x,y = map(int,input().split())
#     matrix[x][y] = 1
#     matrix[y][x] = 1

# dfs(v)
# print() 
# bfs(v)


#2178 : 미로 
# from collections import deque
# n,m = map(int,input().split())
# matrix = [list(map(int,list(input()))) for _ in range(n)] #크으.. 

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(x,y):
#     queue = deque()
#     queue.append([0,0])
#     while queue:
#         a,b = queue.popleft()
#         for i in range(4):
#             cx = a+dx[i]
#             cy = b+dy[i]
#             if 0<=cx<n and 0<=cy<m and matrix[cx][cy]==1:
#                 matrix[cx][cy] = matrix[a][b]+1 
#                 queue.append([cx,cy])

# bfs(0,0)
# print(matrix[n-1][m-1])
# from collections import deque
# n,m = map(int,input().split())
# matrix = [list(map(int,list(input()))) for _ in range(n+1)]

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue = deque()
#     queue.append([x,y])
#     while queue:
#         a,b = queue.popleft()
#         for i in range(4):
#             cx = a+dx[i]
#             cy = b+dy[i]
#             if 0<=cx<n and 0<=cy<m and matrix[cx][cy]==1 : #아직 방문 x 
#                 matrix[cx][cy]=matrix[a][b]+1 
#                 queue.append([cx,cy])




# bfs(0,0)
# print(matrix[n-1][m-1])

