n = int(input())
alist = list(map(int, input().split()))

ans = 0
cnt = 0
while alist != []:
    a = alist.pop(0)

    if a == 1:
        cnt += 1
    else:
        cnt = 0

    if cnt > ans:
        ans = cnt

print(ans + 1)