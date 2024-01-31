n,m=map(int,input().split())
arr=list(map(int,input().split()))
i=0
wifi=0
while i<len(arr)-1:
    if arr[i]==1:
        i+=2*m+1
        wifi+=1
    else:
        i+=1
print(wifi)