from collections import deque 
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global ans 
    queue = deque()
    copyGraph = copy.deepcopy(graph) #깊은 복사 
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 2:
                queue.append((i,j)) #바이러스 위치 저장 
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if cx<0 or cx>=n or cy<0 or cy>=m : #범위체크 
                continue
            if copyGraph[cx][cy] == 0 : #0이라면 ! 감염가능한곳 
                copyGraph[cx][cy] = 2
                queue.append((cx,cy)) #감염시키기 
    cnt = 0 
    for i in range(n):
        cnt+=copyGraph[i].count(0)
        
    ans = max(ans,cnt)

def wallMake(cnt):
    if cnt == 3: #벽설치 끝 
        bfs() 
        return 
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1 
                wallMake(cnt+1)
                graph[i][j] = 0

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

ans = 0 
wallMake(0)
print(ans)


