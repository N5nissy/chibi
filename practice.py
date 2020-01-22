def solve():
    from sys import stdin
    f_i = stdin
    
    n = int(f_i.readline())
    
    items = (f_i.readline().split() for i in range(n))
    items = [(int(v), int(w), t, int(d), n) for v, w, t, d, n in items]
    items.sort()
    items = (' '.join(map(str, i)) for i in items)
    
    print('\n'.join(items))

solve()