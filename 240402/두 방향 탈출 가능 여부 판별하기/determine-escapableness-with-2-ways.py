n,m=map(int,input().split())
graph=[]
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
vistied=[[0 for _ in range(m)] for _ in range(n)]
pos=[]

def ran(x,y):
    return (0<=x and x<m) and (0<=y and y<n)

def can(x,y):
    if not ran(x,y):
        return False
    if vistied[y][x]==1 or graph[y][x]==0:
        return False
    return True

def greid_dfs(x,y):
    global pos
    dx, dy=[0,1], [1,0]
    for i in range(2):
        new_x, new_y = x+dx[i], y+dy[i]
        if can(new_x,new_y):
            vistied[new_y][new_x]=1
            greid_dfs(new_x, new_y)
    if x==(m-1) and y==(n-1):
        pos.append(1)
    else:
        pos.append(0)
    

vistied[0][0]=1
greid_dfs(0,0)
print(sum(pos))