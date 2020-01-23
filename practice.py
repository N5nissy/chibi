import sys
cin = sys.stdin
while True:
    n = int(cin.readline())
    if n == 0:break
    c = {}
    for _ in range(n):
        a,b = cin.readline().strip().split()
        c[a] = b
    m = int(cin.readline())
    ans = ''
    for _ in range(m):
        a = cin.readline().strip()
        ans+=c[a] if a in c else a
    print(ans)