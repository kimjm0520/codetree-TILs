n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

def can(c,r):
    if c<0 or c>=n or r<0 or r>=n:
        return False
    return True

def case1(c,r,ans):
    cnt=0
    p=False
    while can(c,r):
        ans+=graph[c][r]
        c-=1
        r+=1
        cnt+=1
    while (not p) and cnt>1:
        c+=1
        r-=1
        cnt-=1
        ans-=graph[c][r]
        if can(c-1,r-1):
            p=True
            return c,r,ans,p

    return c,r,ans,p
        
def case2(c,r,ans):
    cnt=0
    p=False
    while can(c,r):
        ans+=graph[c][r]
        c-=1
        r-=1
        cnt+=1
    while (not p) and cnt>1:
        c+=1
        r+=1
        cnt-=1
        ans-=graph[c][r]
        if can(c+1,r-1):
            p=True
            return c,r,ans,p
        
    return c,r,ans,p

def case3(c,r,ans):
    cnt=0
    p=False
    while can(c,r):
        ans+=graph[c][r]
        c+=1
        r-=1
        cnt+=1
    while (not p) and cnt>1:
        c-=1
        r+=1
        cnt-=1
        ans-=graph[c][r]
        if can(c+1,r+1):
            p=True
            return c,r,ans,p
        
    return c,r,ans,p

def case4(c,r,c1,r1,ans):
    p=False
    while can(c,r) and (c!=c1 and r!=r1):
        ans+=graph[c][r]
        c+=1
        r+=1
    if c==c1 and r==r1:
        p=True
    return c,r,ans,p   


def qua(c,r):
    p=True
    c1,r1=c,r
    ans=0
    for i in range(1,5):
        if not p:
            return 0
        if i==1:
            c,r,ans,p=case1(c,r,ans)
            
        elif i==2:
            c,r,ans,p=case2(c,r,ans)
            
        elif i==3:
            c,r,ans,p=case3(c,r,ans)
            
        elif i==4:
            c,r,ans,p=case4(c,r,c1,r1,ans)
            
    if not p:
        return 0
    return ans

ans_max=0

for i in range(n):
    for j in range(n):
        ans=qua(i,j)
        if ans_max<ans:
            ans_max=ans
print(ans_max)