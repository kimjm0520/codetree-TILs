n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
coin=0
for i in range(n):
    coin+=graph[i].count(1)

k=0
while k**2+k <= (m*coin-1)//2:
    k+=1
k-=1

def can(c1,r1):
    if c1<0 or c1>=n or r1<0 or r1>=n:
        return False
    return True

def run(c1,r1):
    b=-t
    cnt=0
    for i in range(c1-t,c1+t+1):
        a=abs(b)
        for j in range(r1-t+a,r1+t+1-a):
            if can(i,j):
                cnt+=graph[i][j]
        b+=1
    return cnt

cnt_max=0

for t in range(k):
    for i in range(n):
        for j in range(n):
            cnt=run(i,j)
            if cnt_max<cnt and (t*t+(t+1)*(t+1) <= m*cnt): 
                cnt_max=cnt

print(cnt_max)