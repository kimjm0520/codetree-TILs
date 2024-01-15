n=int(input())
num=[]
for i in range(n):
    a=list(input().split())
    if a[0]=='push_back':
        num.append(int(a[1]))
    elif a[0]=='pop_back':
        del num[len(num)-1]
    elif a[0]=='size':
        print(len(num))
    elif a[0]=='get':
        print(num[int(a[1])-1])