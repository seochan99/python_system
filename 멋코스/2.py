
# # computer
# n = int(input())

# #network 
# m = int(input())
# cnt = 0 
# #그래프 
# matrix = [[0]*(n+1) for _ in range(n+1)]
# visted = [0 for _ in range(n+1)]

# def dfs(start):
#     global cnt 
#     visted[start]=1 
#     for i in range(1,n+1):
#         if visted[i]==0 and matrix[start][i]==1:
#             dfs(i)
#             cnt+=1 

# #연결 끝 
# for i in range(m):
#     x,y = map(int,input().split())
#     matrix[x][y]=1
#     matrix[y][x]=1 
# print(matrix)
# dfs(1)
# print(cnt)