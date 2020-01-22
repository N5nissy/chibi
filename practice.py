q = int(input())

l = []
for _ in range(q):
    a = input().split()
    if a[0] == "2":
        l.pop()
    else:
        m,q = map(int, a)
        if m == 0:
            l.append(q)
        else:
            print(l[q])