"""def can(r,c):
    if r<0 or r>=p or c<0 or c>=p:
        return False
    return True

def boom(r,c,n):
    r1=r
    r2=r
    c1=c
    c2=c
    for i in range(n):
        if can(r1,c):
            graph[r1][c]=0
        if can(r2,c):
            graph[r2][c]=0
        r1-=1
        r2+=1
    for i in range(n):
        if can(r,c1):
            graph[r][c1]=0
        if can(r,c2):
            graph[r][c2]=0
        c1-=1
        c2+=1

p=int(input())
graph=[list(map(int,input().split())) for _ in range(p)]
temp=[[0 for _ in range(p)] for _ in range(p)]
r,c=map(int,input().split())
boom(r-1,c-1,graph[r-1][c-1])

for j in range(p):
    pos=p-1
    for i in range(p-1,-1,-1):
        if graph[i][j]:
            temp[pos][j]=graph[i][j]
            pos-=1

for i in range(p):
    for j in range(p):
        print(temp[i][j],end=' ')
    print()
"""        
# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    
    # Step1. 폭탄이 터질 위치는 0으로 채워줍니다.
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0
	
    # Step2. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
                
    # Step3. grid로 다시 값을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

            
r, c = tuple(map(int, input().split()))
bomb(r - 1, c - 1)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()