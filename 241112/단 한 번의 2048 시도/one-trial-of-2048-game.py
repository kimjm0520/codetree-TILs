graph=[list(map(int,input().split())) for _ in range(4)]
dir1=input()

def gravity_right(graph):
    for i in range(4):
        for j in range(3,0,-1):
            if graph[i][j]==graph[i][j-1]:
                graph[i][j]=graph[i][j]*2
                graph[i][j-1]=0
    for i in range(4):
        for j in range(2,-1,-1):
            while graph[i][j+1]==0:
                graph[i][j+1]=graph[i][j]
                graph[i][j]=0
                j+=1
                if j==3:
                    break

def gravity_left(graph):
    for i in range(4):
        for j in range(3):
            if graph[i][j]==graph[i][j+1]:
                graph[i][j]=graph[i][j]*2
                graph[i][j+1]=0
    for i in range(4):
        for j in range(1,4):
            while graph[i][j-1]==0:
                graph[i][j-1]=graph[i][j]
                graph[i][j]=0
                j-=1
                if j==0:
                    break

def gravity_up(graph):
    for j in range(4):
        for i in range(3):
            if graph[i][j]==graph[i+1][j]:
                graph[i][j]=graph[i][j]*2
                graph[i][j+1]=0
    for j in range(4):
        for i in range(1,4):
            while graph[i-1][j]==0:
                graph[i-1][j]=graph[i][j]
                graph[i][j]=0
                i-=1
                if i==0:
                    break

def gravity_down(graph):
    for j in range(4):
        for i in range(3,0,-1):
            if graph[i][j]==graph[i-1][j]:
                graph[i][j]=graph[i][j]*2
                graph[i-1][j]=0
    for j in range(4):
        for i in range(2,-1,-1):
            while graph[i+1][j]==0:
                graph[i+1][j]=graph[i][j]
                graph[i][j]=0
                i+=1
                if i==3:
                    break

if dir1=="R":
    gravity_right(graph)
elif dir1=="L":
    gravity_left(graph)
elif dir1=='U':
    gravity_up(graph)
elif dir1=='D':
    gravity_down(graph)

for i in range(4):
    for j in range(4):
        print(graph[i][j],end=' ')
    print()