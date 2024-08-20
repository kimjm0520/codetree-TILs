n,t=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

for _ in range(t):
    temp=a[-1]
    
    for i in range(n-1,0,-1):
        a[i]=a[i-1]
    a[0]=c[-1]

    for i in range(n-1,0,-1):
        c[i]=c[i-1]
    c[0]=b[-1]

    for i in range(n-1,0,-1):
        b[i]=b[i-1]
    b[0]=temp

for i in [a,b,c]:
    for j in i:
        print(j,end=' ')
    print()