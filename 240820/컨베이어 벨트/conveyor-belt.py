n,t=map(int,input().split())
graph=[]
for _ in range(2):
    a=list(map(int,input().split()))
    graph.extend(a)

for i in range(t):
    graph.insert(0,graph.pop())

for i in range(len(graph)):
    if i==n:
        print()
    print(graph[i],end=' ')