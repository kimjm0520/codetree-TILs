n=int(input())
num=list(map(int,input().split()))
arr=num[:]
arr.sort()
cnt=0
for i in range(n):
    if arr==num:
        break
    tmp=num[0]
    del num[0]
    for i in range(n-1):
        if tmp==1:
            if num[i]==n:
                num.insert(i+1,tmp)
                break
        elif tmp+1==num[i]:
            num.insert(i,tmp)
            break
        elif tmp==n:
            num.append(tmp)
            break
    cnt+=1
print(cnt)