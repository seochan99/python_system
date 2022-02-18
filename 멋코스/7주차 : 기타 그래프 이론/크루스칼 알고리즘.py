# #특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드를 찾을 때까지 재귀 호출 
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a 
    else :
        parent[a] = b
    
v,e = map(int,input().split())
parent = [0] * (v+1) #부모 테이블 초기화 

edges = []
result = 0
#부모 테이블 상에서, 부모를 자기 자신으로 초기화 
for i in range(1,v+1):
    parent[i] = i 

#union 연산을 각각 수행 
for i in range(e):
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정 
    edges.append((cost,a,b))

#간선을 비용순으로 정렬 
edges.sort()
    
for edge in edges:
    cost, a, b = edge 
    #사이클이 발생하지 않는 경우에만 집합에 포함 
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost 
print(result)