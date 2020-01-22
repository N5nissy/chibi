def solve():
    from sys import stdin
    f_i = stdin
    
    n, q = map(int, f_i.readline().split())
    S = [[] for i in range(n)]
    ans = []
    
    for i in range(q):
        query = f_i.readline()
        op = query[0]
        if op == '0':
            t, x = query[2:].split()
            S[int(t)].append(x)
            continue
        s = S[int(query[2:])]
        if s:
            if op == '1':
                ans.append(s[-1])
            else:
                s.pop()
    
    print('\n'.join(ans))

solve()