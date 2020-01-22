n = int(input())
S = set()
for i in range(n):
    query, x = map(int, input().split())
    if query == 0:
        S.add(x)
        print(len(S))
    else:
        print(1 if x in S else 0)
        