s=list(input())

def length(s):
    p=''
    cnt=1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            cnt+=1
        else:
            p+=s[i-1]+str(cnt)
            cnt=1
    p+=s[-1]+str(cnt)
    return len(p)

def shift(s):
    now=s[-1]
    for i in range(len(s)-1,0,-1):
        s[i]=s[i-1]
    s[0]=now
    return s

leng_min=length(s)

n=len(s)

for i in range(n-1):
    s=shift(s)
    leng=length(s)
    if leng_min>leng:
        leng_min=leng
print(leng_min)