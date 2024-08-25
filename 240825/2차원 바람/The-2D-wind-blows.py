n,m,q=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def can(r,c):
    if c<0 or c>=m or r<0 or r>=n:
        return False
    return True

def spin(r1,c1,r2,c2): #-1
    now1=graph[r1][c2]
    for i in range(c2,c1,-1):
        graph[r1][i]=graph[r1][i-1]
    
    now2=graph[r2][c2]
    for i in range(r2,r1+1,-1):
        graph[i][c2]=graph[i-1][c2]
    graph[r1+1][c2]=now1

    now1=graph[r2][c1]
    for i in range(c1,c2-1):
        graph[r2][i]=graph[r2][i+1]
    graph[r2][c2-1]=now2

    for i in range(r1,r2-1):
        graph[i][c1]=graph[i+1][c1]
    graph[r2-1][c1]=now1

def average(r,c):
    now=[[0,1],[0,-1],[1,0],[-1,0]]
    cnt=graph[r][c]
    t=1
    for i in now:
        r1=r+i[0]
        c1=c+i[1]
        if can(r1,c1):
            cnt+=graph[r1][c1]
            t+=1
    return cnt//t

def cange(r1,c1,r2,c2):
    new_graph=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[i][j]=graph[i][j]
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            new_graph[i][j]=average(i,j)
    return new_graph

r1,c1,r2,c2=map(int,input().split())
r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1

for i in range(q):
    spin(r1,c1,r2,c2)
    graph=cange(r1,c1,r2,c2)

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=' ')
    print()