def spin_right(r,c,m1,m2,m3,m4):
    r2=r-1
    c2=c-1
    temp=graph[r2-m4][c2-m4]
    r2-=m4
    c2-=m4
    r1=r2
    c1=c2
    for _ in range(m4):
        graph[r2][c2]=graph[r2+1][c2+1]
        r2+=1
        c2+=1
    
    temp2=graph[r1-m3][c1+m3]
    r2=r1-m3
    c2=c1+m3
    r1=r2
    c1=c2

    for _ in range(m3-1):
        graph[r2][c2]=graph[r2+1][c2-1]
        r2+=1
        c2-=1
    graph[r2][c2]=temp

    temp=graph[r1+m2][c1+m2]
    r2=r1+m2
    c2=c1+m2
    r1=r2
    c1=c2

    for _ in range(m2-1):
        graph[r2][c2]=graph[r2-1][c2-1]
        r2-=1
        c2-=1
    graph[r2][c2]=temp2

    r2=r1+m1
    c2=c1-m1
    
    for _ in range(m1-1):
        graph[r2][c2]=graph[r2-1][c2+1]
        r2-=1
        c2+=1
    graph[r2][c2]=temp

def spin_left(r,c,m1,m2,m3,m4):
    r2=r-1
    c2=c-1
    temp=graph[r2-m1][c2+m1]
    r2-=m1
    c2+=m1
    r1=r2
    c1=c2
    for _ in range(m1):
        graph[r2][c2]=graph[r2+1][c2-1]
        r2+=1
        c2-=1
    
    temp2=graph[r1-m2][c1-m2]
    r2=r1-m2
    c2=c1-m2
    r1=r2
    c1=c2

    for _ in range(m2-1):
        graph[r2][c2]=graph[r2+1][c2+1]
        r2+=1
        c2+=1
    graph[r2][c2]=temp

    temp=graph[r2+m3][c2-m3]
    r2=r1+m3
    c2=c1-m3
    r1=r2
    c1=c2

    for _ in range(m3-1):
        graph[r2][c2]=graph[r2-1][c2+1]
        r2-=1
        c2+=1
    graph[r2][c2]=temp2
    
    r2=r1+m4
    c2=c1+m4

    for _ in range(m4-1):
        graph[r2][c2]=graph[r2-1][c2-1]
        r2-=1
        c2-=1
    graph[r2][c2]=temp

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
r,c,m1,m2,m3,m4,dip=map(int,input().split())

if dip:
    spin_right(r,c,m1,m2,m3,m4)
else:
    spin_left(r,c,m1,m2,m3,m4)

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=' ')
    print()