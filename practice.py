n = int(input())
num = list(map(int, input().split()))

ans = list(set(num))
ans.sort()
print(' '.join(str(a) for a in ans))
