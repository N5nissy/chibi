import math
n=int(input())
a=list(map(int,input().split()))
a_s=list(set(a))
while len(a_s)!=1:
    gcd=math.gcd(a_s[-1],a_s[-2])
    lcm=int(a_s[-1]*a_s[-2]/gcd)
    a_s=a_s[:-2]
    a_s.append(lcm)
print(a_s[0])