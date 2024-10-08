"""n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def visit_cre():
    return [[0 for _ in range(m)] for _ in range(n)]

def graph_sum(c1,r1,c2,r2):
    cnt=0
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            cnt+=graph[i][j]
    return cnt

def visit_jud(c1,r1,c2,r2,visit): #2번째 맵의 좌표
    p=True
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            if visit[i][j]==1:
                p=False
                return p
    return p

def visit_map(c1,r1,c2,r2): #1번쨰 맵의 좌표
    visit=visit_cre()
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            visit[i][j]=1
    return visit

def sub_graph(c1,r1,c2,r2):
    visit=visit_map(c1,r1,c2,r2)
    cnt=graph_sum(c1,r1,c2,r2)
    cnt_max=-9999999999999999999999
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if visit_jud(i,j,k,l,visit):
                        cnt_max=max(cnt_max,cnt+graph_sum(i,j,k,l))
    return cnt_max

cnt_max=-9999999999999999999
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                cnt_max=max(cnt_max,sub_graph(i,j,k,l))
print(cnt_max)"""
                        

import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

            
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

            
def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹치게 됩니다.
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False


# (x1, y1), (x2, y2) 그리고
# (x3, y3), (x4, y4) 로 이루어져있는
# 두 직사각형이 겹치는지 확인하는 함수
def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()


def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때
# 두 번째 직사각형을 겹치지 않게 잘 잡아
# 최대 합을 반환하는 함수
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    
    # (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 두 번째 직사각형을 정하여
    # 겹치지 않았을 때 중
    # 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, 
                                      rect_sum(x1, y1, x2, y2) +
                                      rect_sum(i, j, k, l))
    
    return max_sum


# 두 직사각형을 잘 잡았을 때의 최대 합을 반환하는 함수
def find_max_sum():
    max_sum = INT_MIN
    
	# (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 첫 번째 직사각형을 정하여
    # 그 중 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum,
                                  find_max_sum_with_rect(i, j, k, l))
    return max_sum


ans = find_max_sum()
print(ans)