n=int(input())
num=list(map(int,input().split()))
for i in range(n):
    min_v=i
    for j in range(i+1,n):
        if num[min_v]>num[j]:
            min_v=j
    tem=num[i]
    num[i]=num[min_v]
    num[min_v]=tem
for i in num:
    print(i,end=' ')