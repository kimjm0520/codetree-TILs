n=int(input())
graph=[]
cnt=0
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)


for i in range(n-2):
    for j in range(n-2):
        for c1 in range(i,i+3):
            for r1 in range(j,j+3):
                if graph[c1][r1]==1:
                    cnt+=1
print(cnt)