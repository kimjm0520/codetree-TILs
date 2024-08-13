n,t=map(int,input().split())
com=list(input())
graph=[list(map(int,input().split())) for _ in range(n)]
c,r=n//2,n//2
p=0

def can(c,r):
    if c<0 or c>=n or r<0 or r>=n:
        return False
    return True

def dire(p,com):
    if com=='L':
        if p==0:
            p=3
        elif p==1:
            p=0
        elif p==2:
            p=1
        elif p==3:
            p=2
    elif com=='R':
        if p==0:
            p=1
        elif p==1:
            p=2
        elif p==2:
            p=3
        elif p==3:
            p=0
    return p

def run(c,r,p):
    c1=c
    r1=r
    a=False
    if p==0:
        c-=1
    elif p==1:
        r+=1
    elif p==2:
        c+=1
    elif p==3:
        r-=1
    if can(c,r):
        a=True
        return c,r,a
    return c1,r1,a

ans=graph[c][r]

for i in com:
    if i=='F':
        c,r,a=run(c,r,p)
        if a:
            ans+=graph[c][r]
    else:
        p=dire(p,i)
print(ans)