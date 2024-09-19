n=int(input())
block=[int(input()) for _ in range(n)]
temp=[]
s,e=map(int,input().split())
for i in range(len(block)):
    if i<s-1 or i>e-1:
        temp.append(block[i])
block=temp[:]
temp=[]
s,e=map(int,input().split())
for i in range(len(block)):
    if i<s-1 or i>e-1:
        temp.append(block[i])
print(len(temp))
for i in temp:
    print(i)