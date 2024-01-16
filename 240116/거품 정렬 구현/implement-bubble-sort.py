n=int(input())
num=list(map(int,input().split()))
for i in range(n):
    for j in range(n-1):
        if num[j]>num[j+1]:
            tem=num[j]
            num[j]=num[j+1]
            num[j+1]=tem
for i in num:
    print(i,end=' ')