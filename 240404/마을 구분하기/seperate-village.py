n=int(input())
graph=[]
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
visit=[[0 for _ in range(n)] for _ in range(n)]

def rge(x,y):
    return 0<= x and x <n and 0<=y and y<n

def can(x,y):
    if not rge(x,y):
        return False
    elif visit[y][x]==1 or graph[y][x]==0:
        return False
    else:
        return True

def dfs(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    t=0
    for i in range(len(dx)):
        new_x, new_y = x+dx[i], y+dy[i]
        if can(new_x,new_y):
            visit[new_y][new_x]=1
            t+=dfs(new_x,new_y)
    return t+1

vl=[]
for y in range(n):
    for x in range(n):
        if graph[y][x]==1 and visit[y][x]==0:
            visit[y][x]=1
            p=dfs(x,y)
            vl.append(p)
vl.sort()
print(len(vl))
for i in vl:
    print(i)