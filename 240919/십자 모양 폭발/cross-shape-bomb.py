def can(r,c):
    if r<0 or r>=p or c<0 or c>=p:
        return False
    return True

def boom(r,c,n):
    r1=r
    r2=r
    c1=c
    c2=c
    for i in range(n):
        if can(r1,c):
            graph[r1][c]=0
        if can(r2,c):
            graph[r2][c]=0
        r1-=1
        r2+=1
    for i in range(n):
        if can(r,c1):
            graph[r][c1]=0
        if can(r,c2):
            graph[r][c2]=0
        c1-=1
        c2+=1

p=int(input())
graph=[list(map(int,input().split())) for _ in range(p)]
temp=[[0 for _ in range(p)] for _ in range(p)]
r,c=map(int,input().split())
boom(r-1,c-1,graph[r-1][c-1])

for j in range(p):
    pos=p-1
    for i in range(p-1,-1,-1):
        if graph[i][j]:
            temp[pos][j]=graph[i][j]
            pos-=1

for i in range(p):
    for j in range(p):
        print(temp[i][j],end=' ')
    print()