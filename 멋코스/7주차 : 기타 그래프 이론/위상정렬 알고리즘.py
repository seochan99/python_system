from collections import deque 

v,e = map(int,input().split())

indegree = [0]*(v+1)
graph =[[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1 

def topology_sort():
    result = []
    q = deque()
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입 
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    # 큐가 빌 때까지 반복 
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1 
            if indegree[i] == 0 :
                q.append(i)
    for i in result:
        print(i,end=" ")
topology_sort()