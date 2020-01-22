n,m=map(int,input().split())
s=x=0
for i in range(m):
    a,b=map(int,input().split())
    if n-a>0:s+=n-a
    if n-a>x:x=n-a
print(s-x)