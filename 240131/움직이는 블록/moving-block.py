n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))
t=sum(num)//n
value=0
for i in num:
    if i>t:
        value+=i-t
print(value)