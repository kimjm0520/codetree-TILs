n,m=map(int,input().split())
num=[]
for _ in range(n):
    a=list(map(int,input().split()))
    num.append(a)
visited=[[0 for _ in range(m)] for _ in range(n)]
dx=[1,0]
dy=[0,1]

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
    global dx,dy
    for dx,dy in zip(dx,dy):
        new_x, new_y = x+dx, y+dy

        if can(x, y):
            visited[x][y]=1
            grid_dfs(x,y)
    return justice(x,y)

visited[0][0]=1
x,y=0,0
print(grid_dfs(x,y))