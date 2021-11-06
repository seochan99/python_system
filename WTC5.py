import sys
input = sys.stdin.readline
from collections import deque #BFS

dx = [1,0]
dy = [0,1]

def solution(rows, columns):
    graph = [[0] * columns for _ in range(rows)] #그래프 생성
    zeroNum=1
    graph[0][0]=1 # 시작점 1 
    queue = deque()
    queue.append([0,0])
    if(rows!=columns):
        while queue:
            a,b = queue.popleft()
            if(graph[a][b]%2==1): #홀수 
                cx = a+dx[1]
                cy = b+dy[1]
                if(cy>=columns):
                    cy=0
                if(graph[cx][cy]==0):#처음가는곳 
                    zeroNum+=1
                graph[cx][cy]=graph[a][b]+1
                queue.append([cx,cy])
                if(zeroNum==columns*rows): #다채움
                    break 
            else : #짝수 
                cx = a+dx[0]
                cy = b+dy[0]
                if(cx>=rows):
                    cx=0
                if(graph[cx][cy]==0):#처음가는곳 
                    zeroNum+=1
                graph[cx][cy]=graph[a][b]+1
                queue.append([cx,cy])
                if(zeroNum==columns*rows): #다채움
                    break
    else :
        while queue:
            a,b = queue.popleft()
            if(graph[a][b]%2==1): #홀수 
                cx = a+dx[1]
                cy = b+dy[1]
                if(cy>=columns):
                    cy=0
                if(graph[cx][cy]==0):#처음가는곳 
                    graph[cx][cy]=graph[a][b]+1
                    queue.append([cx,cy])
                else :
                    break 
            else : #짝수 
                cx = a+dx[0]
                cy = b+dy[0]
                if(cx>=rows):
                    cx=0
                if(graph[cx][cy]==0):#처음가는곳 
                    graph[cx][cy]=graph[a][b]+1
                    queue.append([cx,cy])
                else:
                    break 
    return graph
print(solution(4,4))