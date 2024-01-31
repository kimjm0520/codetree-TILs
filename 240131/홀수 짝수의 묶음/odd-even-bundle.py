n=int(input())
num=list(map(int,input().split()))
even,odd=0,0
cnt=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
if even>=odd:
    print(odd*2)
else:
    odd-=even
    cnt=even*2
    while odd>0:
        if odd==4 or odd==2:
            cnt+=1
            odd-=4
        elif odd==1:
            cnt-=1
            odd-=1
        else:
            odd-=3
            cnt+=2
    print(cnt)