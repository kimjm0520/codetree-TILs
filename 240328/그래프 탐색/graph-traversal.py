n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
v=0

for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(vertex):
    global v
    for cur_v in graph[vertex]:
        if not visited[cur_v]:
            v+=1
            visited[cur_v]=True
            dfs(cur_v)

root_vertex = 1
visited[root_vertex]=True
dfs(root_vertex)
print(v)