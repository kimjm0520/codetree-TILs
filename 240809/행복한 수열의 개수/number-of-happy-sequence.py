n,m=map(int,input().split())
answer=0
graph=[]
for _ in range(n):
    a=list(map(int,input().split()))
    graph.append(a)
for i in range(n):
    cnt=1
    for j in range(1,n):
        if graph[i][j-1]==graph[i][j]:
            cnt+=1
    if cnt>=m:
        answer+=1
for j in range(n):
    cnt=1
    for i in range(1,n):
        if graph[i-1][j]==graph[i][j]:
            cnt+=1
    if cnt>=m:
        answer+=1
print(answer)