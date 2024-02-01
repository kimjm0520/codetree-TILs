n=int(input())
num=list(map(int,input().split()))
num.sort()
arr=[]
for i in range(2*n):
    for j in range(i+1,2*n):
        arr.append(num[j]-num[i])
arr.sort()
print(arr[len(arr)//2])