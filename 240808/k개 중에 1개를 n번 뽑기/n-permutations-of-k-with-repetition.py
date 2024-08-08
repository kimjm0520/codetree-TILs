k,n=map(int,input().split())
answer=[]
def print_pop():
    for i in answer:
        print(i,end=' ')
    print()

def num(cnt):
    if cnt>n:
        print_pop()
        return
    for i in range(1,k+1):
        answer.append(i)
        num(cnt+1)
        answer.pop()
    
num(1)