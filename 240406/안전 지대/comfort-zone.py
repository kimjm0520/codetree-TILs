n,m=map(int,input().split())
graph=[]
for i in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
mk=0
mg=0

def can(x,y):
    if not (0<=x<m and 0<=y<n):
        return False
    elif visit[y][x]==1 or graph[y][x]<=k:
        return False
    else:
        return True

def dfs(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        new_x=x+dx[i]
        new_y=y+dy[i]
        if can(new_x,new_y):
            visit[new_y][new_x]=1
            dfs(new_x,new_y)

for k in range(1,101):
    cnt=0
    visit=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if k<graph[i][j] and visit[i][j]==0:
                dfs(j,i)
                cnt+=1
    if cnt>mg:
        mg=cnt
        mk=k
    if cnt==0:
        break
print(mk,mg)