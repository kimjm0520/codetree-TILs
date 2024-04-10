from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
visit=[[0 for _ in range(m)] for _ in range(n)]
q=deque()

def can(x,y):
    if not (0<=x<m and 0<=y<n):
        return False
    elif visit[y][x]!=0 or graph[y][x]!=1:
        return False
    else:
        return True

def bfs():
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        cur=q.popleft()
        x=cur[0]
        y=cur[1]
        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            if can(new_x,new_y):
                visit[new_y][new_x]=1
                q.append([new_x,new_y])
        if x==m-1 and y==n-1:
            return 1

q.append([0,0])
visit[0][0]=1
a=bfs()
if a:
    print(1)
else:
    print(0)