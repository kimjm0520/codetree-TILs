n,m=map(int,input().split())
num=[]
for _ in range(n):
    a=list(map(int,input().split()))
    num.append(a)
visited=[[0 for _ in range(m)] for _ in range(n)]
p=[]

def justice(x,y):
    if x == (m-1) and y == (n-1):
        return 1
    return 0

def pos(x, y):
    return (0 <= x <= (m-1)) and (0 <= y <= (n-1))

def can(x,y):
    if not pos(x,y):
        return False
    if visited[x][y] or num[x][y] == 0:
        return False
    return True

def grid_dfs(x,y):
    global p
    dx=[1,0]
    dy=[0,1]
    for i in range(2):
        new_x, new_y = x+dx[i], y+dy[i]

        if can(new_x, new_y):
            visited[new_x][new_y]=1
            grid_dfs(new_x,new_y)
    a=justice(x,y)
    p.append(a)

visited[0][0]=1
x,y=0,0
grid_dfs(x,y)
print(p[0])