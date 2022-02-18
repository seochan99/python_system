from collections import deque 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,k = map(int,input().split())
graph = []
virus = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0: #바이러스 있다면 
            virus.append((graph[i][j],i,j)) #바이러스 종류, 위치 
s,x,y = map(int,input().split()) #s초뒤에 x,y위치의 바이러스 

def bfs(s,x,y):
    queue = deque(virus) #바이러스 위치 넣기 
    cnt = 0 
    while queue:
        if cnt == s: #시간이 다됐음
            break 
        for _ in range(len(queue)):
            prev, virusX,virusY = queue.popleft()
            for i in range(4):
                cx = virusX + dx[i]
                cy = virusY + dy[i]
                if 0<=cx<n and 0<=cy<n:
                    if graph[cx][cy] == 0:
                        graph[cx][cy] = graph[virusX][virusY]
                        queue.append((graph[cx][cy],cx,cy))
        cnt+=1 
    return graph[x-1][y-1] #해당위치 출력 

virus.sort() #바이러스 우선순위 정렬 
print(bfs(s,x,y))

