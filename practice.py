n = int(input())

li = [int(input()) for i in range(n)]

ans = 0
for a in li:
    flag = True
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            flag = False
            break
    if flag:
        ans += 1
print(ans)