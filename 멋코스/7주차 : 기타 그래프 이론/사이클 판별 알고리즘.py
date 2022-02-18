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

#부모 테이블 상에서, 부모를 자기 자신으로 초기화 
for i in range(1,v+1):
    parent[i] = i 

cycle = False # 사이클 발생여부 

#union 연산을 각각 수행 
for i in range(e):
    a,b = map(int,input().split())
    # 사이클이 발생한 경우 종료 
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True 
        break 
    else:
        union_parent(parent,a,b)
    
if cycle:
    print("사이클 발생")
else :
    print("사이클 발생 X ")