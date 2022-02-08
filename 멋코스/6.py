# 다익스트라 알고리즘 
import sys
from turtle import distance 
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미 하는 10억 

#노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split())
# start num 
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기 
graph =[[] for _ in range(n+1)] 
#방문한 적이 있는지 체크하는 목적의 리스트 제작 
visted = [False] * (n+1)

# 모든 간선 정보를 입력받기 
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 C
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수 
def get_smallest_node():
    min_value = INF 
    idx= 0 # 가장 최단 거리가 짧은 노드 번호 (인덱스) 
    for i in range(1,n+1):
        if (distance[i]<min_value and not visted[i]) : #만약 거리가 최소설정거리(무한)보다 작고, 방문하지 않은 노드라면
            min_value = distance[i]
            idx = i
    return idx 

def dijkstra(start):
    # 시작 노드에 대해 초기화 
    distance[start] = 0
    visted[start] = True 
    for j in graph[start]:
        distance[j[0]] = j[1] #j[0] : b번 노드 j[1]: 비용 
        #start 에서 j[0]번 노드로 가는 비용 j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대한 반복 
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리 
        now = get_smallest_node()
        visted[now] = True 
        # 현재 노드와 연겨ㅕㄹ된 다른 노드를 확인 
        for j in graph[now]:
            cost = distance[now]+j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost<distance[j[0]]:
                distance[j[0]] = cost 
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print("도달못함")
    else : #도달할 수 있는 경우 거리를 출력 
        print(distance[i]) 
    