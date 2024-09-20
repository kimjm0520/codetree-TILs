n,m=map(int,input().split())
bomb=[int(input()) for _ in range(n)]

def boom(m):
    pos=bomb[0]
    cnt=1
    sign=0
    for i in range(1,len(bomb)):
        if cnt==m:
            sign=1
            for j in range(cnt,0,-1):
                bomb[i-j]=0
            pos=bomb[i]
            cnt=1
        elif pos==bomb[i]:
            cnt+=1
        else:
            pos=bomb[i]
            cnt=1
    if cnt==m:
        sign=1
        for j in range(cnt):
            bomb[i-j]=0
    return sign
        

def clean():
    global bomb
    temp=[]
    for i in range(len(bomb)):
        if bomb[i]:
            temp.append(bomb[i])
    bomb=temp[:]

sign=1
while sign and len(bomb)>0:
    sign=boom(m)
    clean()
print(len(bomb))
for i in range(len(bomb)):
    print(bomb[i])