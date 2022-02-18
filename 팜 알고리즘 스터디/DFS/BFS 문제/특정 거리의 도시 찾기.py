import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split()) 

graph = [[] for _ in range(n+1)]
result = [-1] * (n+1)
result[x] = 0 

for _ in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)

queue = deque([x])

while queue:
    now = queue.popleft()
    for nextcity in graph[now]:
        if result[nextcity] == -1:
            result[nextcity] = result[now] + 1 
            queue.append(nextcity) 
for i in range(n+1):
    if result[i] == k:
        print(i)
if k not in result:
    print(-1)